#!/usr/bin/python3

import os

def main():
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

if __name__ == '__main__':
    main()

