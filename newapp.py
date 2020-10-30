from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# creating class


class ParulBot:
    def __init__(self, username, password):
        # constructor
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome() (remove this comment if you want to use chromedriver)

    # visit link about how to install chromedriver(https://sites.google.com/a/chromium.org/chromedriver/downloads)

    # login function
    def login(self):
        # calling our driver to open web browser
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
        time.sleep(5)

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


shaswatPU = ParulBot(" enter your enrollment no",
                     " enter your password")
shaswatPU.login()
shaswatPU.attendance()

# the pumis website has been updated, this may or may not work anymore. Requires few changes in the xpath.
