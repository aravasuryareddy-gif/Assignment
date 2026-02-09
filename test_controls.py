import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from hmi_automation.can_comm.can_sender import send_signal
from conftest import take_step_screenshot


@pytest.mark.order(1)
def test_home_display_sound_and_light_settings(driver):
    wait = WebDriverWait(driver, 50)

    # ---------------- Home ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[1]/android.view.View'
    ))).click()
    take_step_screenshot(driver, "01_home_opened")

    # ---------------- Controls ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '(//android.view.View[@content-desc="vehicle"])[2]'
    ))).click()
    take_step_screenshot(driver, "02_controls_opened")

    # ---------------- Bluetooth ----------------
    bluetooth_xpath = '//android.view.View[@resource-id="benchmark_root"]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, bluetooth_xpath))).click()
    print("✅ Bluetooth enabled")
    take_step_screenshot(driver, "03_bluetooth_enabled")

    # ---------------- Display ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.TextView[@text="Display"]'
    ))).click()
    print("✅ Display opened")
    take_step_screenshot(driver, "04_display_opened")

    # ---------------- Brightness ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="minus_icon"])[1]'
    ))).click()
    print("➖ Brightness decreased once")
    take_step_screenshot(driver, "05_brightness_decreased")

    plus_xpath = '(//android.widget.ImageView[@content-desc="minus_icon"])[2]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, plus_xpath))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, plus_xpath))).click()
    print("➕ Brightness increased twice")
    take_step_screenshot(driver, "06_brightness_increased")

    # ---------------- Auto Brightness ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.view.View[@content-desc="auto_brightness"]'
    ))).click()
    print("🌞 Auto brightness toggled")
    take_step_screenshot(driver, "07_auto_brightness_toggled")

    # ---------------- Themes ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '(//android.view.View[@content-desc="theme Selected"])[1]'
    ))).click()
    print("🎨 Auto theme selected")
    take_step_screenshot(driver, "08_theme_auto")

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '(//android.view.View[@content-desc="theme Selected"])[2]'
    ))).click()
    print("🎨 Light theme selected")
    take_step_screenshot(driver, "09_theme_light")

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '(//android.view.View[@content-desc="theme Selected"])[3]'
    ))).click()
    print("🎨 Dark theme selected")
    take_step_screenshot(driver, "10_theme_dark")

    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '(//android.view.View[@content-desc="theme Selected"])[1]'
    ))).click()
    print("🎨 Auto theme selected")
    take_step_screenshot(driver, "11_theme_auto_again")

    # ---------------- Sound ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.TextView[@text="Sound"]'
    ))).click()
    print("🔊 Sound module opened")
    take_step_screenshot(driver, "12_sound_opened")

    # ---------------- Mute All ----------------
    mute_all_xpath = '//android.view.View[@resource-id="benchmark_root"]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, mute_all_xpath))).click()
    print("🔇 Mute All enabled")
    take_step_screenshot(driver, "13_mute_all_enabled")

    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, mute_all_xpath))).click()
    print("🔊 Mute All disabled")
    take_step_screenshot(driver, "14_mute_all_disabled")

    # ---------------- Parking Assist ----------------
    parking_xpath = '//android.view.View[@content-desc="Parking Assist"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, parking_xpath))).click()
    print("🚗 Parking Assist muted")
    take_step_screenshot(driver, "15_parking_assist_muted")

    # ---------------- Turn Indicators ----------------
    turn_xpath = '//android.view.View[@content-desc="Turn Indicators"]'
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, turn_xpath))).click()
    print("🔁 Turn Indicators muted")
    take_step_screenshot(driver, "16_turn_indicators_muted")

    # ---------------- Light ----------------
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.TextView[@text="Light"]'
    ))).click()
    print("💡 Light module opened")
    take_step_screenshot(driver, "17_light_opened")

    # ---------------- CAN Signal ----------------
    send_signal("HMI_BCM_Input_11", {"Enable_Escort_Light": 1})
    print("📡 HMI requested Light Assist")
    take_step_screenshot(driver, "18_light_assist_requested")

    print("✅ Test completed successfully")
