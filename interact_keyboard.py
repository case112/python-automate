import pyautogui


pyautogui.moveTo(800, 300)
pyautogui.click()

pyautogui.typewrite(['#','a', 'b', 'left', 'left', 'X', 'Y'], interval=.2)