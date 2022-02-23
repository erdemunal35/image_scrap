from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

# To run Chrome in headless mode (without any graphical user interface)
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://en.zalando.de/womens-clothing/')

# garments = driver.find_elements_by_class_name("heWLCX")
garments = driver.find_elements_by_xpath("//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ']")
garment_range = len(garments)
for i in range(garment_range):
# get the first garment's images
    garments = driver.find_elements_by_xpath("//a[@class='_LM JT3_zV CKDt_l CKDt_l LyRfpJ']")
    garment_link = garments[i].get_attribute('href')
    print(garment_link)

    driver.get(garment_link)
    imgs = driver.find_elements_by_xpath("//img[@class='_6yVObe u-6V88 ka2E9k uMhVZi FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy']")
    imgs_range = len(imgs)
    for j in range(imgs_range):
        src = imgs[j].get_attribute('src')
        image_name = "image_" + str(i) + "_" + str(j)+".png"
        urllib.request.urlretrieve(src, image_name)
    driver.get('https://en.zalando.de/womens-clothing/')
driver.quit()
