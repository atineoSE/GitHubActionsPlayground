#!/usr/bin/python3

import os

def check_environment_vars():
    dummy_var = os.environ.get('DUMMY_VAR')
    dummy_secret = os.environ.get('DUMMY_SECRET')
    if dummy_var == "my_dummy_var":
    	print("Dummy var retrieved successfully")
    else:
    	print("Dummy var not recognized")
    if dummy_secret == "my_dummy_secret":
    	print("Dummy secret retrieved successfully")
    else:
        print("Dummy secret not recognized")

def increment_counter():
    with open('counter', 'r+') as f: 
        num = int(f.read()) 
        num += 1 
        f.seek(0) 
        f.write(str(num))    

if __name__ == '__main__':
    check_environment_vars()
    increment_counter()

