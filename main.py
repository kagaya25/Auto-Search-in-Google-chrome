from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 

search = input("Enter the google search ")
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get('https://www.google.com/search?q='+search) 

print("Finished") 