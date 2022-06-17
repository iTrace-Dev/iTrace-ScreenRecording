
import obspython as obs
import asyncio
import socket
import threading
import time




HOST = "127.0.0.1"
PORT = 8008

TRACKING = False

#profiles = obs.obs_frontend_get_current_profile_path()
#print(profiles)

#print(obs.obs_output_t)

def connectToCore():
    global TRACKING
    print("Connecting to core...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        #output = obs.obs_output_create("itrace","iTrace Record",
        while TRACKING:
            data = s.recv(1024)
            if not data: break
            if data == b"session_end\n":
                print("Got end")
                obs.obs_frontend_recording_stop()
                break
            elif data.startswith(b"session_start"):
                print("Got start!",obs.obs_frontend_get_current_record_output_path())
                obs.obs_frontend_recording_start()
                
            #print(data)    
    print("Loop stopped, disconnected!")
    TRACKING = False


def script_load(settings):
    print("Loading script")


def connectButton(*args):
    global TRACKING
    if TRACKING:
        print("Already connected to Core")
        return
    TRACKING = True

    x = threading.Thread(target=connectToCore)
    x.start()
    print("Pressed!")


def script_properties():
    properties = obs.obs_properties_create()
    con_button = obs.obs_properties_add_button(properties, "connect_button","Connect to Core",connectButton)

    return properties




    
