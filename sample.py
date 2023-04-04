from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


options  = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)

browser.get("https://cyberqgroup.hrhub.ph/Login.aspx")

browser.maximize_window()

input_1=browser.find_element(by=By.ID, value= 'txtUsername')
input_1.send_keys("MKalalo")

input_2=browser.find_element(by=By.ID, value= 'txtPassword')
input_2.send_keys("M@rksprout2")

login=browser.find_element(by=By.NAME, value= 'btnLogIn')
login.send_keys(Keys.RETURN)
try:
    element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "small-image")))
    element.click()

    element2 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//li[@data-bind='click: webBundyLogOut']")))
    element2.click()

    cancel=browser.find_element(by=By.CLASS_NAME, value= 'btn-raw2')
    cancel.send_keys(Keys.RETURN)
except:
    print("nyekok")




# finally:
#     browser.quit()
    # from selenium.webdriver.common.keys import Keys

# PATH = "drivers/chromedriver.exe"
    # element2 = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "//li[@data-bind='click: webBundyLogOut']")))
    # element2.click()

    # element3 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn btn-raw2")))
    # element3.click()
    
# data-bind="click: webBundyLogOut"

# Working
    # input_3=browser.find_element(by=By.PARTIAL_LINK_TEXT, value= 'Show Team Attendance')
    # input_3.send_keys(Keys.RETURN)

# input_1=browser.find_element(by=By.ID, value= 'txtUsername')
# input_1.send_keys("MKalalo")

# input_2=browser.find_element(by=By.ID, value= 'txtPassword')
# input_2.send_keys("M@rksprout2")

# input_2=browser.find_element(by=By.NAME, value= 'btnLogIn')
# input_2.send_keys(Keys.RETURN)







#txtUsername

# WEB SCRAPING

# import requests
# from bs4 import BeautifulSoup
# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
# quotes = soup.find_all("span", class_="text")
# author = soup.find_all("small", class_="author")
# for i in range(0 , len(quotes)):
#         print(quotes[i].text)
#         print(author[i].text, "\n")