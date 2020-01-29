import webbrowser
import pyautogui
import random
from PIL import Image

chrome_app='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
urlFile="urls.txt"

facebookUrl="https://www.facebook.com/groups/mediumwriting/permalink/1187554121618814/"


with open(urlFile) as fp:
    url=fp.readline()
    while url:
        webbrowser.get(chrome_app).open(url)

        pyautogui.moveTo(x=200,y=200,duration=4.0)
        pyautogui.hscroll(-1500)
        pyautogui.moveTo(x=300,y=300,duration=1.5)

        k=0
        ok=0
        while ok == 0 and k != 4:
            screenshot=pyautogui.screenshot()
            graySS=screenshot.convert("L")
            bwSS=graySS.point(lambda x: 0 if x<255 else 255, '1')
            bwSS.save("an"+str(k)+".png")
            k+=1
            pattern=Image.open("clapThresholded.png")

            box = pyautogui.locate(pattern,bwSS,confidence=0.5)
            print(box)
            if box is None:
                pyautogui.moveTo(x=200, y=200, duration=0.5)
                pyautogui.hscroll(-300)
                pyautogui.moveTo(x=300, y=300, duration=1.0)
            else:
                ok=1

        if ok==1:
            pyautogui.click(x=box[0]+20,y=box[1]+20,duration=1.0)

            i=0
            for i in range(0,50):
                t= (float(int(random.random()*100)))/100
                if t<0.5:
                    t=t+0.5
                print(t)
                pyautogui.click(duration=t)

        url=fp.readline()



