"""
Stuff for Youtube video hosting
"""

import re


def embed_url(video_url):
	"""
	desc: Convert video_url like 
	http://www.youtube.com/watch?v=xxxxxxxxxxx or http://youtu.be/xxxxxxxxxxx 
	to https://www.youtube.com/embed/xxxxxxxxxxxx
	"""
	regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"
	return re.sub(regex, r"https://www.youtube.com/embed/\1",video_url)



print(embed_url('https://youtu.be/vo7caiIyta8'))