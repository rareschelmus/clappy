import random
import pyautogui
import webbrowser
import pyperclip

#uri for your browser
chrome_app='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
print(chrome_app)
urlFile="urlFeeder.txt"
pattern="mediumLink2.png"
urlList=[]
with open("urlFeeder.txt") as fp:
	url=fp.readline()
	while url:
		webbrowser.get(chrome_app).open(url)

		pyautogui.moveTo(x=200,y=200,duration=4.0)
		pyautogui.hscroll(-900)
		pyautogui.moveTo(x=220,y=220,duration=1.5)

		k=0
		f=0
		while k<20:
			box=pyautogui.locateOnScreen(pattern,confidence=0.7)
			print(box)
			if box is None:
				pyautogui.moveTo(x=200,y=200,duration=0.5)
				pyautogui.hscroll(-500)
				pyautogui.moveTo(x=300,y=300,duration=1.0)
				f+=1
				if f==5:
					break
			else:
				f=0
				k+=1
				pyautogui.click(x = box[0],y = box[1], duration= 1.0, button ='right')
				pyautogui.move(50, 155, duration = 0.4)
				pyautogui.click()
				copiedUrl = pyperclip.paste()
				urlList.append(copiedUrl)
				print(urlList)
				pyautogui.moveTo(x=200,y=200,duration=0.5)
				pyautogui.hscroll(-200)
				pyautogui.moveTo(x=220,y=220,duration=0.5)
		url=fp.readline()
