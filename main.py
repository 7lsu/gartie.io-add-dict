from selenium import webdriver
from time import sleep
import re

def getNonRepeatList(data):
    new_data = []
    for i in range(len(data)):
        if data[i] not in new_data:
            new_data.append(data[i])
    return new_data

def run():
    difficulty = {'easy':[],'medium':[],'hard':[]}
    for diff in difficulty:
        with open('./{}.txt'.format(diff),encoding='utf-8') as f:
            for s in f.readlines():
                data = s.replace('\n','').replace('！','!').lower()
                difficulty[diff].append(re.sub('[^\w|\u4e00-\u9fa5|\s|!|]+', '', data))
        array = getNonRepeatList(difficulty[diff])
        if (len(array) > 0):
            print("[*] 导入{}词{}个。".format(diff,len(array)))
            sleep(1)
            driver.find_element_by_xpath("//label[@for='{}']".format(diff)).click()
            for word in array:
                input_word(word)
    print("[*] 导入完成")

def input_word(word):
    print("[*] 导入{}".format(word))
    try:
        driver.find_element_by_xpath("//p[@class='legend error']")
    except:
        driver.find_element_by_xpath("//input[@maxlength='30']").send_keys(word)
        driver.find_element_by_xpath("//label[@class='btAdd']").click()
    else:
        driver.find_element_by_xpath("//input[@maxlength='30']").clear()

# //input[@maxlength='30'] 输入框
# //p[@class='legend error'] 重复提示出现
# //label[@class='btAdd'] 添加按钮
# //label[@for='easy'] 简单按钮
# //label[@for='medium'] 中等按钮
# //label[@for='hard'] 困难按钮

def add_cookie():
    driver.delete_cookie('garticio')
    cookie = {
        'garticio':'s%3Ac056d63f-559d-445b-821d-cfb1f9a99a8a.mIhfMgr%2BazPO02qMv7elZpcm11O49jd8ADHrccl9Eqw',
    }
    for name,value in cookie.items():
        cookie_dict = {
            'name':name,
            'value':value,
            'expires':'',
            'path':'/',
            'httpOnly':False,
            'HostOnly':False,
            'Secure':False
        }
        driver.add_cookie(cookie_dict)
    print("[*] cookie添加完成。")
    driver.refresh()

if __name__ == "__main__":
    print("[*] 正在打开FireFoxWebDriver...")
    driver = webdriver.Firefox()
    driver.get("https://gartic.io/")
    while True:
        r = input("[-] 请输入指令：")
        if r == 'run':
            run()
        if r == 'cookie':
            add_cookie()
        if r == 'exit':
            break
    driver.close()

