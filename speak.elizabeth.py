import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your name?")

answer = pg.prompt ("Enter your answer")

if answer == "elizabeth":
    speak.Speak("Ok " + answer + "I am going to leave now. Here is youtube. What would you like to see on youtube.")
    answer1 = pg.prompt ("Enter your answer")
    wb.open("https://www.youtube.com/results?search_query=" + answer1)

elif answer == "vaughn":
    speak.Speak("self destruct")
    speak.Speak("JK I will give you ten seconds to run. 10... 9... 8... 7... 6... 5... 4... 3... 2... 1...Goodbye")
    
elif answer == "Megan":
    speak.Speak("Stop talking to me. I am so superior. In the time you heard this I just learned eve
