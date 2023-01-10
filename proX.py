from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import threading
browser = webdriver.Firefox()




urlList = ["https://free-proxy-list.net/", "https://www.proxyscrape.com/free-proxy-list",
           "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers/", "https://openproxy.space/list"]
# We will setup a List of urls of proxylistsWebsites go to each of them then fire a specific method for that site extract the urls from it then put them in a big list or
# Dicionarie then check each one them if they are alive then add them to the final list


timeot = 15
proxy_http = []
socks5 = []
socks4 = []
proxiesCount=0




# Methods for each Website
def free_proxy_list():
    global proxy_http
    browser.get(urlList[0])
    clipbtn = browser.find_element(By.CLASS_NAME, "fa-clipboard")
    clipbtn.click()

    proxylist_frm = browser.find_element(By.CLASS_NAME, 'form-control')
    proxy_http = proxylist_frm.text.splitlines()
    del proxy_http[0]
    del proxy_http[0]
    del proxy_http[0]
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


# This will start all of the methods one by one
def HarvestProxies():
    free_proxy_list()

    #openproxy()

def make_http_request(proxy):
    try:
        global proxy_http
        response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy} , timeout=timeot)
        print(proxy , " is valid")

    except:
        print(proxy ," is invalid")
        proxy_http.remove(proxy)

def checkProxies():
    threads = []
    for p in proxy_http:
        thread = threading.Thread(target=make_http_request, args=(p,) )
        thread.start()
        threads.append(thread)


    for thread in threads:
        thread.join()


def printlogo():
    print("        ______                                                          ")
    print("  _____|\     \___________            ____            _____       _____ ")
    print(" /     / |     \          \       ____\_  \__         \    \     /    / ")
    print("|      |/     /|\    /\    \     /     /     \         \    |   |    /  ")
    print("|      |\____/ | |   \_\    |   /     /\      |         \    \ /    /   ")
    print("|\     \    | /  |      ___/   |     |  |     |          \    |    /    ")
    print("| \     \___|/   |      \  ____|     |  |     |          /    |    \    ")
    print("|  \     \      /     /\ \/    |     | /     /|         /    /|\    \   ")
    print(" \  \_____\    /_____/ |\______|\     \_____/ |        |____|/ \|____|  ")
    print("  \ |     |    |     | | |     | \_____\   | /         |    |   |    |  ")
    print("   \|_____|    |_____|/ \|_____|\ |    |___|/          |____|   |____|  ")
    print("                                 \|____|                                ")
    print("                                                                    1.0")






while True:
    os.system("clear")
    printlogo()
    proxiesCount=len(proxy_http)+len(socks4)+len(socks5)
    print("----------------------------------------------")
    print("HTTP : ", len(proxy_http))
    print("Socks 4  : " ,len(socks4))
    print("Socks 5 : " ,len(socks5))
    print("All proxies : " ,proxiesCount)
    print("----------------------------------------------")
    print("1 - Check proxies")
    print("2 - Get yourself some proxies")
    print("3 - Save to file")
    print("4 - Close script")
    option = input(' > ')
    match option:
        case "1":
            if(proxiesCount!=0):
                timeot = input("Max timeout in seconds (default 10 sec) : ")
                checkProxies()
        case "2":
            HarvestProxies()
        case "4":
            break