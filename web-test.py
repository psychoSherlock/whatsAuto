from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

prof = "/home/white-devil/.mozilla/firefox/qelozt29.selenium"


fp = webdriver.FirefoxProfile(prof)

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)



browser.get('https://web.whatsapp.com')
print("Opened.....")

#/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1]/div/span
#/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div/div/span
# /html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[1] 3
while True:
    command = input('>>')
    try:
        test = browser.find_element_by_xpath(command)
        print(test.text)
    except Exception as e:
        print(e)