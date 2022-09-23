import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'http://bl-h5-as.robotbona.com/'
idpw = 'danhui1639'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

def sign_in():
    id_input = driver.find_element_by_xpath('//*[@id="account_softbona_com"]')
    pw_input = driver.find_element_by_xpath('//*[@id="pwd"]')
    id_input.send_keys(idpw)
    pw_input.send_keys(idpw)
    pw_input.send_keys(Keys.RETURN)
    # elem = driver.find_element_by_class_name("particulars-btn")
    # print(elem)

def click_device_status():
    device_status_btn = driver.find_element_by_xpath('/html/body/div[1]/ul/li[4]/ul/li[3]/a')
    device_status_btn.click()

def click_user():
    for user_btn_index in range(15):
        user_btns = driver.find_elements_by_xpath('//*[@class="particulars-btn"]')
        # print(len(user_btns))
        user_btns[user_btn_index].click()
        time.sleep(1.5)
        cur_page_btn = driver.find_element_by_xpath('//*[@id="pagination"]/ul')
        pages_btn = cur_page_btn.find_elements_by_class_name('pagenum')
        # print(pages_btn)
        # print(len(pages_btn))
        max_page = pages_btn[len(pages_btn)-1]
        print(max_page.text)
        driver.back()
        time.sleep(1.5)

def save_cleaning_time():
    print('signin success')


if __name__ == '__main__':
    sign_in()
    time.sleep(3)
    click_device_status()
    time.sleep(2)
    click_user()
    save_cleaning_time()
