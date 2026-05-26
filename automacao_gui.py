import pyautogui as at

at.hotkey ("win","r")
at.write ("mspaint", 0.2)
at.press ("enter")
at.sleep (3)
at.mouseDown (500,500)
at.moveTo(1000,1000)