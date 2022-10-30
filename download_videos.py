import pytube
import os
with open("./playlist_url.txt", 'r', encoding='UTF-8') as file:
	for link in file:
		link=link.replace("\n","")
		yt = pytube.YouTube(link)
		stream = yt.streams.get_highest_resolution()
		stream.download()
