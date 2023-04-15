import os
import time
from test_bot import Bot_Brain
from interface import main_app

switch_on = False
user_input = main_app()
switch_on = True
if switch_on:
    app = Bot_Brain()
    app.login("arpitsengar2022@vitbhopal.ac.in", os.getenv("PASSWORD"))
    app.engine(user_input)
time.sleep(600)
