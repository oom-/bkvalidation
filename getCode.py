#!/usr/bin/env python3
#Get Code for BKBURGER

from selenium import webdriver
import sys
import os

toto = -1

def nextPage(driver):
    global toto
    toto += 1;
    i = 0
    driver.find_element_by_id("NextButton").click()

    try:
        if driver.find_element_by_id("softblock").get_attribute("softblock") == "softblock" :
            print ("FAil ! page saved in =>" + "toto"+ str(toto) +".jpg")
            driver.save_screenshot("toto"+ str(toto) +".jpg")
            sys.exit(0)
    except:
        i = 1
    try:
        if driver.find_element_by_id("FNSleftBlank").get_attribute("FNSleftBlank") == "FNSleftBlank" :
            print ("FAil ! page saved in =>" + "toto"+ str(toto) +".jpg")
            driver.save_screenshot("toto"+ str(toto) +".jpg")
            sys.exit(0)
    except:
        i = 1
    try:
        print (driver.find_element_by_id("ProgressPercentage").get_attribute("innerHTML"))
    except:
        i = 12

def coche(driver):
    i = 0
    elements = driver.find_elements_by_class_name("radioBranded")
    nbelements = len(elements)
    total = nbelements
    if nbelements == 6 or nbelements == 12:
        while nbelements > 0:
            driver.find_elements_by_class_name("radioBranded")[(nbelements % 2 + i) % total].click()
            nbelements = nbelements - 2
            i = i + 2
    elif nbelements >= 5 :
        while nbelements > 0:
            driver.find_elements_by_class_name("radioBranded")[(nbelements % 5 + i) % total].click()
            nbelements = nbelements - 5
            i = i + 5
    elif nbelements > 1:
        driver.find_elements_by_class_name("radioBranded")[1].click()
    elif nbelements == 1:
        driver.find_elements_by_class_name("radioBranded")[0].click()

def getBKcode(ref1, day, month, year, hour, min):
    i = 0
    index = "https://www.bkvousecoute.fr"
    scriptp1 = "document.getElementById(\"SurveyCode\").value = " + ref1 + ";"
    scriptp1 = scriptp1 + "document.getElementById(\"InputDay\").value = '"+ str(day).rjust(2, '0') +"';"
    scriptp1 = scriptp1 + "document.getElementById(\"InputMonth\").value = '" + str(month).rjust(2, '0') + "';"
    scriptp1 = scriptp1 + "document.getElementById(\"InputYear\").value = '" + str(year).rjust(2, '0') + "';"
    scriptp1 = scriptp1 + "document.getElementById(\"InputHour\").value = '" + str(hour).rjust(2, '0') + "';"
    scriptp1 = scriptp1 + "document.getElementById(\"InputMinute\").value = '" + str(min).rjust(2, '0') + "';"
    scriptp2 = "document.getElementsByTagName(\"select\")[0].value = \"2\";"
    scriptp2 = scriptp2 + "document.getElementsByTagName(\"select\")[1].value = \"2\";"
    scriptp3 = "document.getElementsByTagName(\"input\")[0].value = \"54000\""
    print ("Initialisation du navigateur :")
    if (os.name == 'nt'):
        driver = webdriver.PhantomJS("./PhantomJs/phantomjs-win.exe")
    else:
        driver = webdriver.PhantomJS("./PhantomJs/phantomjs-unix")
    #For firefox
    #fp = webdriver.FirefoxProfile()
    #driver = webdriver.Firefox(fp)
    driver.get(index)
    print ("Ok.")
    print ("Remplissage du formulaire :")
    nextPage(driver)
    driver.execute_script(scriptp1)
    nextPage(driver)
    if (len(driver.find_elements_by_class_name("radioBranded")) == 2):
        driver.find_elements_by_class_name("radioBranded")[1].click()
    else:
        try :
            driver.find_elements_by_class_name("radioBranded")[2].click()
        except:
            driver.save_screenshot("toto"+ str(toto) +".jpg")
    nextPage(driver)
    driver.find_elements_by_class_name("radioBranded")[1].click()
    nextPage(driver)
    driver.find_elements_by_class_name("radioBranded")[0].click()
    nextPage(driver)
    while (len(driver.find_elements_by_tag_name("select")) == 0):
        coche(driver)
        nextPage(driver)
    driver.execute_script(scriptp2);
    nextPage(driver)
    driver.execute_script(scriptp3)
    nextPage(driver)
    print (driver.find_elements_by_class_name("ValCode")[0].get_attribute('innerHTML'))

if len(sys.argv) != 7:
    print ("Usage: ./%s BKref day month year hh mm" % sys.argv[0])
    print ("Exemple: 22407 1 4 16 21 03")
else:
    print ("Ok, c'est parti pour un burger gratos !")
    getBKcode(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
