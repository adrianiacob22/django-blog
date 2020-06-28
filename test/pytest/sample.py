from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import pytest
import allure

text_titlu = "Titlu pentru testare"
text_body = "Introduc un text pentru testarea campului body"
user = "testuser"
parola = "us3rpass"
user1 = "invalid"
parola1 = "invalid"
app_url = 'http://myapp.local.net:32080/'
browser = webdriver.Firefox()
# wait = WebDriverWait(driver, 10)

@pytest.fixture()
def testSetup():
    browser.implicitly_wait(1)
    yield
    browser.quit()

@allure.description("Validez ca login functioneaza cu credentiale valide")
@allure.severity(severity_level="CRITICAL")
def testLogin(testSetup):
    browser.get(app_url)
    browser.implicitly_wait(3)
    # Fac un refresh de pagina sa ma asigur ca aceasta s-a incarcat corect
    browser.refresh()
    # Dau click pe butonul de login
    browser.find_element_by_xpath('/html/body/div/a').click()
    # Introduc username si password apoi apas Log in
    enterUsername(user)
    enterPassword(parola)
    time.sleep(2)
    browser.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click
    browser.implicitly_wait(3)
    assert "admin" in browser.current_url

@allure.description("Validez ca login nu functioneaza cu credentiale invalide")
@allure.severity(severity_level="NORMAL")
def testInvalidLogin(testSetup):
    browser.get(app_url)
    browser.implicitly_wait(3)
    # Fac un refresh de pagina sa ma asigur ca aceasta s-a incarcat corect
    browser.refresh()
    # Dau click pe butonul de login
    browser.find_element_by_xpath('/html/body/div/a').click()
    # Introduc username si password
    enterUsername(user1)
    enterPassword(parola1)
    # Introduc utilizator si parola, apoi dau click pe login
    browser.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/input').click
    time.sleep(2)
    # browser.implicitly_wait(10)
    try:
        assert "next=" in browser.current_url
    finally:
        if(AssertionError):
            allure.attach(browser.get_screenshot_as_png(), name="Invalid_Credentials", attachment_type=allure.attachment_type.PNG)

@allure.step("Introdu numele de utilizator {0}")
def enterUsername(username):
    browser.find_element_by_id('id_username').send_keys(username)

@allure.step("Introdu parola {0}")
def enterPassword(password):
    browser.find_element_by_id('id_password').send_keys(password)


# def testPost():
#     browser.get(app_url)
#     browser.implicitly_wait(3)
#     # Dau click pe butonul de login
#     browser.find_element_by_xpath('/html/body/div/a').click()
#     # Stochez in variabile campurile username si password
#     username = browser.find_element_by_id('id_username')
#     password = browser.find_element_by_id('id_password')
#     # Introduc utilizator si parola, apoi apas enter
#     username.send_keys(user)
#     password.send_keys(parola)
#     password.send_keys(Keys.ENTER)
#     browser.implicitly_wait(3)
#     # Dau click pe posts pentru a crea o postare in aplicatia Posts
#     browser.find_element_by_link_text('Posts').click()
#     # Astept sa se incarce noua pagina
#     browser.implicitly_wait(2)
#     # Dau click pe add pentru a adauga o postare noua
#     browser.find_element_by_xpath("//*[@class='addlink']").click()
#     # Astept sa se incarce noua pagina
#     browser.implicitly_wait(2)
#     #Adaug o postare noua
#     titlu = browser.find_element_by_id('id_title')
#     body = browser.find_element_by_id('id_body')
#     titlu.send_keys(text_titlu)
#     body.send_keys(text_body)
#     # salvez postarea
#     browser.find_element_by_name('_continue').click()
#     # sterg postarea
#     browser.find_element_by_xpath("//*[@class='deletelink']").click()
#     browser.implicitly_wait(3)
#     browser.find_element_by_xpath('/html/body/div/div[3]/form/div/input[2]').click()
#     browser.implicitly_wait(3)
#     # assert "successfully" in showclass

# def testLogout():
#     # apas log out
#     browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()
#     browser.implicitly_wait(3)
#     # inchid ferastra browserului
#     browser.close()
