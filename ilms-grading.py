from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import random
from hw_id_parser import hw_id_parser
from customize import HW_WEBSITE, CSV_FILENAME
from customize import ACCOUNT, PASSWORD
from customize import customize_comment
from customize import CLEAR_PREVIOUS

ILMS_WEBSITE = 'http://lms.nthu.edu.tw'

class bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.grades = {}
        print('start reading %s.......'%(CSV_FILENAME))
        self.read_csv(CSV_FILENAME)
        print('find %d scores in %s\n'%(len(self.grades), CSV_FILENAME))
        
        print('start parsing index.html.......')
        parser = hw_id_parser()
        parser.start()
        self.hw_id_table = parser.get_table()
        print('parse ending')
        print('find %d students in index.html.\n'%(len(self.hw_id_table)))
   

    def start(self):
        self.driver.get(ILMS_WEBSITE)
        
        sleep(1)

        print('login....\n')
        self.login()
        
        sleep(2)

        print('re-direct to homework website...')
        self.driver.get(HW_WEBSITE)

        sleep(1)

        first_student = self.driver.find_element_by_xpath('//*[@id="t1_tr0"]/td[2]/div/a')
        first_student.click()

        sleep(1)
        last_one = False
        while not last_one:
            last_one = self.grading()
        
        print('done.:))')
    

    def check_is_finish(self):
        is_last_one = self.driver.find_element_by_xpath('//*[@id="fmNext"]').get_attribute("value") # //*[@id="fmNext"]
        is_last_one = int(is_last_one)
        if is_last_one == 1:
            return False
        return True
    
    def find_student_name(self):
        # by 黃oo, 2020-04-15 22:55, 人氣(33)
        doc_txt = self.driver.find_element_by_xpath('//*[@id="doc"]/div[2]/div[1]').text

        NAME = doc_txt[doc_txt.find(' ')+1: doc_txt.find(',')]
        return NAME
    
    def get_student_id(self):
        # http://lms.nthu.edu.tw/course.php?courseID=40770&f=doc&cid=2066894
        url = self.driver.current_url
        cid_index = url.rfind('=') + 1
        cid = url[cid_index:]
        student_id = self.hw_id_table[cid]
        return student_id

    def grading(self):
        # find the name
        NAME = self.find_student_name()
        ID   = self.get_student_id()
        print('start grading ', ID,NAME)
        
        grade = self.grades[ID]

        # grading
        grade_btn = self.driver.find_element_by_xpath('//*[@id="tScore"]/a')
        grade_btn.click()

        sleep(0.4)

        self.driver.switch_to.frame('if1')
        grade_input = self.driver.find_element_by_xpath('//*[@id="fmScore"]')
        if CLEAR_PREVIOUS: grade_input.clear()
        grade_input.send_keys(grade['score'])
        
        

        comment = customize_comment(grade)

        comment_input = self.driver.find_element_by_xpath('//*[@id="fmScoreNote"]')
        if CLEAR_PREVIOUS: comment_input.clear()
        comment_input.send_keys(comment)
        last_one = self.check_is_finish()

        sleep(1)

        # next one
        comfirm_btn = self.driver.find_element_by_xpath('//*[@id="fm"]/div[2]/input[1]')
        comfirm_btn.click()
        sleep(1)
        return last_one
    
    def safe_find_by_xpath(self, xpath):
        btn = None
        while True:
            try:
                btn = self.driver.find_element_by_xpath(xpath)
                break
            except:
                print('find not safely...')
                r = random.randint(0, 4)/10
                sleep(r)
        return btn

    
    def login(self):
        login_btn = self.driver.find_element_by_xpath('//*[@id="login"]/a[3]')
        login_btn.click()
        
        self.wait_page_by_check_xpath('//*[@id="loginAccount"]')


        account_input = self.driver.find_element_by_xpath('//*[@id="loginAccount"]')
        account_input.send_keys(ACCOUNT)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginPasswd"]')
        password_input.send_keys(PASSWORD)

        login_btn = self.driver.find_element_by_xpath('//*[@id="base"]/div[2]/div/div/div[4]/input[1]')
        login_btn.click()

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def wait_page_by_check_xpath(self, xpath):
        while True:
            if self.check_exists_by_xpath(xpath):
                break
            sleep(1)

    def read_csv(self, csv_path):
        G = None
        with open(csv_path, newline='') as csvfile:
            G = list(csv.reader(csvfile))
        keys = G[0]

        for g in G:
            if g[0] == 'ID': continue
            ID = g[0]
            m = {}
            for i in range(len(keys)):
                m[ keys[i] ] = g[i]
            self.grades[ID] = m

if __name__ == "__main__":
    my_bot = bot()
    my_bot.start()
