from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
browser = webdriver.Firefox()





urlList = ["https://free-proxy-list.net/", "https://www.proxyscrape.com/free-proxy-list",
           "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers/", "https://openproxy.space/list"]
# We will setup a List of urls of proxylistsWebsites go to each of them then fire a specific method for that site extract the urls from it then put them in a big list or
# Dicionarie then check each one them if they are alive then add them to the final list


proxyList = {
    "ip address :": "",
    "Port   ": "",
    "Code   ": "",
    "Country   ": "",
}
unknownType = []
proxy_http = []
socks5 = []
socks4 = []


def free_proxy_list():
    global unknownType
    browser.get(urlList[0])
    clipbtn = browser.find_element(By.CLASS_NAME, "fa-clipboard")
    clipbtn.click()

    proxylist_frm = browser.find_element(By.CLASS_NAME, 'form-control')
    unknownType = proxylist_frm.text.splitlines()
def proxy_scrap():
    global proxy_http
    global socks4
    global socks5
    browser.get(urlList[1])
    sleep(5)
    http_btn = browser.find_element(By.XPATH,'//*[@id="downloadhttp"]')
    http_btn.click()
    mail_text= browser.find_element(By.ID,"email_box")
    select_case = browser.find_element(By.XPATH,'//*[@id="usecase_box"]')
    mail_text.send_keys("jaja@mail.com")
    select_case.click()
    select_case.click()
    select_case.click()
    select_case.click()
    dw_btn = browser.find_element(By.ID,"submit_fpl_download")
    dw_btn.click()
def openproxy():
    global proxy_http
    global socks4
    global socks5
    browser.get("https://openproxy.space/list/http")
    sleep(3)
    http_proxis = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/section[4]/textarea')
    proxy_http = http_proxis.text.splitlines()
    browser.get("https://openproxy.space/list/socks4")
    sleep(3)
    socks4_prox = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/section[4]/textarea')
    socks4 = socks4_prox.text.splitlines()
    browser.get("https://openproxy.space/list/socks5")
    sleep(3)
    socks5_prox = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/section[4]/textarea')
    socks5 = socks5_prox.text.splitlines()


#free_proxy_list()
#proxy_scrap()
openproxy()
#print(unknownType)
#del unknownType[0]
#del unknownType[0]
#del unknownType[0]






print(unknownType)
print(proxy_http)
print(socks4)
print(socks5)
