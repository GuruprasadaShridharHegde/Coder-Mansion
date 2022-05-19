from pytube import YouTube
video_link = 'https://www.youtube.com/watch?v=fieYJi54t6k'
video = YouTube(video_link)
video.streams.filter(res='144p').first().download('E:\Github\Coder Mansion')
