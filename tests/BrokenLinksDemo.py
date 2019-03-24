from selenium import webdriver
import requests

driver=webdriver.Chrome(executable_path="C:/Users/Dell/PycharmProjects/Automation_POM_Framework2/drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("www.google.com")#Webdriver Exception
#driver.get("http://localhost:9001/login.do")
driver.get("http://google.com")
ele=driver.find_element_by_tag_name("a")
print(type(ele))
el1=[]
el2=[]
for i in ele:
    r=requests.head(i.get_attribute("href"))
    if r.status_code !=200:
        el1.append(i.get_attribute("href"))

    else:
        el2.append(i.get_attribute("href"))

print("Broken Link",el1)
print("Working Link",el2)
