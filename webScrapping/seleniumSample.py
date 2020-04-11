from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\geckodriver.exe')
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
elem.click()

#elems = browser.find_elements_by_css_selector('p')
#searchElem = browser.find_elements_by_css_selector('.search-field')
#searchElem.send_keys('zophie')
#searchElem.submit()

#browser.forward()
#browser.refresh()
#browser.quit()
