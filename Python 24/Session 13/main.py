import pyautogui as pag
import time

time.sleep(1)

# pag.moveTo(120, 879, .5)

pag.click(120, 879)

time.sleep(10)

pag.click(394, 94)
time.sleep(0.5)

pag.write('www.google.com')
time.sleep(0.5)
pag.press('enter')
time.sleep(3)

pag.click(516, 408)
time.sleep(0.5)

pag.write('Python')
time.sleep(0.5)
pag.press('enter')
time.sleep(3)

pag.screenshot('python.png')


print(pag.position())

