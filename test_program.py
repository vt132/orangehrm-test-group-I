from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
import csv

PASSWORD = "Test123!"


class TestSuite:
    def __init__(self, components):
        self.components = components

    def run(self):
        for component in self.components:
            print(component)
            component.run()   

class TestCase:
    def __init__(self, data_file):
        self.data_file = data_file

    def read_data(self):
        with open(f"./{self.data_file}.csv", newline="") as f:
            reader = csv.DictReader(f)
            self.data_rows = [row for row in reader]

    def setup_login(self, driver):
        driver.maximize_window()
        wait = WebDriverWait(driver, 60)
        driver.get("http://localhost:80")
        wait.until(EC.url_to_be("http://localhost/web/index.php/auth/login"))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']/div[@class='orangehrm-login-container']/div[@class='orangehrm-login-slot-wrapper']/div[@class='orangehrm-login-slot']/div[@class='orangehrm-login-form']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys("admin1")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']/div[@class='orangehrm-login-container']/div[@class='orangehrm-login-slot-wrapper']/div[@class='orangehrm-login-slot']/div[@class='orangehrm-login-form']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(PASSWORD)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']/div[@class='orangehrm-login-container']/div[@class='orangehrm-login-slot-wrapper']/div[@class='orangehrm-login-slot']/div[@class='orangehrm-login-form']/form[@class='oxd-form']/div[@class='oxd-form-actions orangehrm-login-action']/button"))).click()

    def run_chrome(self):
        self.read_data()
        for data_row in self.data_rows:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.setup_login(driver)
            print(self.execute_test(data_row, driver))
            driver.quit()

    def run_firefox(self):
        self.read_data()
        for data_row in self.data_rows:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            self.setup_login(driver)
            print(self.execute_test(data_row, driver))
            driver.quit()

    def run_edge(self):        
        self.read_data()
        for data_row in self.data_rows:
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            self.setup_login(driver)
            print(self.execute_test(data_row, driver))
            driver.quit()

    def execute_test(self, data, driver):
        pass

    def run(self):
        self.run_firefox()
        self.run_chrome()
        self.run_edge()
        

class PIMFullNameEmployeeIDValid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="full_name_employee_id_valid",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["first_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["middle_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["last_name"])

        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text
            return "Fail"
        except:
            pass

        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass

        return "Pass"

class PIMFullNameEmployeeIDInvalid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="full_name_employee_id_invalid",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["first_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["middle_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["last_name"])   
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL, "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["eid"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div"))).click()

        try:
            if (WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text != "Should not exceed 30 characters"
                or WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text != "Should not exceed 30 characters" 
                or WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text != "Should not exceed 30 characters"):
                return "Fail"
        except:
            return "Fail"

        try:
            if data["invalid_eid_type"] == "exceed":
                if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should not exceed 10 characters":
                    return "Fail"
            else:
                if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Employee Id already exists":
                    return "Fail"
        except:
            return "Fail"

        return "Pass"


class PIMFullNameEmployeeIDEmpty(TestCase):
    def __init__(self):
        super().__init__(
            data_file="full_name_employee_id_empty",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["first_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["middle_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["last_name"])   
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL, "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div"))).click()

        try:
            if (WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text != "Required"
                or WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text != "Required"):
                return "Fail"
        except:
            return "Fail"
                
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text
            return "Fail"
        except:
            pass


        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass

        return "Pass"


class PIMFullNameEmployeeID(TestSuite):
    def __init__(self):
        super().__init__(components=[PIMFullNameEmployeeIDValid(), PIMFullNameEmployeeIDInvalid(), PIMFullNameEmployeeIDEmpty()])


class PIMUsernameInvalid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="username_invalid",
        )
    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']/label/span"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["username"])
        try:
            if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != data["message"]:
                return "Fail"
        except:
            return "Fail"
        return "Pass"


class PIMUsernameValid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="username_valid",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']/label/span"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["username"])
        try:
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class PIMUsername(TestSuite):
    def __init__(self):
        super().__init__(components=[PIMUsernameValid(), PIMUsernameInvalid()])


        

