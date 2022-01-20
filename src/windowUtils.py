import subprocess


def get_linux_bombcrypto_windows(): 
    stdout = (subprocess.Popen("xdotool search --name bombcrypto", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()) 
    windows = stdout.split('\n') 
    return windows

def activate_linux_window(window_id):
    subprocess.Popen(f"xdotool windowactivate {window_id}", shell=True)

def get_linux_window_name(window_id): 
    stdout = (subprocess.Popen(f"xdotool getwindowname {window_id}", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()) 
    return stdout