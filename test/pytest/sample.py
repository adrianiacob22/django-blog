from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

# browser = webdriver.Chrome('/home/adrian/opt/chromedriver/chromedriver')
# creez o functie care asteapta sa se incarce pagina si lasa mai mult timp pentru a observa actiunile
def waitLoadPage():
    WebDriverWait(browser, 3).until(EC.url_changes(current_url))
    time.sleep(2)

browser = webdriver.Firefox()
browser.get('http://myapp.local.net:32080/')


# Fac un refresh de pagina sa ma asigur ca aceasta s-a incarcat corect
time.sleep(2)
browser.refresh()

# browser.find_element_by_link_text('Admin Login')
adminlogin = browser.find_element_by_xpath('/html/body/div/a')
# Dau click pe butonul de login
adminlogin.click()
# Stochez in variabile campurile username si password
username = browser.find_element_by_id('id_username')
password = browser.find_element_by_id('id_password')

# Introduc utilizator si parola, apoi apas enter
username.send_keys('testuser')
password.send_keys('us3rpass')
password.send_keys(Keys.ENTER)


# Salvez url-ul paginii
current_url = browser.current_url

# Astept sa se incarce noua pagina
waitLoadPage()

# Dau click pe posts pentru a crea o postare in aplicatia Posts
postsapp = browser.find_element_by_link_text('Posts')
# postsapp = browser.find_elements_by_xpath("//href[contains('posts')]")
postsapp.click()

# Astept sa se incarce noua pagina
waitLoadPage()
# Dau click pe add pentru a adauga o postare noua
addpost = browser.find_element_by_xpath("//*[@class='addlink']")
addpost.click()
# Astept sa se incarce noua pagina
waitLoadPage()

#Adaug o postare noua
titlu = browser.find_element_by_id('id_title')
body = browser.find_element_by_id('id_body')

titlu.send_keys('titlu de test')
body.send_keys('adaug o postare noua pentru test')
# salvez postarea
element = browser.find_element_by_name('_continue').click()
ActionChains(browser).click(element).perform()
# sterg postarea
browser.find_element_by_xpath("//*[@class='deletelink']").click()

waitLoadPage()

browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[2]').click()

waitLoadPage()

# apas log out
browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()

waitLoadPage()
# inchid ferastra browserului
browser.close()
