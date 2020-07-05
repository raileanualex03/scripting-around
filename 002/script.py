
from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler

import os
import json
import time
from pathlib import Path

AUDIO = ["mp3", "mp4", "3gp", "aa", "msv", "wav", "wma", "cda"]
DOCUMENTS = ["doc", "docx", "pdf", "html", "xls", "xlsx", "odx", "ppt", "pptx", "txt"]
EXECUTABLES = ["exe"]
IMAGES = ["jpg", "jfif", "png"]

Dictionary = {
	"Audio":AUDIO,
	"Documents": DOCUMENTS,
	"Executables":EXECUTABLES,
	"Images": IMAGES
}



class MyHandler(FileSystemEventHandler):
	def __init__(self):
		self.ELEMS = ["Audio", "Documents", "Executables", "Images","Other"]
		for elem in self.ELEMS:
			directory = folder_to_track+"/"+elem
			if not os.path.exists(directory):
				os.mkdir(folder_to_track+"/"+elem)



	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
				new_destination = folder_destination
				src = folder_to_track+"/"+filename
				time.sleep(0.1)
				full_name = filename.split('.')
				if len(full_name) == 2:
					name = full_name[0]
					extension = full_name[1]

					for elem in self.ELEMS:
						print(str(full_name) + " " + extension)
						if elem != "Other":
							if extension in Dictionary[elem]:
								try:
									new_destination = folder_destination+"/"+elem+"/"+filename
									os.rename(src, new_destination)
								except:
									continue
						else:
							try:
								new_destination = folder_destination+"/Other/"+filename
								os.rename(src, new_destination)
							except:
								continue

						
folder_to_track =str(os.path.join(Path.home(), "Downloads"))
folder_destination = str(os.path.join(Path.home(), "Downloads"))
event_handler =MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()