from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotSelectableException, ElementNotVisibleException, MoveTargetOutOfBoundsException, NoSuchElementException
from os import system, name
import random
import warnings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
warnings.filterwarnings("ignore", category=DeprecationWarning) 

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')



recenici=['The best channel on Telegram','Always the latest news','Nema greska','SPAM 1',
'SPAM 2','SPAM 3','SPAM 4','SPAM 5','SPAM 6','wow','Keep up the good job']
#recenici=':🇺🇸:'
#add your path
PATH = "C:\Program Files\Web Driver\chromedriver.exe"




clear()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH)
clear()
broj = input("ENTER NUMBER: ")
print("You entered: " + broj)

act=ActionChains(driver)

    
time.sleep(2)
driver.execute_script('window.open("https://webz.telegram.org");')
driver.switch_to.window(driver.window_handles[0])
driver.close()
driver.switch_to.window(driver.window_handles[0])


def log():
    clear()
    print('log')
    print(broj)

#check the url if it's z version
def proveriURL():
    if driver.current_url!='https://webz.telegram.org':
        driver.get('https://webz.telegram.org')

# log in account
def najava():
    neEPRVPAT=0
    time.sleep(1)
    while True:
        kopce1=driver.find_elements_by_xpath('//*[@id="auth-qr-form"]/div/button')
        if len(kopce1):
            time.sleep(1)
            break

    kopce1=driver.find_element_by_xpath('//*[@id="auth-qr-form"]/div/button')
    act.move_to_element(kopce1).click().perform()
    time.sleep(1)
    while True:
        poleBroj=driver.find_elements_by_xpath('//*[@id="sign-in-phone-number"]')
        if len(poleBroj):
            time.sleep(1)
            break
    
    poleBroj=driver.find_element_by_xpath('//*[@id="sign-in-phone-number"]')
    poleBroj.clear()

    act.move_to_element(poleBroj).click().send_keys(broj).perform()
    time.sleep(1)
    while True:
        kopce2=driver.find_elements_by_xpath('//*[@id="auth-phone-number-form"]/div/form/button[1]')
        if len(kopce2):
            time.sleep(1)
            break

    kopce2=driver.find_element_by_xpath('//*[@id="auth-phone-number-form"]/div/form/button[1]')
    act.move_to_element(kopce2).click().perform()
    time.sleep(2)

# enter code
def vnesiKod():
    time.sleep(2)
    while True:
        mesto=driver.find_elements_by_xpath('//*[@id="sign-in-code"]')
        if len(mesto):
            break
    kod = input("ENTER CODE: ")
    print("You entered: " + kod)
    mesto=driver.find_element_by_xpath('//*[@id="sign-in-code"]')
    mesto.clear()
    act.move_to_element(mesto).click().send_keys(kod).perform()
    time.sleep(8)

najava()
vnesiKod()

def klikNaChannelFolder():
    #print('kopce chanell')
    kopceZaChanell='//*[@id="LeftColumn-main"]/div[2]/div/div/div[1]/button[3]'
    driver.find_element_by_xpath(kopceZaChanell).click()
    time.sleep(2)
    #print('kopce chanell  gotovo')


def checkFolder():
    time.sleep(0.5)
    sureCheck=driver.find_element_by_xpath('//*[@id="LeftColumn-main"]/div[2]/div/div/div[1]/button[3]')
    nig=sureCheck.get_attribute("class")
    if nig!='Tab active':
        klikNaChannelFolder()
    print(nig)


def najdiNovo():
    while True:
        #clear()
        checkFolder()
        if najdiListice()==0:
            continue
        listice=driver.find_element_by_xpath('//*[@id="LeftColumn-main"]/div[2]/div/div/div[2]/div[2]')
        novo=listice.find_elements_by_class_name('Badge')
        #print(len(novo))
        print('----------')
        popUP()
       

        if novo:
            return komentiraj(novo)

def najdiListice():
    listice=driver.find_elements_by_xpath('//*[@id="LeftColumn-main"]/div[2]/div/div/div[2]/div[2]')
    if len(listice):
        return 1
    else:
        return 0

def kopceDole():
    pass
    selected=driver.find_elements_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[3]/div/button')
    if len(selected):
        nemaGreska=driver.find_element_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[3]/div/button')
        act.move_to_element(nemaGreska).click().perform()
        return 1
    else:
        pass


