from pytube import YouTube

# Prompt user to enter the YouTube video link
link = input("Enter the YouTube video link: ")

# Create a YouTube object with the provided link
yt = YouTube(link)

# Print video title and views
print("Title: ", yt.title)

print("View: ", yt.views)

# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()

# Download the video to the specified directory
yd.download('/Users/sachi/Downloads')