import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from hmi_automation.can_comm.can_sender import send_signal
from conftest import take_step_screenshot


# ---------------- Helper functions ----------------
def click_with_retry(xpath, wait, driver, label, retries=5, delay=1):
    """Click an element with retries and take screenshot."""
    for i in range(retries):
        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath))).click()
            print(f"✅ {label}")
            take_step_screenshot(driver, label)
            return True
        except Exception:
            print(f"⚠ Retry {i+1}/{retries} failed for xpath: {xpath}")
            time.sleep(delay)
    raise Exception(f"❌ Failed to click element: {xpath}")


def scroll_and_click(xpath, driver, wait, label, max_swipes=5):
    """Scroll and click an element if not immediately visible."""
    for i in range(max_swipes):
        try:
            element = driver.find_element(AppiumBy.XPATH, xpath)
            if element.is_displayed():
                element.click()
                print(f"✅ {label}")
                take_step_screenshot(driver, label)
                return True
        except:
            size = driver.get_window_size()
            driver.execute_script("mobile: swipeGesture", {
                "left": 0,
                "top": int(size["height"] * 0.6),
                "width": size["width"],
                "height": int(size["height"] * 0.2),
                "direction": "up",
                "percent": 0.8
            })
            time.sleep(1)
    raise Exception(f"❌ Failed to scroll and click: {xpath}")


# ---------------- Test ----------------
@pytest.mark.order(1)
def test_home_scooter_full_features(driver):
    wait = WebDriverWait(driver, 60)

    # ---------------- Home ----------------
    click_with_retry(
        '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[1]/android.view.View',
        wait, driver, "01_home_opened"
    )

    # ---------------- Scooter ----------------
    click_with_retry(
        '(//android.view.View[@content-desc="vehicle"])[1]',
        wait, driver, "02_scooter_opened"
    )

    # ---------------- Feature Tile ----------------
    scroll_and_click(
        '//android.widget.ScrollView/android.view.View[1]/android.view.View[2]',
        driver, wait, "03_feature_tile_opened"
    )

    # ---------------- BCM → HMI ACK ----------------
    send_signal("BCM_HMI_Features_Acknowledgment", {
        "BCM_Feature_Acknowledgment": 0,
        "BCM_Feature_Command": 0,
        "BCM_Feature_ID": 7,
        "BCM_Feature_ACK_Code": 2
    })
    print("📡 BCM Feature ACK sent")
    take_step_screenshot(driver, "04_bcm_ack_sent")
    time.sleep(1)

    # ---------------- Scroll up ----------------
    size = driver.get_window_size()
    driver.execute_script("mobile: swipeGesture", {
        "left": 0,
        "top": int(size["height"] * 0.2),
        "width": size["width"],
        "height": int(size["height"] * 0.6),
        "direction": "up",
        "percent": 0.8
    })
    print("⬆️ Screen scrolled up")
    take_step_screenshot(driver, "05_scrolled_up")
    time.sleep(1)

    # ---------------- Regen & Hill Hold ----------------
    send_signal("BCM_HMI_Features_Status", {"BCM_Regen_CustomState": 1})
    print("📡 Regen enabled")
    take_step_screenshot(driver, "06_regen_enabled")

    send_signal("BCM_HMI_Features_Status", {"BCM_HillHold_State": 1})
    print("📡 Hill Hold enabled")
    take_step_screenshot(driver, "07_hill_hold_enabled")
    time.sleep(1)

    # ---------------- Feature ID 7 Levels ----------------
    send_signal("HMI_BCM_Feature_Commands", {"HMI_Feature_ID": 7})
    print("📡 Feature ID 7 enabled")
    take_step_screenshot(driver, "08_feature_7_enabled")

    levels = {0: "Level1", 1: "Level2", 2: "Level3", 3: "Level4"}
    for sub_cmd, label in levels.items():
        send_signal("HMI_BCM_Feature_Commands", {
            "HMI_Feature_ID": 7,
            "HMI_Feature_Sub_Command": sub_cmd
        })
        print(f"🎚 Feature 7 set to {label}")
        take_step_screenshot(driver, f"09_feature7_{label}")
        time.sleep(0.7)

    # ---------------- Speed Limit ----------------
    click_with_retry(
        '//android.view.View[@content-desc="Speed-limit icon"]',
        wait, driver, "10_speed_limit_enabled"
    )

    # ---------------- Charging Module ----------------
    click_with_retry(
        '//android.widget.TextView[@text="Charging"]',
        wait, driver, "11_charging_module_opened"
    )

    charging_xpaths = [
        '(//android.view.View[@content-desc="Charging image"])[1]',
        '(//android.view.View[@content-desc="Charging image"])[2]',
        '//android.widget.ScrollView/android.view.View[3]/android.view.View'
    ]
    close_popup_xpath = '//android.view.ViewGroup/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'

    for idx, xpath in enumerate(charging_xpaths, start=1):
        scroll_and_click(xpath, driver, wait, f"12_charging_info_{idx}_opened")
        scroll_and_click(close_popup_xpath, driver, wait, f"13_charging_popup_{idx}_closed")
        time.sleep(1)

    # ---------------- Privacy Module ----------------
    click_with_retry(
        '//android.widget.TextView[@text="Privacy"]',
        wait, driver, "14_privacy_opened"
    )

    click_with_retry(
        '//android.view.View[@content-desc="Incognito icon"]',
        wait, driver, "15_incognito_enabled"
    )

    click_with_retry(
        '//android.view.View[@content-desc="Do Not Disturb icon"]',
        wait, driver, "16_dnd_enabled"
    )

    # ---------------- Widgets Module ----------------
    click_with_retry(
        '//android.widget.TextView[@text="Widgets"]',
        wait, driver, "17_widgets_opened"
    )

    click_with_retry(
        '//android.widget.ScrollView/android.view.View/android.view.View/android.view.View',
        wait, driver, "18_widget_toggled"
    )

    # ---------------- Button via UiSelector ----------------
    try:
        button = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Button")'
        )
        button.click()
        print("✅ Button clicked using UiSelector")
        take_step_screenshot(driver, "19_button_clicked")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Failed to click button using UiSelector: {e}")

    # ---------------- Close Scooter Screen ----------------
    scroll_and_click(
        '//android.view.View[@resource-id="benchmark_root"]/android.view.View[3]/android.view.View[1]/android.view.View',
        driver, wait, "20_scooter_screen_closed"
    )

    print("✅ Test completed successfully")
