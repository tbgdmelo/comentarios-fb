import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pyautogui

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

#modifique o caminho_para_chrome_driver e o link_postagem
#o link postagem pode ser de um comentario ou um reply

chrome = webdriver.Chrome(chrome_options=option, executable_path='caminho_para_chrome_driver')
chrome.get('link_postagem')

#inserir as informacoes da conta facebook que vai comentar
a1 = chrome.find_element_by_id("email")
a1.send_keys('meu_login')
a1 = chrome.find_element_by_id("pass")
a1.send_keys('minha_senha')
a1 = chrome.find_element_by_id("u_0_2")
a1.click()

time.sleep(15)
contador = 0 
while (contador < 100 ): #quantidade de comentarios que vai fazer
    cont = str(contador)
    pyautogui.write('plou', interval=0.25) #texto que vai comentar
    pyautogui.press('enter')
    contador=contador+1
    time.sleep(5)

chrome.close()