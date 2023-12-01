from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=chrome_options)


