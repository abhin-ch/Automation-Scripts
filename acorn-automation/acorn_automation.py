from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class Execute(object):
    def __init__(self):
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)
        
    def login_process(self, use, key):
        self.driver.get("https://www.acorn.utoronto.ca/")
        acorn = self.driver.find_element_by_link_text("Login to ACORN")
        acorn.click()
        try:
            username = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username.send_keys(use)
            
        except:
            self.driver.quit()

        try:
            password = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password.send_keys(key)
        except:
            self.driver.quit()

        try:
            log_in = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.NAME, "_eventId_proceed"))
            )
            log_in.click()
            self.driver.implicitly_wait(15)
            print("Log In Sucessful Chief! Trying Redirection")
        except:
            self.driver.quit()

    def redirect(self):
        try:
            redirect = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "acorn"))
            )
            self.driver.get("https://acorn.utoronto.ca/sws/#/courses/1")
            print("REDIRECTING..... ")
        except:
            self.driver.quit()

    def x_path(self, course):
        string = '//*[@id='+'"'+ course+ '-planCourseBox"]/div[1]/div/div[2]/div[1]/a'
        return string 

    def enrol(self,course):
        x_p = self.x_path(course)
        print(x_p)
        try:
            enrol = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, x_p ))
            )
            print(" Enrolling in "+ course )
            enrol.click()
        except:
            print("Sorry couldn't find "+ course + " Boss :(")


    def enrol_confirmation(self, course):
        try:
            enrol_confir = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="enrolFromPlan"]' ))
            )
            print("Bro you're enrolled in " + course + " Congratulation")
            enrol_confir.click()
        except:
            print("You were not enrolled in the Course :(")

    def exit(self):
        self.driver.quit()
