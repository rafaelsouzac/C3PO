# arquivo de verificação dos atendentes
# é o encarregado de verificar qual robo é especializado para o atendimento.

from selenium import webdriver

driver = webdriver.Chrome(executable_path='../dirigindo/chromedriver.exe')
driver.get('https://www.facebook.com')
