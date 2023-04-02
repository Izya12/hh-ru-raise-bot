from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.webdriver.edge import service
import os
os.system("cls") #clear screen from previous sessions
import time

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument('headless') # that is, run in the command line only, server run prep
# options.add_argument("start-maximized")
my_service=service.Service(r'msedgedriver.exe')
options.page_load_strategy = 'eager' #do not wait for images to load
options.add_experimental_option("detach", True)
options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage') # uses disk instead of RAM, may be slow, use it if You receive "driver Run out of memory" crashed browser message

s = 30 #time to wait for a single component on the page to appear, in seconds; increase it if you get server-side errors «try again later»

driver = webdriver.Edge(service=my_service, options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver,s)
   
username = os.environ.get('LOGIN')
password = os.environ.get('KEY')

login_page = "https://hh.ru/account/login"
resume_stats_page = "https:/hh.ru/applicant/resumes"

def login():
    driver.get(login_page)
    wait.until(EC.element_to_be_clickable((By.NAME, 'login'))).send_keys(username)

    show_more_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='expand-login-by-password']")))
    driver.execute_script('arguments[0].click()', show_more_button)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']"))).send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='account-login-submit']")))
    driver.execute_script('arguments[0].click()', login_button)
    
# def scroll_to_bottom(): 
#     reached_page_end= False
#     last_height = driver.execute_script("return document.body.scrollHeight")
    
#     #expand the skills list:
#     while not reached_page_end:
#         driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#         time.sleep(2)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if last_height == new_height:
#             reached_page_end = True
#         else:
#             last_height = new_height

def resume_raise():
    try:
        raise_button= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='resume-update-button']")))
        action.move_to_element(raise_button).perform()
        time.sleep(3)
        action.click(raise_button).perform() 
    except:
        return 1
           
def main():
    login()
    time.sleep(10)
    driver.get(resume_stats_page)
    time.sleep(10)
    # scroll_to_bottom()
    resume_raise()

    os.system("cls") #clear screen from unnecessary logs since the operation has completed successfully
    print("Your resume is raised in the list on the hh.ru! \n \nSincerely Yours, \nNAKIGOE.ORG\n")
    driver.close()
    driver.quit()
main()
