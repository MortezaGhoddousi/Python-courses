import pyautogui
import time

def findImage(image_path):
    timeout = 10
    start_time = time.time()
    found = None

    while time.time() - start_time < timeout:
        found = pyautogui.locateOnScreen(image_path, confidence=0.7, grayscale=True)   
        if found:
            center = pyautogui.center(found)
            return center
        else:
            print("Image not found, retrying...")
            time.sleep(0.5)
    if not found:
        return "Failed to find the image on the screen."


image_path = 'googleLogo.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(0.5)
pyautogui.write('github.com')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)

image_path = 'searchIcon.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(0.5)
pyautogui.write('MortezaGhoddousi')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(4)

image_path = 'users.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(0.5)

image_path = 'name.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(2)

image_path = 'repo.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(2)

image_path = 'python.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(2)

image_path = 'codeIcon.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(2)

image_path = 'download.png'

center = findImage(image_path)
pyautogui.click(center)
time.sleep(2)
