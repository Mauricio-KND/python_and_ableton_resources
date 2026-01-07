from __future__ import absolute_import, print_function, unicode_literals
import Live
#import builtins import range
from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.EncoderElement import EncoderElement
from _Framework.SliderElement import SliderElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.SubjectSlot import subject_slot
from _Framework.TransportComponent import TransportComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.Layer import Layer
from _Framework.ModesComponent import AddLayerMode, LayerMode, ModesComponent

from .GLOBALS import *
from .nanoCustom import MyCustomComponent

# 0 = Note
# 1 = CC
# 0 = non momentary controls
# 1 = momentary controls

class Nano(ControlSurface):
    __module__ = __name__
    __doc__ = "A script for the NanoKontrol2"
    def __init__(self, c_instance): # Import CS Component
        ControlSurface.__init__(self, c_instance)
        self.msg_test()
        with self.component_guard():    # Context manager, which guards code. Prevents unnecesary updating and enables optimisations
            self._create_controls()
            self._create_transport()
            self._create_device()
            mixer = self._create_mixer()
            self._session = self._create_session()
            self._create_custom()
            self._create_modes()
            self._session.set_mixer(mixer)


    def msg_test(self):
        self.log_message("================== LOG FOR CUSTOM NANO SCRIPT ==================")
        self.show_message('Nano Script Loaded')

    def _create_controls(self):
        def make_button(identifier, name, midi_type=1):
            self.log_message('Creating %s, identifier %s' % (name, identifier))
            return ButtonElement(is_momentary=True, msg_type=midi_type, channel=chan, identifier=identifier, name=name)

        def make_encoder(identifier, name):
            return EncoderElement(1, channel=chan, identifier=identifier, map_mode=Live.MidiMap.MapMode.absolute,name=name)

        def make_slider(identifier, name):
            return SliderElement(1, channel=chan, identifier=identifier, name=name)
        # Create the faders
        self._faders = ButtonMatrixElement(rows=[
            [make_slider(0 + i, 'Volume_%d' % (i + 1)) for i in range(8)]])
        # Create the SOLO buttons
        self._solo_buttons = ButtonMatrixElement(rows=[
            [make_button(32 + i, 'Solo_%d' % (i + 1)) for i in range(8)]])
        self._mute_buttons = ButtonMatrixElement(rows=[
            [make_button(48 + i, 'Mute_%d' % (i + 1)) for i in range(8)]])
        self._arm_buttons = ButtonMatrixElement(rows=[
            [make_button(64 + i, 'Arm_%d' % (i + 1)) for i in range(8)]])
        self._encoders = ButtonMatrixElement(rows=[
            [make_encoder(16 + i, 'Pan_Device_%d' % (i + 1)) for i in range(8)]])

        self._up_btn = make_button(62, 'Up')
        self._down_btn = make_button(61, 'Down')

        self._track_left_btn = make_button(58, 'Track_Left')
        self._track_right_btn = make_button(59, 'Track_right')

        self._rewind_btn = make_button(43, 'Rewind')
        self._forward_btn = make_button(44, 'Forward')

        self._loop_btn = make_button(46, 'Cycle')
        self._set_btn = make_button(60, 'Set')
        self._stop_btn = make_button(42, 'Stop')

        # Mode Buttons
        self._regular_mode_btn = make_button(41, 'Regular_Mode_Button')
        self._shift_mode_btn = make_button(45, 'Shift_Mode_Button')

    def _create_session(self):
        self.log_message("================== Session Created ==================")
        self._session = SessionComponent(num_tracks=num_tracks, num_scenes=num_scenes, is_enabled=True, auto_name=True)
        self.set_highlighting_session_component(self._session)
        self._session.set_track_bank_buttons(self._track_right_btn, self._track_left_btn)
        self._session.set_scene_bank_buttons(self._up_btn, self._down_btn)
        self._session.scene(0).set_launch_button(self._rewind_btn)
        self._session.scene(1).set_launch_button(self._forward_btn)
        self._session.set_stop_all_clips_button(self._stop_btn)
        self._on_session_offset_changed.subject = self._session
        return self._session

    def _create_transport(self):
        self.log_message("================== Transport Created ==================")
        self._transport = TransportComponent(self)
        self._transport.set_loop_button(self._loop_btn)
        self._transport.set_metronome_button(self._set_btn)

    def _create_device(self):
        self.log_message("================== Device Created ==================")
        self._device = DeviceComponent(name='Device_Component', is_enabled=True, device_selection_follows_track_selection=True)

    def _create_mixer(self):
        self.log_message("================== Mixer Created ==================")
        self._mixer = MixerComponent(num_tracks, name='Mixer')
        # Make sure we see the first track upon opening the set
        self.song().view.selected_track = self._mixer.channel_strip(0)._track
        self._mixer.set_volume_controls(self._faders)
        return self._mixer

    def _create_custom(self):
        self._custom = MyCustomComponent()

    def _create_modes(self):
        self._modes = ModesComponent('Custom_Mode')
        self._modes.add_mode('regular_mode', LayerMode(self._mixer, Layer(pan_controls=self._encoders,
                                                                          solo_buttons=self._solo_buttons,
                                                                          mute_buttons=self._mute_buttons,
                                                                          arm_buttons=self._arm_buttons)))
        self._modes.add_mode('shift_mode', (
            AddLayerMode(self._device, Layer(parameter_controls=self._encoders,
                                             on_off_button=self._solo_buttons[6])),
            AddLayerMode(self._transport, Layer(record_button=self._solo_buttons[0],
                                                tap_tempo_button=self._solo_buttons[1])),
            AddLayerMode(self._session, Layer(clip_launch_buttons=self._mute_buttons)),
            AddLayerMode(self._mixer, Layer(track_select_buttons=self._arm_buttons)),
            AddLayerMode(self._custom, Layer(unmute_all_button=self._solo_buttons[2],
                                             toggle_view_button=self._solo_buttons[3],
                                             prev_device_button=self._solo_buttons[4],
                                             next_device_button=self._solo_buttons[5],
                                             dev_reset_button=self._solo_buttons[7]))))

        self._modes.layer = Layer(regular_mode_button=self._regular_mode_btn,
                                  shift_mode_button=self._shift_mode_btn)

        self._modes.selected_mode = 'regular_mode'
        self._on_selected_mode.subject = self._modes


    @subject_slot('selected_mode')
    def _on_selected_mode(self, mode):
        if mode == 'regular_mode':
            self.show_message('Regular Mode')
        else:
            self.show_message('Shift Mode')



    @subject_slot('offset')
    def _on_session_offset_changed(self):
        session = self._on_session_offset_changed.subject
        self._show_controlled_tracks_message(session)

    def _show_controlled_tracks_message(self, session):
        self.log_message("================== This works ==================")
        start = session.track_offset() + 1
        end = min(start + 8, len(session.tracks_to_use()))
        if start < end:
            self.show_message('Controlling Track %d to %d' % (start, end))
        else:
            self.show_message('Controlling Track %d' % start)



