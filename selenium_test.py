from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")
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