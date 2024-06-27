from webdriver_manager.chrome import ChromeDriverManager 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
browser.implicitly_wait(5)
browser.get("https://wikipedia.org/")

# Add tests here