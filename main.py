import os
import time
import json
from bot_brain import Bot_Brain
from interface import App

switch_on = False
user_input = App().main_app()
switch_on = True

with

if switch_on:
    app = Bot_Brain()
    app.login(os.getenv("CGMAIL"), os.getenv("PASSWORD"))
    app.engine(user_input)

time.sleep(600)
