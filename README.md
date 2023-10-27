# iTrace-ScreenRecording
OBS Plugin for Screen Recording during an iTrace-Core Tracking session.

To use, ensure that you have Python 3.6 installed on your machine. 3.6 is required, and any other version will not work. Python 3.6 does not need to be added to your PATH, and it can be installed anywhere.

Launch OBS, and select Tools->Scripts. Go to Python Settings, and locate the folder that contains the Python 3.6 installation. If done correctly, you should see "Loaded Python Version: 3.6" message on the window.

To load the plugin, go back to the Scripts tab, and select the `+` button. Then select the iTrace-Recorder.py file.

To use the plugin, ensure iTrace-Core is open. Click on "iTrace-Recorder.py" on the scripts window, and then click the "Connect to Core" button. iTrace-ScreenRecord should now be connected, and you can test it by quickly starting a tracking session. OBS should automatically start and stop a recording.
