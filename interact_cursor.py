import pyautogui

print(pyautogui.size())

pyautogui.moveTo(300, 100, duration=1.5)

pyautogui.moveRel(500, 0, duration=3)
pyautogui.moveRel(0, 500, duration=3)
pyautogui.moveRel(-500, 0, duration=3)
pyautogui.moveRel(0,-500, duration=3)