class PIMPasswordAndConfirmValid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="password_confirm_valid",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']/label/span"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["password"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["password"])
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).click()
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class PIMPasswordInvalid(TestCase):
    def __init__(self):
        super().__init__(
            data_file="password_invalid",
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']/label/span"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["password"])
        try:
            if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != data["message"]:
                print(data["message"])
                return "Fail"
        except:
            return "Fail"
        return "Pass"


class PIMPasswordAndConfirmMismatch(TestCase):
    def __init__(self):
        super().__init__(
            data_file="password_confirm_valid", # enough to create mismatch later
        )

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][2]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-paper-container']/div[@class='orangehrm-header-container']/button[@class='oxd-button oxd-button--medium oxd-button--secondary']"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']/label/span"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["password"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["password"] + "1")
        try:
            if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/form[@class='oxd-form']/div[@class='orangehrm-employee-container']/div[@class='orangehrm-employee-form']/div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Passwords do not match":
                return "Fail"
        except:
            return "Fail"
        return "Pass"

    


class PIMPasswordAndConfirm(TestSuite):
    def __init__(self):
        super().__init__(components=[
            PIMPasswordAndConfirmMismatch(),
            PIMFullNameEmployeeIDValid(),
            PIMPasswordInvalid(),
        ])

class PIMCreateEmployee(TestSuite):
    def __init__(self):
        super().__init__(components=(
            PIMFullNameEmployeeID(),
            PIMUsername(),
            PIMPasswordAndConfirm(),
        ))


class MyInfoFullNameAndIDValid(TestCase):
    def __init__(self):
        super().__init__(data_file="full_name_employee_id_valid")
    
    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["first_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["middle_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["last_name"])
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text
            return "Fail"
        except:
            pass

        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass

        return "Pass"

class MyInfoFullNameAndIDInvalid(TestCase):
    def __init__(self):
        super().__init__(data_file="full_name_employee_id_invalid")
    
    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["first_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["middle_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["last_name"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["eid"])
        try:
            if (WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text != "Should not exceed 30 characters" 
            or WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text != "Should not exceed 30 characters" 
            or WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text != "Should not exceed 30 characters"):
                return "Fail"
        except:
            return "Fail"
        
        try:
            if data["invalid_eid_type"] == "exceed":
                if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should not exceed 10 characters":
                    return "Fail"
            else:
                if WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Employee Id already exists":
                    return "Fail"
        except:
            return "Fail"

        return "Pass"


class MyInfoFullNameAndIDEmpty(TestCase):
    def __init__(self):
        super().__init__(data_file="full_name_employee_id_invalid")
    
    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        try:
            if (WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/span"))).text != "Required" 
            or WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][3]/span"))).text != "Required"):
                return "Fail"
        except:
            return "Fail"
        
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][1]/div[@class='oxd-grid-1 orangehrm-full-width-grid']/div[@class='oxd-grid-item oxd-grid-item--gutters']/div[@class='oxd-input-group']/div[@class='--name-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class MyInfoFullNameAndID(TestSuite):
    def __init__(self):
        super().__init__(components=(
            MyInfoFullNameAndIDValid(),
            MyInfoFullNameAndIDInvalid(),
            MyInfoFullNameAndIDEmpty(),
        ))


class MyInfoDriverLicenseOtherIDValid(TestCase):
    def __init__(self):
        super().__init__(data_file="other_id_and_driver_license_valid")

    def execute_test(self, data, driver ):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class MyInfoDriverLicenseOtherIDInvalid(TestCase):
    def __init__(self):
        super().__init__(data_file="other_id_and_driver_license_invalid")

    def execute_test(self, data, driver ):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        try:
            if (WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should not exceed 30 characters"
            or WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should not exceed 30 characters"):
                return "Fail"
        except:
            return "Fail"
        return "Pass"


class MyInfoDriverLicenseOtherIDEmpty(TestCase):
    def __init__(self):
        super().__init__(data_file="other_id_and_driver_license_valid") # 

    def execute_test(self, data, driver ):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["input"])
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["input"])
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class MyInfoDriverLicenseOtherID(TestSuite):
    def __init__(self):
        super().__init__(components=(
            MyInfoDriverLicenseOtherIDValid(),
            MyInfoDriverLicenseOtherIDInvalid(),
            MyInfoDriverLicenseOtherIDEmpty()
        ))


