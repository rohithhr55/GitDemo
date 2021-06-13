from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("https://www.pib.gov.in/indexd.aspx")
sel=Select(driver.find_element_by_xpath("/html/body/form/header/div[1]/div/div/div/div[2]/ul/li[2]/select"))
sel.select_by_visible_text("PIB Bengaluru")
#driver.find_element_by_xpath("/html/body/form/div[4]/div/nav/div/ul/li[5]/ul/li[1]/a").click()
