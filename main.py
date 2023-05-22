import sys
import unittest
from time import sleep

from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xmlrunner import xmlrunner


class HomePageTests(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):

        browser = None

        for i, arg in enumerate(sys.argv):
            if arg == '--browser' and i + 1 < len(sys.argv):
                browser = sys.argv[i + 1]
                break

        if browser == 'chrome':
            cls.driver = webdriver.Chrome('drivers/chromedriver.exe')
        elif browser == 'firefox':
            cls.driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        elif browser == 'edge':
            cls.driver = webdriver.Edge(executable_path='drivers/mseddriver.exe')
        else:
            print(f"Browser no valid: {browser}")

        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    def test_suggestion_class(self):
        driver = self.driver

        sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[1]/div[2]/fieldset/input"))
        )
        suggesstion_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/fieldset/input')
        suggesstion_element.send_keys("Me")

        WebDriverWait(driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, "//li//div[@class='ui-menu-item-wrapper'][contains(text(),'Mexico')]"))
        )

        suggestion = driver.find_element(By.XPATH, "//li//div[@class='ui-menu-item-wrapper'][contains(text(),'Mexico')]")
        suggestion.click()
        sleep(2)

    def test_dropdown_example(self):
        driver = self.driver

        dropdown_element = driver.find_element(By.XPATH, "//*[@id='dropdown-class-example']")
        dropdown_element.click()

        dropdown_select = driver.find_element(By.XPATH, "//*[@id='dropdown-class-example']/option[3]")
        dropdown_select.click()
        sleep(2)
        dropdown_element.click()
        sleep(1)
        dropdown_element.click()
        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='dropdown-class-example']/option[4]").click()
        sleep(1)

    def test_switch_window(self):
        driver = self.driver

        main_window = driver.current_window_handle

        driver.find_element(By.XPATH, "//*[@id='openwindow']").click()

        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

        all_windows = driver.window_handles

        for window in all_windows:
            if window != main_window:
                driver.switch_to.window(window)
                break

        try:
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
                (By.XPATH, "//*[contains(text(),'30 day money back guarantee')]"), "30 day money back guarantee"
            ))
            sleep(2)
        except TimeoutException:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            self.fail("El texto esperado '30 day money back guarantee' no está presente en la nueva ventana.")

    def test_switch_tab(self):
        driver = self.driver

        driver.find_element(By.XPATH, "//*[@id='opentab']").click()
        driver.switch_to.window(driver.window_handles[1])
        try:
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
                             (By.XPATH, "//*[contains(text(), 'View all courses')]"), "View all courses"))
        except TimeoutException:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            self.fail("El botón esperado 'View all courses' no está presente en la nueva ventana.")

    def test_switch_alert(self):
        driver = self.driver

        driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Stori Card")
        driver.find_element(By.CSS_SELECTOR, "input#alertbtn").click()
        alert = driver.switch_to.alert
        sleep(2)
        alert.accept()

        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Stori Card")
        driver.find_element(By.XPATH, "//*[@id='confirmbtn']").click()
        driver.switch_to.alert

        alert_text = alert.text
        self.assertEqual('Hello Stori Card, Are you sure you want to confirm?', alert_text)
        sleep(1)
        alert.accept()
        sleep(1)

    def test_table_example(self):
        driver = self.driver
        list_courses = []
        XPATH_PRICE_ELEMENT = "/html/body/div[3]/div[1]/fieldset/table/tbody/tr/td[3]"
        price = "25"
        total_courses = 0
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, XPATH_PRICE_ELEMENT)))

            price_elements = driver.find_elements(By.XPATH, XPATH_PRICE_ELEMENT)

            for i in range(len(price_elements)):
                price_table = driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/fieldset/table/tbody/tr[{i + 2}]/td[3]').text

                if price_table == price:
                    course_names = driver.find_element(By.CSS_SELECTOR, f"#product >tbody > tr:nth-child({i + 2}) > td:nth-child(2)").text
                    list_courses.append(course_names)
                    total_courses += 1
            print(f'Total of Number of Courses are: {total_courses}')
            print('\n'.join(map(str, list_courses)))
        except NoSuchElementException as ex:
            print(ex.msg)

    def test_table_fixed(self):
        driver = self.driver

        position = "Engineer"
        engineer_elements = len(driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr/td[2]"))

        try:
            for i in range(engineer_elements):
                position_table = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[{i +1}]/td[2]').text
                if position_table == position:
                    name_engineer = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr[{i +1}]/td[1]').text
                    print(name_engineer)
        except NoSuchElementException as ex:
            print(ex.msg)

    def test_iframe_example(self):
        driver = self.driver

        iframe_element = driver.find_element(By.XPATH, "//*[@id='courses-iframe']")
        driver.switch_to.frame(iframe_element)

        element_inside_iframe = driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div/div/div/div[2]/ul/li[2]").text
        print(element_inside_iframe)

        print("============= BONUS =================")
        columns = len(driver.find_elements(By.XPATH, "/html/body/div/div[2]/section[2]/div/div/div/div/ul"))
        for i in range(columns):
            paragraphs = len(driver.find_elements(By.XPATH, f'/html/body/div/div[2]/section[2]/div/div/div/div[{i + 1}]/ul/li'))

            for j in range(paragraphs):
                if (j+1) % 2 != 0:
                    paragraphs_text = driver.find_element(By.XPATH, f'/html/body/div/div[2]/section[2]/div/div/div/div[{i + 1}]/ul/li[{j + 1}]').text
                    print(paragraphs_text)
        driver.switch_to.default_content()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(argv=sys.argv[:1], verbosity=2, testRunner=HTMLTestRunner(output='', report_name='report'))
