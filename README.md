# Vityarthi Course Completer
Web automation program designed to complete your [Vityarthi Course](https://vityarthi.com/classes?sort=newest)! This program is designed to help save you time and effort by automating the repetitive tasks of marking the videos as done.

# Installation
- Clone the repo using:  
```
  git clone https://github.com/arpy8/vityarthi-course-completer
```

- change directory to your local repo in cmd
```
  cd vityarthi-course-completer
```

- Install required libraries
```
  pip install -r requirements.txt
```


### Do these before running "main.py"
  - Go to [settings](https://vityarthi.com/panel/setting) in vityarthi and enter your email (college email) and password.
  - Enter the same id/pass in "user_info.txt" and save it. 
  - Finally, run main.py

The program will automatically go through each video and mark it as done for every module that is specified, allowing you to focus on other important things while the program does the work. 

### Few things I'd like to mention:
- This project is still under development.
- There's a bug which doesn't allow this app to complete module 1, avoid selecting it. I'll try resolving it asap.
- Please keep in mind my program's basic work is to just trigger the "I passed this lesson" button for every video, so in case there is any video which is already marked as done, the bot will click it too.
- Avoid interacting with the machine while the programming is running, since doing that would result in an error and cause the program to crash.

# Demo
<p style="text-align:center;">(2x speed)</p>
<img src="assets/demo.gif" width="1400">


# Contact
If you have any questions or face any issue, please don't hesitate to reach out to [me](mailto:arpitsengar99@gmail.com).
