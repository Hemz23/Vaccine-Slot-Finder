# 🇮🇳
# Developed By: Hemal Pitroda

from tkinter.constants import W
from logConfig import logger
import os
import sys
import time
import tkinter.font as tkfont
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from chromedriver_autoinstaller import install
import tkinter as tk

from bs4 import BeautifulSoup as bs

class Web:

    def __init__(self):
        self.cwd = os.getcwd()
        self.driver=''
        self.wait = 10
    
    def init_tkinter(self):
        win = tk.Tk()
        win.title('Vaccine Slot Finder')
        frm1 = tk.Frame(master=win,padx=10,pady=10)
        frm1.rowconfigure([0,1,2],minsize=20)
        frm1.columnconfigure([0,1],minsize=120)
        frm1.grid(row=0,column=0)

        btnFont = tkfont.Font(family='Calibri',size=16)

        lbl_mob = tk.Label(master=frm1,text="Mobile #")
        lbl_mob.grid(row=0,column=0,pady=5,padx=5,sticky='nsew')
        txt_mob = tk.Entry(master=frm1)
        txt_mob.grid(row=0,column=1,pady=5,padx=5,sticky='nsew')

        lbl_state = tk.Label(master=frm1,text="State")
        lbl_state.grid(row=1,column=0,pady=5,padx=5,sticky='nsew')
        txt_state = tk.Entry(master=frm1)
        txt_state.grid(row=1,column=1,pady=5,padx=5,sticky='nsew')

        lbl_city = tk.Label(master=frm1,text="City")
        lbl_city.grid(row=2,column=0,pady=5,padx=5,sticky='nsew')
        txt_city = tk.Entry(master=frm1)
        txt_city.grid(row=2,column=1,pady=5,padx=5,sticky='nsew')

        btn_process = tk.Button(master=frm1,text='Start',command=lambda:self.process(txt_mob.get(),txt_state.get(),txt_city.get()),height=1,width=20,font=btnFont)
        btn_process.grid(row=3,column=0,pady=10,columnspan=2)

        win.mainloop()
    
    def process_login(self,mob):
        try:
            number_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID, 'mat-input-0')))
            time.sleep(1)
            number_elm.send_keys(mob)
            time.sleep(0.5)
        except Exception as e:
            raise Exception(e)
        
        try:
            btn_otp = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//ion-button[contains(text(),"Get OTP")]')))
            self.driver.execute_script('arguments[0].click();',btn_otp)
            time.sleep(0.5)
        except Exception as e:
            raise Exception(e)
        messagebox.showinfo('OTP',"press ok after entering otp")
        time.sleep(1)
        try:
            btn_verify = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//ion-button[contains(text(),"Proceed")]')))
            self.driver.execute_script('arguments[0].click();',btn_verify)
            time.sleep(0.5)
        except Exception as e:
            raise Exception(e)

        try:
            # schedule_elms = WebDriverWait(self.driver, self.wait).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="m-lablename"]')))
            # for i in range(len(schedule_elms)):
            #     self.driver.execute_script('arguments[0].click();',schedule_elms[i])
            #     time.sleep(1)
            schedule_elms = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//span[@class="m-lablename"]')))
            self.driver.execute_script('arguments[0].click();',schedule_elms)
            time.sleep(1)
        except Exception as e:
            raise Exception(e)
        
        # try:
        #     final_schedule_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//ion-button[contains(text(),"Schedule Now")]')))
        #     self.driver.execute_script('arguments[0].click();',final_schedule_elm)
        #     time.sleep(0.5)
        # except Exception as e:
        #     raise Exception(e)
        
        # search by district
        try:
            district_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID, 'status')))
            self.driver.execute_script('arguments[0].click();',district_elm)
            time.sleep(0.5)
        except Exception as e:
            raise Exception(e)
        
    
    def process(self,mob,state,city):

        while True:

            try:
                try:
                    self.driver = webdriver.Chrome()
                except Exception as e:
                    logger.exception(e)
                    install()
                    self.driver = webdriver.Chrome()

                self.driver.get('https://selfregistration.cowin.gov.in/')

                self.process_login(mob)

                try:
                    state_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID, 'mat-select-value-1')))
                    self.driver.execute_script('arguments[0].click();',state_elm)
                    time.sleep(1)
                except Exception as e:
                    raise Exception(e)

                try:
                    state_name_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//span[@class="mat-option-text" and contains(text(),"' + state + '")]')))
                    self.driver.execute_script('arguments[0].click();',state_name_elm)
                    time.sleep(1)
                except Exception as e:
                    raise Exception(e)

                try:
                    city_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.ID, 'mat-select-value-3')))
                    self.driver.execute_script('arguments[0].click();',city_elm)
                    time.sleep(1)
                except Exception as e:
                    raise Exception(e)

                try:
                    city_name_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//span[@class="mat-option-text" and contains(text(),"' + city + '")]')))
                    city_name_elm.click()
                except Exception as e:
                    raise Exception(e)

                while True:
                    try:
                        try:
                            btn_search = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//ion-button[contains(text(),"Search")]')))
                            self.driver.execute_script('arguments[0].click();',btn_search)
                            time.sleep(0.5)
                        except Exception as e:
                            raise Exception(e)

                        try:
                            age_elm = WebDriverWait(self.driver, self.wait).until(EC.presence_of_element_located((By.XPATH, '//label[contains(text(),"Age 18+")]')))
                            self.driver.execute_script('arguments[0].click();',age_elm)
                            time.sleep(0.5)
                        except Exception as e:
                            raise Exception(e)
                        
                        try:
                            block_elms = WebDriverWait(self.driver, self.wait).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="vaccine-box vaccine-box1 vaccine-padding"]')))
                            for i in range(len(block_elms)):
                                block_text = block_elms[i].text.casefold().strip()
                                if "booked" not in block_text and block_text!='na' and block_text!='age 18+' and block_text!='':
                                    logger.info('Block Value:%s',block_elms[i].text.casefold().strip())
                                    messagebox.showinfo('FOUND','BLOCK FOUND! PLEASE PROCEED MANUALLY FROM HERE.')
                                    break
                        except Exception as e:
                            raise Exception(e)
                    except Exception as e:
                        if "SignIn for Vaccination" in self.driver.page_source:
                            self.driver.quit()
                            break
                        print(e)
                        logger.exception('Err:%s',e)

                

            except Exception as e:
                print(e)
                logger.exception('Err:%s',e)

obj = Web()
obj.init_tkinter()