class MyInfoDateRelatedInvalid(TestCase):
    def __init__(self):
        super().__init__(data_file="date_related_invalid")

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()

        try:
            if (WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should be a valid date in yyyy-mm-dd format"
            or WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text != "Should be a valid date in yyyy-mm-dd format"):
                return "Fail"
        except:
            return "Fail"
        return "Pass"


class MyInfoDateRelatedEmpty(TestCase):
    def __init__(self):
        super().__init__(data_file="date_related_valid")

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["input"])
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(data["input"])
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()

        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"


class MyInfoDateRelatedValid(TestCase):
    def __init__(self):
        super().__init__(data_file="date_related_valid")

    def execute_test(self, data, driver):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-date-wrapper']/div[@class='oxd-date-input']/input"))).click()
        active_ele = driver.switch_to.active_element
        active_ele.send_keys(Keys.CONTROL + "a")
        active_ele.send_keys(Keys.DELETE)
        active_ele.send_keys(data["input"])
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/input"))).click()

        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][2]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/span"))).text
            return "Fail"
        except:
            pass
        return "Pass"

class MyInfoDateRelated(TestSuite):
    def __init__(self):
        super().__init__(components=(
            MyInfoDateRelatedInvalid(),
            MyInfoDateRelatedEmpty(),
            MyInfoDateRelatedValid(),
        ))


class MyInfoChoiceFieldAllCase(TestCase):
    def __init__(self):
        super().__init__(data_file="date_related_valid") # don't actually need data file

    def execute_test(self, data, driver):
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-text oxd-select-text--active']/div[@class='oxd-select-text--after']/i"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --positon-bottom']/div[@class='oxd-select-option'][2]"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-text oxd-select-text--active']/div[@class='oxd-select-text--after']/i"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][1]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --positon-bottom']/div[@class='oxd-select-option'][1]"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-text oxd-select-text--active']/div[@class='oxd-select-text--after']/i"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --positon-bottom']/div[@class='oxd-select-option'][2]"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-text oxd-select-text--active']/div[@class='oxd-select-text--after']/i"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][1]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group oxd-input-field-bottom-space']/div[2]/div[@class='oxd-select-wrapper']/div[@class='oxd-select-dropdown --positon-bottom']/div[@class='oxd-select-option'][1]"))).click()
        except:
            return "Fail"
        return "Pass"

class MyInfoChoiceField(TestSuite):
    def __init__(self):
        super().__init__(components=(MyInfoChoiceFieldAllCase(),)) # don't actually need data file


class MyInfoGenderAllCase(TestCase):
    def __init__(self):
        super().__init__(data_file="date_related_valid") # don't actually need data file

    def execute_test(self, data, driver):
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-navigation']/aside[@class='oxd-sidepanel']/nav[@class='oxd-navbar-nav']/div[@class='oxd-sidepanel-body']/ul[@class='oxd-main-menu']/li[@class='oxd-main-menu-item-wrapper'][6]/a"))).click()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group']/div[@class='--gender-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][1]/div[2]/div[@class='oxd-radio-wrapper']/label/span"))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row'][3]/div[@class='oxd-grid-3 orangehrm-full-width-grid'][2]/div[@class='oxd-grid-item oxd-grid-item--gutters'][2]/div[@class='oxd-input-group']/div[@class='--gender-grouped-field']/div[@class='oxd-input-group oxd-input-field-bottom-space'][2]/div[2]/div[@class='oxd-radio-wrapper']/label/span"))).click()
            
        except:
            return "Fail"
        return "Pass"


class MyInfoGender(TestSuite):
    def __init__(self):
        super().__init__(components=(
            MyInfoGenderAllCase(),
        ))


class MyInfo(TestSuite):
    def __init__(self):
        super().__init__(components=(
            MyInfoFullNameAndID(),
            MyInfoDriverLicenseOtherID(),
            MyInfoChoiceField(),
            MyInfoGender()
        ))


def main():
    tests = (PIMCreateEmployee(), MyInfo())
    for test in tests:
        test.run()


if __name__ == "__main__":
    main()
