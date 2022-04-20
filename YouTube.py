#https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
#import the library. pip install pytube3
from pytube import YouTube

#ask user to enter the link to download
link = input("Enter the link: ")
yt = YouTube(link)

#Revealing Video Information
print("Title: ", yt.title)  #Tittle of Video
print("Number of views: ", yt.views)  #Number of view of video
print("Length of video: ", yt.length)  #Length of the video
print("Description: ", yt.description)  #Description of video
print("Ratings: ", yt.rating)  #Rating

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading....")
ys.download()
print("Download completed! =)")

#videos donwload path: C:\Users\mazev\PycharmProjects\MyProJect