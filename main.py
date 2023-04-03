from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    options = ()
    browser = make_chrome_browser(*options)

    browser.maximize_window()
    browser.get('https://phptravels.com/demo/')
    

        # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, 'form')
        )
    )

    # Completando formulario
    browser.find_element(By.CLASS_NAME, 'first_name').send_keys("Felipe Manoel")
    browser.find_element(By.CLASS_NAME, 'last_name').send_keys("Ferreira da Costa")
    browser.find_element(By.CLASS_NAME, 'business_name').send_keys("Shakalzyn")
    browser.find_element(By.CLASS_NAME, 'email').send_keys("shakalzyn@mail.com")

    # Resolvendo conta
    numero1 = int(browser.find_element(By.ID, 'numb1').text)
    numero2 = int(browser.find_element(By.ID, 'numb2').text)
    resultadoconta = numero1 + numero2
    browser.find_element(By.ID, 'number').send_keys(resultadoconta)

    # Submetendo formulário 
    browser.find_element(By.ID, 'demo').click()

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