def komentiraj(novo):
    for i in range(0,len(novo)):
        #recheck()
        print('KOMENTIRAJ PRED KLIK')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((novo[i])))
        act.move_to_element_with_offset(novo[i], -100, 0).click().perform()
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="MiddleColumn"]/div[3]/div[2]/div/div[1]/div')))
        if kopceDole() == 0:
            act.move_to_element_with_offset(novo[i], -100, 0).click().perform()
        
        if findListaPostovi()==0:
            continue
        else:
            listaPostovi=driver.find_element_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[2]/div/div[1]/div')  #listaodkanalpost

        if findPost(listaPostovi)==0:
            continue        
        else:
            post=listaPostovi.find_element_by_class_name('last-in-list')

        if findKomentar(post)==0:
            continue
        
        if klikniKopce()==0:
            continue
    najdiNovo()

def findListaPostovi():
    print('LISTAPOSTOVI START')
    if popUP()==0:
        print('KLIKNIKOPCE RETURN 0 OD POPUP')
        return 0
    time.sleep(0.2)
    try: 
        test=driver.find_elements_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[2]/div/div[1]/div')
    except StaleElementReferenceException:
        return 0
    test=driver.find_elements_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[2]/div/div[1]/div')
    if len(test):
        print('LISTAPOSTOVI RETURN 1')
        return 1
    else:
        print('LISTAPOSTOVI RETURN 0')
        return 0



def findPost(listaPostovi):
    print('FIND POST START')
    if popUP()==0:
        print('KLIKNIKOPCE RETURN 0 OD POPUP')
        return 0
    time.sleep(0.2)
    post=listaPostovi.find_elements_by_class_name('last-in-list')
    if len(post):
        print('FIND POST RETURN 1')
        return 1
    else:
        print('FIND POST RETURN 0')
        return 0

        
def findKomentar(post):
    print('FIND KOMENTAR START')
    time.sleep(0.5)
    if popUP()==0:
        print('FINDKOMENTAR RETURN 0 OD POPUP')
        return 0
    elem=post.find_elements_by_class_name('CommentButton')

    if len(elem)>0:

        post.find_element_by_class_name('CommentButton').click()
        time.sleep(0.5)
        print('FIND KOMENTAR 1')
        return 1

    else:

        print('FIND KOMENTAR 0')
        return 0


def sendMessage():
    if popUP()==0:
        print('KLIKNIKOPCE RETURN 0 OD POPUP')
        return 0


    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Send Message"]'))
    )
    except TimeoutException:
        print("TIMEOUT RETURN 0")
        return 0
    

    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//button[@title="Send Message"]')))

    lele=driver.find_elements_by_xpath('//button[@title="Send Message"]')
    

    if len(lele)>0:
        time.sleep(0.3)

        if popUP()==0:
            
            return 0
        
        lord=driver.find_element_by_xpath('//button[@title="Send Message"]')
        time.sleep(0.2)
        act.move_to_element(lord).click().perform()

        time.sleep(0.8)

        driver.back()
        driver.back()

        return 1
    else:

        return 0



def klikniKopce():
    time.sleep(0.5)
    

        
    if popUP()==0:
        return 0
    random_index = random.randint(0,len(recenici)-1)
    act.send_keys(recenici[random_index]).perform()
        #act.send_keys(recenici).perform()
    time.sleep(0.2)

    if sendMessage():
        return 1
    else:
        return 0
        #print('klikniKopce finish')
    

def popUP():
    #print("popup time")
    print('POPUP START')
    elem=driver.find_elements_by_xpath('//button[contains(text(),"OK")]')
    if len(elem)>0:
        print('POPUP RETURN 0')
        driver.back()
        driver.back()
        driver.back()
        return 0
    else:
        return 1


def main():
    try:
        log()
        proveriURL()
        klikNaChannelFolder()
        najdiNovo()

    except TimeoutException:
        main()
    except StaleElementReferenceException:
        main()
    except MoveTargetOutOfBoundsException:
        main()
    except ElementNotInteractableException:
        main()
    except ElementClickInterceptedException:
        main()
    except ElementNotVisibleException:
        main()
    except ElementNotSelectableException:
        main()
    except NoSuchElementException:
        main()


if __name__ == "__main__":
    main()
