import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException, NoSuchWindowException


class Bot_Brain:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="assets/chromedriver.exe")

    def login(self, GMAIL, PASS):
        self.driver.maximize_window()
        self.driver.get(url="https://vityarthi.com/login")
        time.sleep(1)

        self.driver.find_element(By.NAME, "username").send_keys(GMAIL)
        self.driver.find_element(By.ID, "password").send_keys(PASS)
        self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)

    def engine(self, TO_CLICK):
        self.driver.get(url="https://vityarthi.com/course/learning/Python-Essentials")
        time.sleep(2)

        module_codes = [35, 37, 39, 42, 43, 44, 45, 46, 48, 56, 68, 77, 79]
        for i in TO_CLICK:
            try:
                """opening the module"""
                self.driver.find_element(By.ID, f'chapter_{module_codes[i]}').click()
                time.sleep(1)

                j = 0
                while True:
                    try:
                        j += 1
                        """clicking video box to open it"""
                        self.driver.find_element(By.XPATH,
                                                 f'//*[@id="collapseChapter{module_codes[i]}"]/div/div[{j}]').click()
                        time.sleep(0.5)

                        """clicking checkbox"""
                        self.driver.find_element(By.XPATH,
                                                 f'//*[@id="collapseChapter{module_codes[i]}"]/div/div[{j}]/div/div['
                                                 f'2]/div/label').click()
                        time.sleep(0.5)

                        """scrolling content page to avoid exception"""
                        pg.press("pagedown")

                    except ElementNotInteractableException or ElementClickInterceptedException:
                        print(f"Inner exception at: {i+1}, vid: {j}")
                        pass
                    except NoSuchElementException:
                        print(f"Module {i+1} completed.")
                        break

            except ElementNotInteractableException or ElementClickInterceptedException:
                print(f"Outer exception at: {i+1}, vid: {j}")
                pass
            except NoSuchWindowException:
                print("Window closed.")
                exit()
