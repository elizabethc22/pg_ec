import pyautogui as pg
import webbrowser
import time

speak.Speak("Ni hao! Ni jiao shen me ming zi? Wo jiao PC. Wo hao ma! Ni ne?")
Location = pg.prompt("Where do you live? (write town and state)")



# Question 1

activity = pg.prompt(
"""
What kind of activity woukld you like to do?
a)Relaxing
b)Energized
c)A little of both

"""
    )



# Question 2

inout = pg.prompt(
"""
Would you like to be indoors or outdoors?
a)Outdoors
b)Indoors

"""
    )

if inout == "a" and activity == "a":
    answer = pg.confirm("Which activity would you like to do?" , "title" ,["beach/pool" , "shopping"])
    
            

if inout == "a" and activity == "b":
     answer = pg.confirm("Which activity would you like to do?" , "title" ,["hiking/biking" , "tennis"])
    
if inout == "a" and activity == "c":
    answer = pg.confirm("Which activity would you like to do?" , "title" ,["pool" , "shopping" , "tennis"])
    
if inout == "b" and activity == "a":
    answer = pg.confirm("Which activity would you like to do?" , "title" ,["spa/salon" , "shopping"])

if inout == "b" and activity == "b":
  answer = pg.confirm("Which activity would you like to do?" , "title" ,["gym/workout class" , "squash"])

if inout == "b" and activity == "c":
     answer = pg.confirm("Which activity would you like to do?" , "title" ,["yoga" , "shopping"])

answer2 = pg.confirm ("To clarify: your location is " + Location + " and you activity is " + answer + ".")

    



