from pytube import YouTube

# Ask user for the YouTube video URL
link = input("Enter URL of Video: ")

# Create a YouTube object with the URL
video = YouTube(link)

# Get the highest resolution stream available
stream = video.streams.get_highest_resolution()

# Download the video
stream.download()

print("Video downloaded successfully!")
