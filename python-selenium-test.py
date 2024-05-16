import time, random
import chromedriver_autoinstaller
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install() 

website = "https://github.com"

#chrome_options = Options()
#driver = webdriver.Chrome(options=chrome_options)


#options = webdriver.ChromeOptions()
options = Options()
#options.add_argument('--headless')
options.headless = True
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.get(website)

try:
    driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a").click()
    current_url = driver.current_url
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    #time.sleep(random.randint(3, 6))
    driver.save_screenshot('website.png')
    driver.quit()
except NoSuchElementException:
    pass
