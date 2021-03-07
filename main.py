import subprocess
import pyautogui
import time
import pandas as pd  #data analysis?? basically access a spreadsheet with data in it -_-
from datetime import datetime

def sign_in(meetingid):
	#this will open the app
	subprocess.call("C:/Users/omisi/AppData/Roaming/Zoom/bin/Zoom.exe")
	time.sleep(5)
	#join_button contains the x and y coords of the location of the button it found by itself somehow.
	join_button = pyautogui.locateCenterOnScreen("C:/Users/omisi/OneDrive/Desktop/Auto_Zoom/join_button.png")
	pyautogui.moveTo(join_button)
	pyautogui.click()
	print("clicked")

	#this part is to write the meeting id after clicking there
	'''meeting_id = pyautogui.locateCenterOnScreen("C:/Users/omisi/OneDrive/Desktop/Auto_Zoom/meeting_id.png")
	pyautogui.moveTo(meeting_id)
	pyautogui.click()'''
	time.sleep(5)
	pyautogui.write(meetingid)
	print(meetingid)

	#audio connect option press
	time.sleep(5)
	audio_connect = pyautogui.locateCenterOnScreen("C:/Users/omisi/OneDrive/Desktop/Auto_Zoom/audio.png")
	pyautogui.moveTo(audio_connect)
	pyautogui.click()

	#the final join button click
	final_join = pyautogui.locateCenterOnScreen("C:/Users/omisi/OneDrive/Desktop/Auto_Zoom/final_join.png")
	pyautogui.moveTo(final_join)
	pyautogui.click()

	

'''
while True:
	now = datetime.now().strftime("%H:%M")
	if now in str(df['timings']):
'''

sign_in("935 630 7847")