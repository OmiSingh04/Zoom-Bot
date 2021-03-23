import subprocess
import pyautogui
import time
import pandas as pd  #data analysis?? basically access a csv with data in it -_-
from datetime import datetime

def sign_in(meetingid):
	#this will open the app
	subprocess.call("C:/Users/omisi/AppData/Roaming/Zoom/bin/Zoom.exe")
	time.sleep(5)
	#join_button contains the x and y coords of the location of the button it found by itself somehow.
	join_button = pyautogui.locateCenterOnScreen("join_button.png")
	pyautogui.moveTo(join_button)
	pyautogui.click()
	print("clicked")

	#this part is to write the meeting id after clicking there
	meeting_id = pyautogui.locateCenterOnScreen("meeting_id.png")
	pyautogui.moveTo(meeting_id)
	pyautogui.click()
	
	time.sleep(5)
	pyautogui.write(meetingid)
	print(meetingid)

	#audio connect option press
	time.sleep(5)
	audio_connect = pyautogui.locateCenterOnScreen("audio.png")
	pyautogui.moveTo(audio_connect)
	pyautogui.click()

	#the final join button click
	final_join = pyautogui.locateCenterOnScreen("final_join.png")
	pyautogui.moveTo(final_join)
	pyautogui.click()


sign_in("1111111111")
