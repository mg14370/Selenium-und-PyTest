from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

# Hilfsfunktion
def js_click(element):
    driver.execute_script("arguments[0].click();", element)

# Chrome-Optionen
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# 1+2. Browser starten und zur URL navigieren
driver.get("https://www.automationexercise.com")
time.sleep(2)

# 3. Startseite überprüfen
assert driver.title != "", "❌ Startseite nicht sichtbar!"
print("✅ Startseite sichtbar!")

# Cookie Banner schließen falls vorhanden
try:
    cookie_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(@class, 'fc-cta-consent')]")
    ))
    js_click(cookie_button)
    time.sleep(1)
except:
    pass

# 4. Signup / Login klicken
signup_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login")))
js_click(signup_link)

# 5. "New User Signup!" überprüfen
signup_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='New User Signup!']")))
assert signup_text.is_displayed(), "❌ 'New User Signup!' nicht sichtbar!"
print("✅ 'New User Signup!' sichtbar!")

# 6. Name und E-Mail eingeben
driver.find_element(By.XPATH, "//input[@placeholder='Name']").send_keys("TestUser")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("test@test3000.com")
time.sleep(1)

# 7. Signup Button klicken
js_click(driver.find_element(By.XPATH, "//button[@data-qa='signup-button']"))
time.sleep(2)

# 8. "ENTER ACCOUNT INFORMATION" überprüfen
account_info = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Enter Account Information']")))
assert account_info.is_displayed(), "❌ 'ENTER ACCOUNT INFORMATION' nicht sichtbar!"
print("✅ 'ENTER ACCOUNT INFORMATION' sichtbar!")

# 9. Details ausfüllen
js_click(driver.find_element(By.ID, "id_gender1"))  # Titel: Mr
driver.find_element(By.ID, "password").send_keys("Test1234!")
Select(driver.find_element(By.ID, "days")).select_by_value("1")
Select(driver.find_element(By.ID, "months")).select_by_value("1")
Select(driver.find_element(By.ID, "years")).select_by_value("1990")
time.sleep(1)

# 10+11. Checkboxen
js_click(driver.find_element(By.ID, "newsletter"))
js_click(driver.find_element(By.ID, "optin"))
time.sleep(1)

# 12. Adressdaten
driver.find_element(By.ID, "first_name").send_keys("Test")
driver.find_element(By.ID, "last_name").send_keys("User")
driver.find_element(By.ID, "company").send_keys("TestCompany")
driver.find_element(By.ID, "address1").send_keys("123 Test Street")
driver.find_element(By.ID, "address2").send_keys("Apt 1")
Select(driver.find_element(By.ID, "country")).select_by_visible_text("India")
driver.find_element(By.ID, "state").send_keys("Bavaria")
driver.find_element(By.ID, "city").send_keys("Munich")
driver.find_element(By.ID, "zipcode").send_keys("80331")
driver.find_element(By.ID, "mobile_number").send_keys("01234567890")
time.sleep(1)

# 13. Create Account klicken
js_click(driver.find_element(By.XPATH, "//button[@data-qa='create-account']"))
time.sleep(2)

# 14. "ACCOUNT CREATED!" überprüfen
created = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@data-qa='account-created']")))
assert created.is_displayed(), "❌ 'ACCOUNT CREATED!' nicht sichtbar!"
print("✅ 'ACCOUNT CREATED!' sichtbar!")

# Werbe-Popup schließen falls vorhanden
try:
    close_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[text()='Close']")
    ))
    js_click(close_btn)
    time.sleep(1)
except:
    pass

# 15. Continue klicken
js_click(driver.find_element(By.XPATH, "//a[@data-qa='continue-button']"))
time.sleep(3)

# 16. "Logged in as username" überprüfen
logged_in = wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[contains(text(),'Logged in as')]")
))
assert logged_in.is_displayed(), "❌ Nicht eingeloggt!"
print("✅ Eingeloggt!")

# 17. Delete Account klicken
js_click(driver.find_element(By.XPATH, "//a[@href='/delete_account']"))
time.sleep(2)

# 18. "ACCOUNT DELETED!" überprüfen
deleted = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@data-qa='account-deleted']")))
assert deleted.is_displayed(), "❌ 'ACCOUNT DELETED!' nicht sichtbar!"
print("✅ 'ACCOUNT DELETED!' sichtbar!")

js_click(driver.find_element(By.XPATH, "//a[@data-qa='continue-button']"))
time.sleep(1)

driver.quit()

"""
python test_3_benutzer_registrieren.py
"""
