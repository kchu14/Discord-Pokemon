import pyautogui
import time


time.sleep(5)
start = time.time()
point = pyautogui.position()
print(point)


count = 0
# time.sleep()
while True:
    pyautogui.click(x=point.x, y=point.y, button="left")
    pyautogui.typewrite(";pokemon\n")
    count += 1
    print(f"pokemon {count}")
    time.sleep(10810)
