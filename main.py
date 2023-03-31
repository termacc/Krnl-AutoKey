import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--incognito")

# Step 1
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_position(0, 0)
driver.set_window_size(700, 700)
print("Step 1: Solve the captcha")
driver.get("https://cdn.krnl.place/getkey.php")
input("Solve the captcha and press enter to continue...")

for i in range(20, 0, -1):
    print(f"Step 1: Waiting for {i} seconds...", end='\r')
    time.sleep(1)

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Step 2
print("Step 2: Solve the captcha")
driver.get("https://cdn.krnl.place/getkey_games")
driver.execute_script("document.cookie='referrer=linkvertise.com';")
input("Solve the captcha and press enter to continue...")

for i in range(20, 0, -1):
    print(f"Step 2: Waiting for {i} seconds...", end='\r')
    time.sleep(1)

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Step 3
print("Step 3: Solve the captcha")
driver.get("https://cdn.krnl.place/getkey_games")
driver.execute_script("document.cookie='referrer=linkvertise.com';")
input("Solve the captcha and press enter to continue...")

for i in range(20, 0, -1):
    print(f"Step 3: Waiting for {i} seconds...", end='\r')
    time.sleep(1)

if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Step 4
print("Step 4: Solve the captcha")
driver.get("https://cdn.krnl.place/getkey_games")
driver.execute_script("document.cookie='referrer=linkvertise.com';")
input("Solve the captcha and press enter to continue...")

for i in range(20, 0, -1):
    print(f"Step 4: Waiting {i} seconds...", end='\r')
    time.sleep(1)

# Quit the browser
driver.quit()
