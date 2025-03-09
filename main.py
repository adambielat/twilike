from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import time
from colorama import init, Fore
import logging
import pandas as pd
import undetected_chromedriver as uc
import os

username = "USERHERE"
password = "PASSHERE"

#  Chrome Options
options = uc.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

#  Logging Options
logging.basicConfig(level=logging.WARNING)
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('webdriver_manager').setLevel(logging.WARNING)
init(autoreset=True)

os.system('cls')
print(Fore.LIGHTCYAN_EX + """
    ┌───────────────────────────────────────────────────────────────────────┐
    │ _________  ___       __   ___  ___       ___  ___  __    _______      │
    │|\___   ___\\\  \     |\  \|\  \|\  \     |\  \|\  \|\  \ |\  ___ \     │
    │\|___ \  \_\ \  \    \ \  \ \  \ \  \    \ \  \ \  \/  /|\ \   __/|    │
    │     \ \  \ \ \  \  __\ \  \ \  \ \  \    \ \  \ \   ___  \ \  \_|/__  │
    │      \ \  \ \ \  \|\__\_\  \ \  \ \  \____\ \  \ \  \\\ \  \ \  \_|\ \ │
    │       \ \__\ \ \____________\ \__\ \_______\ \__\ \__\\\ \__\ \_______\│
    │        \|__|  \|____________|\|__|\|_______|\|__|\|__| \|__|\|_______|│
    └───────────────────────────────────────────────────────────────────────┘
""")

def menu():
    global searchterm
    searchterm = str(input("""  
        Please enter the search term or hashtag.
        ENTER:  """))
    openX()






def openX():
    global searchterm
    driver.get("https://www.x.com/login")
    time.sleep(3)
    usernameInput = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    usernameInput.click()
    usernameInput.send_keys(username)
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
    time.sleep(3)
    passwordInput = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    passwordInput.click()
    passwordInput.send_keys(password)
    time.sleep(3)
    login = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
    time.sleep(3)
    search()

def search():
    bar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
    body = driver.find_element(By.TAG_NAME, 'body')
    bar.click()
    bar.send_keys(searchterm)
    bar.send_keys(Keys.ENTER)
    time.sleep(3)
    latest = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
    likeposts()
  
                
def likeposts():
    os.system('cls')
    print(Fore.LIGHTCYAN_EX + """
    ┌──────────────────────────────────────────────────────────────────────────────────┐
    │ ________  _________  ________  ________  _________  ___  ________   ________     │
    │|\   ____\|\___   ___\\\   __  \|\   __  \|\___   ___\\\  \|\   ___  \|\   ____\    │
    │\ \  \___|\|___ \  \_\ \  \|\  \ \  \|\  \|___ \  \_\ \  \ \  \\\ \  \ \  \___|    │
    │ \ \_____  \   \ \  \ \ \   __  \ \   _  _\   \ \  \ \ \  \ \  \\\ \  \ \  \  ___  │
    │  \|____|\  \   \ \  \ \ \  \ \  \ \  \\\  \|   \ \  \ \ \  \ \  \\\ \  \ \  \|\  \ │
    │    ____\_\  \   \ \__\ \ \__\ \__\ \__\\\ _\    \ \__\ \ \__\ \__\\\ \__\ \_______\│
    │   |\_________\   \|__|  \|__|\|__|\|__|\|__|    \|__|  \|__|\|__| \|__|\|_______|│
    │   \|_________|                                                                   │
    └──────────────────────────────────────────────────────────────────────────────────┘""")
    
    print()
    loop = 1
    actions = ActionChains(driver)
    body = driver.find_element(By.TAG_NAME, 'body')
    time.sleep(3)
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//article'))
            )
            like_buttons = driver.find_elements(By.XPATH, '//button[@data-testid="like"]')
            if not like_buttons:
                print(Fore.LIGHTRED_EX + "  No like buttons found. Scrolling down...")
                driver.execute_script("window.scrollBy(0, 1000);")
                time.sleep(3)
                continue
            for i, like in enumerate(like_buttons):
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", like)
                    time.sleep(1)
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(like))
                    driver.execute_script("arguments[0].click();", like)
                    print(Fore.LIGHTGREEN_EX + "    Liked post")
                    time.sleep(2)  
                except Exception as e:
                    print(Fore.RED + "  Failed to like post. Loading more posts.")
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(3)
        except Exception as e:
            print(Fore.LIGHTRED_EX + "  Blocked by user, skipping post.")
            time.sleep(1)
            blockbutton = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/button').click()
            time.sleep(2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


menu()
