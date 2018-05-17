import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=k6NTcNFjVjE","https://www.youtube.com/watch?v=3opTwpiCZ6c","https://www.youtube.com/watch?v=3iU24f9-13Y"]

music = ["http://coldplay.com/","http://theacid.com/","http://www.kodaline.com/","http://stevemillerband.com/","http://www.khalidofficial.com/"]

answer = pg.prompt(
"""

Which would you rather do?
a) Catch some highlights
b) Listen to some ~groovy~ tunes

"""
    )
if answer == "a" or "Catch some highlights":
    for i in videos:
        webbrowser.open(i)


elif answer == "b" or "Listen to some groovy tunes":
    for i in music:
        webbrowser.open(i)
