# Python and Ableton Live Integration Project Documentation

## Course Overview
This repository contains practical implementations from the Udemy course "Learn Python through Music with Ableton Live" (https://globant.udemy.com/course/learning-python-with-ableton-live/). The materials focus on Python programming concepts applied to music production and Ableton Live integration, with emphasis on real-time control systems and algorithmic composition.

## Directory Structure
```
python_and_ableton_resources/
├── Part B/               # Core Python implementations for musical applications
│   ├── B7 - Send CC Data.py
│   ├── B21 - Sending data to Ableton.py
│   └── ... (fundamental implementations)
├── Part C/               # Advanced Ableton API integrations
│   ├── C1 - The LOM.py
│   ├── C8 - Play Clips.py
│   └── ... (API interaction examples)
├── Part D/               # MIDI Remote Script framework
│   └── nano/             # Custom control surface implementation
└── 00data/               # Scientific datasets for algorithmic composition
```

## Technical Features
- Real-time MIDI control surface implementation for dynamic parameter modulation
- OSC communication protocols for inter-application data exchange
- Algorithmic composition systems using scientific datasets
- Custom MIDI controller scripting framework
- Webcam-based gesture recognition for musical input control

## System Requirements
- Ableton Live 11/12 (API access enabled in Preferences > API)
- Python 3.9+
- Required Python packages:
  - python-osc
  - mediapipe
  - numpy

## Installation Procedure
1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install required dependencies:
```bash
pip install python-osc mediapipe numpy
```

3. Configure Ableton Live API access:
   - Open Ableton Live Preferences > API
   - Enable "Allow Python API" and "Allow OSC API"

## Usage Examples
```python
# MIDI CC Data Transmission (Part B7)
from ableton.midi import CCData
cc = CCData(channel=1, control=20, value=127)
cc.send_to_ableton()  # Transmit control change to Ableton

# Clip Automation (Part C8)
from ableton.clips import ClipPlayer
player = ClipPlayer(track_name="Drums")  # Target track by name
player.play_clip(clip_index=0)  # Initiate clip playback
```

## Development Environment
- macOS 11+
- Python 3.9+
- Visual Studio Code