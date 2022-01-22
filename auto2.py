from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import easygui

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_argument("--user-data-dir=C:\\Users\\ragha\\AppData\\Local\\Google\\Chrome\\User Data\\") #Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\\Users\\ragha\\Downloads\\chromedriver_win32\\chromedriver.exe",options=chromeOptions)
link=easygui.enterbox("Enter link:")

driver.maximize_window()  
#https://forms.gle/Tze5KCuPNs3UphxW7
driver.get(link)
time.sleep(1)

questions=driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionBaseTitle")
for x in questions:
    print(x.text.lower())
    if("name" in x.text.lower()):
        print("YESSSSSSSSSSSSSSS")
print(len(questions))
print("----------------------------------------------")

answers=driver.find_elements_by_xpath("//*[@class='quantumWizTextinputPapertextareaInput exportTextarea' or @class='quantumWizTextinputPaperinputInput exportInput' or @class='freebirdFormviewerComponentsQuestionCheckboxRoot' or @class='appsMaterialWizToggleRadiogroupGroupContent exportGroupContent']")
#answers=driver.find_elements_by_xpath("//*[@class='quantumWizTextinputPaperinputInput exportInput']")

#print(len(answers))
#answers=driver.find_elements_by_class_name('quantumWizTextinputPaperinputInput exportInput')
print(len(answers))
#answers=driver.find_elements_by_class_name("freebirdFormviewerComponentsQuestionTextTextInput")
c=0;
for x in questions:
    if("name" in x.text.lower()):
        if("caps" in (x.text).lower() or "capital" in (x.text).lower() or "capitals" in (x.text).lower()):
            answers[c].send_keys("RAGHAV MEHROTRA")
        else:
            answers[c].send_keys("Raghav Mehrotra")
    if("email" in x.text.lower()):
        answers[c].send_keys("raghav.mehrotra2019@vitstudent.ac.in")
    if("reg no" in x.text.lower() or "regno" in x.text.lower() or "reg no." in x.text.lower() or "regno." in x.text.lower()):
        answers[c].send_keys("19BIT0128")

    c=c+1
#for y in answers:
#    print(y.text)
#print(len(answers))

#name=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#ln="RAGHAV"
#name[0].send_keys(ln)
#email=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#email[0].send_keys("raghavmehrotra256@gmail.com")
#address=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
#address[0].send_keys("Padam Apartments, Civil Lines, Kanpur")
#phoneno=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
#phoneno[0].send_keys("7905089037")
#comments=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[2]/textarea')
#comments[0].send_keys("Nothing")

#submit=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
#submit[0].click()
submit=driver.find_elements_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
print(submit)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
submit[0].click()
time.sleep(4)
driver.quit()
