from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    # Source: https://stackoverflow.com/questions/44597107/webdrivererror-error-chrome-failed-to-start-exited-abnormally
    # Author: Raony Benjamim
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('no-sandbox')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("http://162.246.157.124:8000/")

    time.sleep(5)

    name = driver.find_element_by_id("name")
    about = driver.find_element_by_id("about")
    skills = driver.find_element_by_id("skills")
    education = driver.find_element_by_id("education")
    work = driver.find_element_by_id("work")
    contact = driver.find_element_by_id("contact")

    assert name != None
    assert about != None
    assert skills != None
    assert education != None
    assert work != None
    assert contact != None

    driver.quit()
