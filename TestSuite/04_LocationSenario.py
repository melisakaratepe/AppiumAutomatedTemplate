import base64
import os
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.kobil.kycandroidapp.app'
desired_caps['appActivity'] = 'com.kobil.kycandroidapp.app.MainActivity'
desired_caps['app'] = 'C:\KYC\kyc-v5-android-app-release.apk'
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

screenshot_name = time.strftime("_%Y_%m_%d-%H%M%S")

screenshot_name = driver.current_activity + screenshot_name
path_name = "/Users/Melisa/Desktop/AppiumSession/Screenshots/"
file_extension = ".png"

video_name = driver.current_activity + time.strftime("_%Y_%m_%d-%H%M%S")
video_extension = ".mp4"
video_path_name = os.path.join(path_name + video_name + video_extension)

try:

    driver.start_recording_screen()
    driver.implicitly_wait(20)
    driver.find_element_by_id("com.kobil.kycandroidapp.app:id/custombutton_start_continue").click()
    driver.find_element_by_id("com.kobil.kycandroidapp.app:id/custombutton_home_selection_verify").click()
    driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(
        expected_conditions.element_to_be_clickable(
            (By.ID, "com.kobil.kycandroidapp.app:id/custombutton_mrz_lets_start")))
    driver.find_element_by_id("com.kobil.kycandroidapp.app:id/custombutton_mrz_lets_start").click()
    driver.implicitly_wait(10)
    driver.find_element_by_id("com.kobil.kycandroidapp.app:id/custombutton_mrz_lets_start").click()
    driver.implicitly_wait(15)
    driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button").click()

except NoSuchElementException as err:
    print("NoSuchElementException: {0}".format(err))
    driver.save_screenshot(path_name + screenshot_name + file_extension)
    print("there is a bug")
    video_data = driver.stop_recording_screen()
    with open(video_path_name, "wb") as video_file:
        video_file.write(base64.b64decode(video_data))

except:
    print("Unexpected error")

finally:
    print("the test finished")
    driver.stop_recording_screen()
