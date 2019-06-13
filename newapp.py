from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# creating a class


class ParulBot:
    def __init__(self, username, password):
        # constructor
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    # closing of browser is not necessary but still if you want to..
    def closeBrowser(self):
        self.driver.close()

    #   login function
    def login(self):
        # calling our driver to open firefox
        driver = self.driver
        driver.get("http://180.211.119.163:8081/StudentPanel/")
        time.sleep(2)
        # read the selenimum documentation to finding/locating particular text box, elements, links etc
        # here we use xpath method to find username and password box
        user_element = driver.find_element_by_xpath(
            "//input[@name='txtEnrollmentNo']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath(
            "//input[@name='txtPassword']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
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


shaswatPU = ParulBot(" enter your enrollment number ",
                     " enter your password here ")
shaswatPU.login()
shaswatPU.attendance()
