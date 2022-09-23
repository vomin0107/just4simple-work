import pyautogui
import time

jlist = [17]
for j in jlist:
    text = ''
    for i in range(j*20, j*20+20):
        text += 'SF' + str(3910628547000+i) + ' '
    print(text)
    print(j)

    pyautogui.click(1668, 440)
    time.sleep(0.5)

    pyautogui.click(1059, 448)
    time.sleep(0.5)

    pyautogui.typewrite(text)
    time.sleep(0.5)

    pyautogui.click(1727, 440)
    time.sleep(3)

    pyautogui.moveTo(1180, 686)
    time.sleep(8)


# 1668 440, 1727 440, 1180 611, 1408 611