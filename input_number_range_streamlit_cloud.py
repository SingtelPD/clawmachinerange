#======SUBJECT TO CHANGE===========
url = "https://fsm.sg.formulasquare.com/fsm_api/wawaji_cms/"
#==================================

import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True


st.title("5G Claw Machine CMS - input coupon code number range")
st.write("Please use the form below to enter the codes into the CMS system. Note: the form below accepts coupon codes that are whole numbers only.\n\n If at any point you encounter an error message, this could be due to the following: 1) username and/or password is incorrrect; or 2) coupon code already exists in the CMS system.")

form = st.form("range_form")
username = form.text_input("Please enter the CMS username")
password = form.text_input("Please enter the CMS password")
start_num = form.text_input("Starting coupon code number")
end_num = form.text_input("Ending coupon code number")
submit = form.form_submit_button("Add coupon codes to CMS")

if submit:
    st.info("Running. Please do NOT click on the button again.")

    #convert start_num and end_num to integer
    start_num = int(start_num)
    end_num = int(end_num)+1

    web = webdriver.Chrome(options=options)
    web.get(url)
    time.sleep(3)

    #Login
    username_field = web.find_element("xpath", '/html/body/div/div/main/div/div/div/div/form/div[1]/input')
    username_field.send_keys(username)
    password_field = web.find_element("xpath", '/html/body/div/div/main/div/div/div/div/form/div[3]/input')
    password_field.send_keys(password)
    submit_login_button = web.find_element("xpath", '/html/body/div/div/main/div/div/div/div/form/div[5]/input')
    submit_login_button.click()
    time.sleep(2)

    #navigate to coupon codes page
    coupon_codes = web.find_element("xpath", '/html/body/div/div/main/div/div[1]/button[3]')
    coupon_codes.click()
    time.sleep(1)

    #enter coupon codes within range
    for i in range (start_num, end_num):
        add_new = web.find_element("xpath", '/html/body/div/div/main/div/div[2]/div/div[1]/button')
        add_new.click()
        time.sleep(1)
        code_field = web.find_element("xpath", '/html/body/div/div/main/div/div[2]/div/div/form/div[1]/input')
        code_field.send_keys(i)
        time.sleep(1)
        submit_button = web.find_element("xpath", '/html/body/div/div/main/div/div[2]/div/div/form/div[8]/input')
        submit_button.click()
        time.sleep(1)
        st.write(f"Coupon code {i} has been added to the CMS system.")

    st.success("All oupon codes have been added to the CMS system")
