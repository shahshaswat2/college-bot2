from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


EnrollNo = input("Enter Enrollment Number: ")
Password = input("Enter Password: ")


class ParulBot:

    # visit link about how to install chromedriver(https://sites.google.com/a/chromium.org/chromedriver/downloads)
    driver = webdriver.Chrome("C:/chromedriver")

    def login(self):
        # calling our driver to open Chrome
        driver = self.driver
        driver.get("http://180.211.119.163:8081/StudentPanel/")
        time.sleep(2)
        # read the selenimum documentation to finding/locating particular text box, elements, links etc
        # here we use xpath method to find username and password box
        user_element = driver.find_element_by_xpath(
            "//input[@name='txtEnrollmentNo']")
        user_element.send_keys(EnrollNo)
        password_element = driver.find_element_by_xpath(
            "//input[@name='txtPassword']")
        password_element.send_keys(Password)
        time.sleep(2)

    # to go to attendance page after signing in
    def attendance(self):
        driver = self.driver
        driver.get(
            "http://180.211.119.163:8081/StudentPanel/TTM_Attendance/TTM_Attendance_StudentAttendance.aspx")
        time.sleep(2)


# "//input[@name='txtEnrollmentNo']"
# "//input[@name='txtPassword']"
# "//li[starts-with(@id, 'ctl00_li_student_Attendance')]"
# "//a[@href='TTM_Attendance/TTM_Attendance_StudentAttendance.aspx']"

shaswatPU = ParulBot()
shaswatPU.login()
shaswatPU.attendance()
