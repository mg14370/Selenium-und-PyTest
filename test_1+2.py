import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Aufgabe 1:  Login + Produkt prüfen
def test_login_and_product(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, "Login fehlgeschlagen!"
    product = driver.find_element(By.XPATH, "//*[text()='Sauce Labs Backpack']")
    assert product.is_displayed(), "Produkt nicht gefunden!"
    print("Produkt 'Sauce Labs Backpack' wurde gefunden!")

# Aufgabe 2: Parametrisierung
@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
])
def test_login(driver, username):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url, f"Login fehlgeschlagen für: {username}"
    print(f"Login erfolgreich für: {username}")
