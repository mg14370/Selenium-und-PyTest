import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_und_produkt():
    driver = webdriver.Chrome()

    # Navigiere zu saucedemo.com
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Benutzername eingeben
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)

    # Passwort eingeben
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)

    # Login Button klicken
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Überprüfe ob Login erfolgreich war
    assert "inventory" in driver.current_url, "Login fehlgeschlagen!"
    time.sleep(2)

    # Produkt "Sauce Labs Backpack" suchen
    product = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']")
    time.sleep(2)

    # Sicherstellen, dass das Produkt angezeigt wird
    assert product.is_displayed(), "Produkt 'Sauce Labs Backpack' nicht gefunden!"
    time.sleep(2)

    driver.quit()
