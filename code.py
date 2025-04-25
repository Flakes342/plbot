from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pywhatkit

usernameStr = ''
passwordStr = ''

browser = webdriver.Chrome()
browser.get(('https://ocs.iitd.ac.in/portal/login'))

# fill in username and hit the next button
username = browser.find_element("id","mat-input-0")
username.send_keys(usernameStr)
username.submit()

# nextButton.click()
password = browser.find_element("id", "mat-input-1")
password.send_keys(passwordStr)

import time
time.sleep(7) 
# well = browser.find_element("xpath", "/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-student/mat-card/div[1]/h1")

comp = '1 – 7 of 7'
c=0
while True :
    appli = browser.find_element('xpath','/html/body/app-root/mat-sidenav-container/mat-sidenav/div/div/app-sidenav/mat-list[2]/mat-list-item[3]/div')
    appli.click()
    listt = browser.find_element('xpath','/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-student-applications/div/mat-form-field[2]/div/div[1]/div/mat-select/div/div[1]/span/span')
    listt.click()
    applied = browser.find_element('xpath','/html/body/div[3]/div[2]/div/div/div/mat-option[1]/span')
    applied.click()
    time.sleep(2)
    napplied = browser.find_element('xpath','/html/body/div[3]/div[2]/div/div/div/mat-option[2]/span')
    napplied.click()

    comp2 = (browser.find_element('xpath', '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/app-student-applications/mat-card/mat-card-content/mat-paginator/div/div/div[2]/div')).text
    if comp2 == comp:
        if c%5 == 0:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            pywhatkit.sendwhatmsg_instantly('+919995772400', 'Lol nothing new - _Beep boop. I am a bot, and this action was performed automatically_',10)        
        c += 1
        time.sleep(200)
        browser.refresh()
        continue
    else:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        pywhatkit.sendwhatmsg_instantly('+918307210141', 'New Shortlist !! - _Beep boop. I am a bot, and this action was performed automatically_',10)
        pywhatkit.sendwhatmsg_instantly('+919995772400', 'New Shortlist !! - _Beep boop. I am a bot, and this action was performed automatically_',10)
        comp = comp2




# im=ImageGrab.grab(bbox=(530,600,650,700))
# im.show()

# # # to file
# im.save('im.png')
# # signInButton = browser.find_element_by_id('Login')
# # signInButton.click()

# from PIL import Image
# import pytesseract

# im = Image.open("C:/Users/DELL/OneDrive/Desktop/EQAWO.png")
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(im)

# print(text)
