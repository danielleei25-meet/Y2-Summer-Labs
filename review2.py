def create_youtube_video(title,description):
	video = ("Title": title, "description": description, "likes": 0, "dislikes": 0,
	 "comment": {})
	return video

def like(video):
	if "like" in video:
		video["likes"]+=1
	return video

def commnets_adds(theyoutubevideo,username,textofuser)
	theyoutubevideo["comments"][username]=textofuser
	return theyoutubevideo

def dislike(video):
	if "dislike" in video:
		video["dislike"]+=1
	return video

video=create_youtube_video("product review", "makeup brands")
commnets_adds(video, "Danielle", "very good review may purchase later!")


for i in range (496):
	like(video)
	dislike(video)
print (video) 