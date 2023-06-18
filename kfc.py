import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
  print('input num')
  kfcnum = input()
  driver = webdriver.Chrome()
  driver.get('https://s.kfcvisit.com/cze')
  numbox = driver.find_element('id','InputCouponNum')
  numbox.send_keys(kfcnum)
  time.sleep(2)
  url = driver.current_url
  x = "Finish"
  while url.find(x) == -1:
    if x in url:
      break
    next1 = driver.find_element('id','NextButton')
    next1.click()
    time.sleep(1)
    url = driver.current_url
    print(url)
  
  outcome = driver.find_element(By.CSS_SELECTOR,'p.ValCode')
  code = outcome.get_attribute('innerHTML')
  print(code)
  driver.quit()
 
