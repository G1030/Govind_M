from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies=driver.get_cookies()
print("Size of Cookies:",len(cookies))

#PRINT DETAILS OF ALL COOKIES
for c in cookies:
    #print(c)                                #Print All Cookies
    print(c.get("name"))                    #Print All Cookies Name
    #print(c.get("name"),":",c.get("value"))

#HOW TO ADD NEW COOKIE
driver.add_cookie({"name":"MyCookie","value":"12345"})
cookies=driver.get_cookies()
print("Size of Cookies After Adding New One:",len(cookies))

#DELETE SPECIFIC COOKIE
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("Size of Cookies After Delete One:",len(cookies))

#DELETE ALL COOKIES
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of Cookies Delete All:",len(cookies))

driver.quit()


