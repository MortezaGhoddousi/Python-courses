import pyautogui as pag
from time import sleep

sleep(2)

pag.hotkey('ctrl', 'shift', 'i')
sleep(1)
pag.typewrite("window.location = 'https://www.google.com';");
pag.press('enter')
sleep(1)

pag.typewrite("var inp = document.querySelector('.gLFyf');");
pag.press('enter')
sleep(1)

pag.typewrite("inp.value = 'MortezaGhoddousi';");
pag.press('enter')
sleep(1)



# pag.click(397, 1004)
# sleep(1)

# pag.click(157, 46)
# sleep(.2)

# pag.typewrite('www.google.com')

# pag.press('enter')
# sleep(1)

# pag.click(434, 484)
# sleep(.2)

# pag.typewrite('mortezaghoddousi')
# pag.press('enter')
# sleep(2)

# pag.screenshot('morteza.png')

# print(pag.position())