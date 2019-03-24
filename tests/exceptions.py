from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Automation_POM_Framework2/drivers/chromedriver.exe")
#driver.get("www.google.com")#Webdriver Exception
driver.get("http://localhost:9001/login.do")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_name1("xyz").send_keys("admin")# No Such Element Exception

#ele=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")

driver.close()