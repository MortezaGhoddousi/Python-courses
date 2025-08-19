import pyautogui as pag
import time

time.sleep(3)

pag.click(1804, 26, 1)
time.sleep(0.5)

pag.click(36, 338, 1)
time.sleep(0.5)

pag.hotkey('alt', 'space')
time.sleep(0.5)

pag.press('x')
time.sleep(0.5)

pag.click(741, 375, 1)
time.sleep(0.5)

pag.typewrite('Fatemeh Jaavdani')
pag.press('enter')
time.sleep(1)

pag.screenshot('FatemehJaavdani.jpg')

x = 5
print(f"x is: {x}")


