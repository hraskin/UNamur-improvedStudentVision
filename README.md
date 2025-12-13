# ImprovedBoardVision

An accessible project for students with visual impairments. ImprovedBoardVision captures the blackboard or whiteboard and retransmits it to the student after processing it through a pipeline of visual enhancement steps, such as edge detection and luminosity and contrast enhancement.

## Setup Instructions to enable video flow from android device

### Prerequisites
- Android device in developer mode and USB debugging enabled
- DroidCam app installed on the android device
- Homebrew installed on MacOS device

### Steps

1. Install adb on your MacOS device.
```bash
brew install android-platform-tools
```

2. Connect your android device to your MacOS device via USB.

3. Verify that your device is connected.
```bash
adb devices
```

4. Create a reverse port forwarding from your MacOS device to your android device.
```bash
adb reverse tcp:4747 tcp:4747
```

5. Enjoy video streaming from your android device to your MacOS device using DroidCam app.

## Run the project

In an environment python

```bash
python main.py
```
