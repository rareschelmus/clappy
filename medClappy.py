import webbrowser
import pyautogui
import random
from PIL import Image

#uri for your browser
chrome_app='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
urlFile="urls.txt"

with open(urlFile) as fp:
    url=fp.readline()
    while url:
        webbrowser.get(chrome_app).open(url)

        pyautogui.moveTo(x=200,y=200,duration=4.0)
        pyautogui.hscroll(-1500)
        pyautogui.moveTo(x=300,y=300,duration=1.5)

        k=0
        ok=0
        while ok == 0 and k != 6:
            screenshot=pyautogui.screenshot()
            graySS=screenshot.convert("L")                          #screenshot turned to greyscale
            bwSS=graySS.point(lambda x: 0 if x<255 else 255, '1')   #greyscale turned to black and white image, threshold applied
            #bwSS.save("an"+str(k)+".png" # uncomment this to check image if doubts
            k+=1
            pattern=Image.open("clapThresholded.png")

            box = pyautogui.locate(pattern,bwSS,confidence=0.5)
            print(box)
            if box is None:
                pyautogui.moveTo(x=200, y=200, duration=0.5)
                pyautogui.hscroll(-700)
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



