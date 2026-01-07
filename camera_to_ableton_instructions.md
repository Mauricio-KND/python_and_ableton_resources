# Webcam MIDI Control System - Execution Guide

## System Requirements
- macOS with Python 3.9+ virtual environment
- Ableton Live 11/12 with API enabled
- Physical webcam (internal or external)
- python packages: mediapipe, numpy, python-rtmidi, opencv-python

## Execution Steps
1. **Activate virtual environment**:
```bash
source venv/bin/activate
```

2. **Run the camera script**:
```bash
python3 "Part_B/B21_-_Sending_data_to_Ableton.py"
```

3. **Expected Behavior**:
- Webcam feed window appears (labeled "Your Face goes here")
- Hand tracking visualization overlays the video
- Left side of screen (X < 540) controls MIDI CC values (Y-axis mapped to 0-127)
- Right side of screen (X > 540) controls MIDI notes (Y-axis mapped to MIDI notes 60-92)
- MIDI output named "Ableton Camera Control" appears in system MIDI ports

4. **Ableton Configuration**:
- In Ableton Live: Create new MIDI track
- Set Input Type to "Ableton Camera Control" (or corresponding MIDI port name)
- Enable MIDI input monitoring
- Map track parameters to incoming MIDI CC data

## Troubleshooting
- **No webcam feed**: Check camera permissions in System Settings > Privacy
- **MIDI not working**: 
  - Verify Ableton's MIDI preferences include the virtual port
  - Try `midicc` utility to test MIDI output: `pip install midicc && midicc`
- **Performance issues**: 
  - Reduce webcam resolution: `cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)` in script
  - Adjust hand detection confidence values in `mpHands.Hands()` initialization

## Technical Notes
- The system divides the webcam frame horizontally:
  - Left half (0-540px): Continuous Controller (CC) data output
  - Right half (540-1080px): Note event generation
- Y-axis position maps to:
  - CC values (0-127) in left half
  - MIDI note numbers (60-92) in right half
- Hand landmarks detected using MediaPipe's hand solution (17 key points)