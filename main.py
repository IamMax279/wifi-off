from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# gateway IP
driver.get("http://192.168.1.1")

wait = WebDriverWait(driver, 10)

username = wait.until(EC.presence_of_element_located((By.ID, "login_username")))
password = driver.find_element(By.ID, "login_password")
button = driver.find_element(By.ID, "login_save")

username.send_keys("USERNAME")
password.send_keys("PASSWORD")
button.click()

devices_list = wait.until(EC.presence_of_element_located((By.ID, "devicesList")))
devices_list.click()

iframe = wait.until(EC.presence_of_element_located((By.ID, "iframeapp")))
driver.switch_to.frame(iframe)

laptop = wait.until(EC.presence_of_element_located((By.ID, "DEVICE_MAC_ADDRESS")))
laptop.click()

block_label = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="scheduler_mode_block"]')))
block_label.click()

save = driver.find_element(By.ID, "save")
save.click()

submit = wait.until(EC.presence_of_element_located((By.ID, "popup_block_confirm_submit")))
submit.click()