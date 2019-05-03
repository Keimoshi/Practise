# encoding: utf-8
import time
from selenium import webdriver

def login(username , password):
    url = 'https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/auth?client_id=customer-portal&redirect_uri=https%3A%2F%2Faccess.redhat.com%2Fwebassets%2Favalon%2Fj%2Fincludes%2Fsession%2Fscribe%2F%3FredirectTo%3Dhttps%253A%252F%252Faccess.redhat.com&state=2cab7891-d192-4cf2-89a7-3e4d88b710bd&nonce=e6ac5367-aabe-422a-b58f-8e4ef9f3ccbf&response_mode=fragment&response_type=code&scope=openid'
    driver = webdriver.Firefox()
    driver.get(url)
    # print driver.title
    name_input = driver.find_element_by_id('username')  # 找到用户名的框框
    pass_input = driver.find_element_by_id('password')  # 找到输入密码的框框
    login_button = driver.find_element_by_id('_eventId_submit')  # 找到登录按钮

    name_input.clear()
    name_input.send_keys(username)  # 填写用户名
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    time.sleep(0.2)
    login_button.click()            # 点击登录

    time.sleep(0.2)
    print driver.get_cookies()

    time.sleep(2)
    print driver.title

    driver.close()

if __name__ == "__main__":
    user = "NkingWu"
    pw = "Gtja.8888!"
    login(user, pw)