from selenium import webdriver
from time import sleep

def getNonRepeatList(data):
    new_data = []
    for i in range(len(data)):
        if data[i] not in new_data:
            new_data.append(data[i])
    return new_data

def run():
    with open('./easy.txt',encoding='utf-8') as f:
        easy = []
        for s in f.readlines():
            easy.append(s.replace('\n',''))
    easy = getNonRepeatList(easy)
    with open('./medium.txt',encoding='utf-8') as f:
        medium = []
        for s in f.readlines():
            medium.append(s.replace('\n',''))
    medium = getNonRepeatList(medium)
    with open('./hard.txt',encoding='utf-8') as f:
        hard = []
        for s in f.readlines():
            hard.append(s.replace('\n',''))
    hard = getNonRepeatList(hard)
    if len(easy)==0 and len(medium)==0 and len(hard)==0:
        print('没有词语可以导入哦。')
        exit()
    print("已导入简单词{}个，中等词{}个，困难词{}个。".format(len(easy),len(medium),len(hard)))

    print("开始导入简单词")
    sleep(3)

    #导入简单
    driver.find_element_by_xpath("//label[@for='easy']").click()
    for s in easy:
        input_word(s)
    print("开始导入中等词")
    sleep(3)

    #导入中等
    driver.find_element_by_xpath("//label[@for='medium']").click()
    for s in medium:
        input_word(s)
    print("开始导入困难词")
    sleep(3)

    #导入困难
    driver.find_element_by_xpath("//label[@for='hard']").click()
    for s in hard:
        input_word(s)
    print("导入完成")
    sleep(3)

def input_word(word):
    print("导入{}".format(word))
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
    print("cookie添加完成。")
    driver.refresh()

if __name__ == "__main__":
    print("正在打开FireFox.")
    driver = webdriver.Firefox()
    driver.get("https://gartic.io/")
    while True:
        r = input("请输入指令：")
        if r == 'run':
            run()
        if r == 'cookie':
            add_cookie()
        if r == 'exit':
            break
    driver.close()

