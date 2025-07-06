from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


class Login:
    def __init__(self, driver):
        self.driver = driver

    def abrir_pagina(self):
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/login.php#")

    def inserir_email(self, usuario):
        self.driver.find_element(By.XPATH, '(//input[@class="form-control"])[1]').send_keys(usuario)

    def inserir_senha(self, senha):
        self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(senha)

    def login(self):
        self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]').click()



cadastro = Login(driver)
cadastro.abrir_pagina()
cadastro.inserir_email("iancadel@gmail.com")
cadastro.inserir_senha("123443")
cadastro.login()

driver.quit()













