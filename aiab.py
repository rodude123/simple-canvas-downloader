from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

##################################################################
## Creator:                                                     ##
## rodude123                                                    ##
## https://github.com/rodude123                                 ##
## Usage:                                                       ##
## Download selenium using pip                                  ##
## add chromedriver to the local directory of where the file is ##
## set download directory in the variable below                 ##
## set sussex canvas email and password in variable below       ##
##################################################################

chromedriver = "./chromedriver"
downloadDir = ""
email = ""
pwd = ""

chromeOptions = Options()

# this is the preference we're passing
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': downloadDir}}
driver.execute("send_command", params)

def exists(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver.get("https://canvas.sussex.ac.uk/courses/8727/modules")

driver.find_element_by_xpath('//*[@id="userNameInput"]').send_keys(email)

driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(pwd)

driver.find_element_by_xpath('//*[@id="submitButton"]').click()

# driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[3]/div[1]/div/div/div[3]/div/div/div/div[13]/div[1]/a').click()

for i in range(6, 17):
    print(i)
    sleep(2)
    if exists('/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div['+str(i)+']/div[2]/ul/li[2]/div/div[1]/div[1]/span/a'):
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div['+str(i)+']/div[2]/ul/li[2]/div/div[1]/div[1]/span/a').click()
                break
            except (ElementClickInterceptedException, NoSuchElementException) as e:
                driver.refresh()
    else:
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[3]/div[2]/div['+str(i)+']/div[2]/ul/li/div/div[1]/div[1]/span/a').click()
                break
            except (ElementClickInterceptedException, NoSuchElementException) as e:
                driver.refresh()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/span/a').click()
    sleep(2)
    driver.execute_script("window.history.go(-1)")
driver.quit()