#!/usr/bin/env python3
"""
InnerWorks Metrics Automation Script
Sends metrics from Chrome, Firefox, and Brave browsers automatically
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Configuration
URL = "http://localhost:5173"  # Change to your deployed URL or ngrok URL
DEVICE_NAME = "LenovoY520Ubuntu"

def send_metrics_chrome(device_name):
    """Send metrics using Chrome browser"""
    print(f"🌐 Opening Chrome...")

    options = ChromeOptions()
    # options.add_argument('--headless')  # Uncomment to run in background
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)
        print(f"✅ Chrome opened: {URL}")

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # Fill Device Name
        device_input = wait.until(EC.presence_of_element_located((By.ID, "deviceName")))
        device_input.clear()
        device_input.send_keys(device_name)
        print(f"📝 Device Name entered: {device_name}")

        # Click dropdown
        dropdown = driver.find_element(By.CLASS_NAME, "dropdown-trigger")
        dropdown.click()
        time.sleep(0.5)

        # Select Chrome from dropdown
        chrome_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-item') and text()='Chrome']"))
        )
        chrome_option.click()
        print(f"🔽 Browser selected: Chrome")

        # Click Send button
        send_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        send_button.click()
        print(f"🚀 Sending metrics...")

        # Wait for success message
        success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
        print(f"✅ Success: {success.text}")

        # Wait 2 seconds before closing
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error in Chrome: {str(e)}")
    finally:
        driver.quit()
        print(f"🔒 Chrome closed\n")

def send_metrics_firefox(device_name):
    """Send metrics using Firefox browser"""
    print(f"🌐 Opening Firefox...")

    options = FirefoxOptions()
    # options.add_argument('--headless')  # Uncomment to run in background
    driver = webdriver.Firefox(options=options)

    try:
        driver.get(URL)
        print(f"✅ Firefox opened: {URL}")

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # Fill Device Name
        device_input = wait.until(EC.presence_of_element_located((By.ID, "deviceName")))
        device_input.clear()
        device_input.send_keys(device_name)
        print(f"📝 Device Name entered: {device_name}")

        # Click dropdown
        dropdown = driver.find_element(By.CLASS_NAME, "dropdown-trigger")
        dropdown.click()
        time.sleep(0.5)

        # Select Firefox from dropdown
        firefox_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-item') and text()='Firefox']"))
        )
        firefox_option.click()
        print(f"🔽 Browser selected: Firefox")

        # Click Send button
        send_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        send_button.click()
        print(f"🚀 Sending metrics...")

        # Wait for success message
        success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
        print(f"✅ Success: {success.text}")

        # Wait 2 seconds before closing
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error in Firefox: {str(e)}")
    finally:
        driver.quit()
        print(f"🔒 Firefox closed\n")

def send_metrics_brave(device_name):
    """Send metrics using Brave browser"""
    print(f"🌐 Opening Brave...")

    options = ChromeOptions()
    # Path to Brave binary (macOS)
    options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
    # options.add_argument('--headless')  # Uncomment to run in background

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)
        print(f"✅ Brave opened: {URL}")

        # Wait for page to load
        wait = WebDriverWait(driver, 10)

        # Fill Device Name
        device_input = wait.until(EC.presence_of_element_located((By.ID, "deviceName")))
        device_input.clear()
        device_input.send_keys(device_name)
        print(f"📝 Device Name entered: {device_name}")

        # Click dropdown
        dropdown = driver.find_element(By.CLASS_NAME, "dropdown-trigger")
        dropdown.click()
        time.sleep(0.5)

        # Select Brave from dropdown
        brave_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dropdown-item') and text()='Brave']"))
        )
        brave_option.click()
        print(f"🔽 Browser selected: Brave")

        # Click Send button
        send_button = driver.find_element(By.CLASS_NAME, "btn-primary")
        send_button.click()
        print(f"🚀 Sending metrics...")

        # Wait for success message
        success = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))
        print(f"✅ Success: {success.text}")

        # Wait 2 seconds before closing
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error in Brave: {str(e)}")
    finally:
        driver.quit()
        print(f"🔒 Brave closed\n")

def main():
    """Main function to run automation"""
    print("=" * 60)
    print("🤖 InnerWorks Metrics Automation Started")
    print("=" * 60)
    print(f"🌐 Target URL: {URL}")
    print(f"💻 Device Name: {DEVICE_NAME}")
    print(f"🔧 Browsers: Chrome, Firefox, Brave")
    print("=" * 60 + "\n")

    # Send metrics from each browser
    send_metrics_chrome(DEVICE_NAME)
    send_metrics_firefox(DEVICE_NAME)
    send_metrics_brave(DEVICE_NAME)

    print("=" * 60)
    print("✅ Automation Completed Successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
