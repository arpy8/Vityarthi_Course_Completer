import os
import time

from bot_brain import Bot_Brain
from app import test_app


switch_on = False
user_input = test_app()
switch_on = True
app = Bot_Brain()
app.login("arpitsengar2022@vitbhopal.ac.in", os.getenv("PASSWORD"))
app.engine(user_input)
time.sleep(600)
