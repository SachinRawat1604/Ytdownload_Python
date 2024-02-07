from tkinter import Canvas, Tk, Label, Entry, Button
from PIL import ImageTk, Image
from pytube import YouTube

def download_video():
    try:
            
        # Prompt user to enter the YouTube video link
        link = link_entry.get()

        # Create a YouTube object with the provided link
        yt = YouTube(link)

        # Print video title and views
        print("Title: ", yt.title)
        title_Label.config(text="Title: "+ yt.title)

        print("View: ", yt.views)
        views_Label.config(text="Views: "+ str(yt.views))

        # Get the highest resolution stream
        yd = yt.streams.get_highest_resolution()

        # Download the video to the specified directory
        yd.download('/Users/sachi/Downloads')

        # Update the status label to indiate successful download
        status_Label.config(text="Download completed Successfully!",font=(20))
    
    except Exception as e:
        #  Update the status label to indiate an error
        status_Label.config(text="An error occur"+ str(e),font=(20))

#create the main application window
root = Tk()
root.title("YouTube Video downloader")

# Set the size of the window
root.geometry("800x600")

# Load the background image
background_image = Image.open("Ytdownload_Python/youtube.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and display the background image
canvas = Canvas(root, width= background_image.width, height= background_image.height)
canvas.pack()
canvas.create_image(0,0, anchor="nw", image= background_photo)

# create labels, entry wiget and button
link_label = Label(root, text="Enter the youtube viedo link:-- ", font=(20),bg="light blue")
link_label.place(relx=0.5, rely=0.2, anchor="center")
link_entry = Entry(root, width=50,font=(20))
link_entry.place(relx=0.5, rely=0.4, anchor="center")

download_button = Button(root, text="Download", command=download_video, font=(20))
download_button.place(relx=0.5, rely=0.6, anchor="center")

title_Label = Label(root, text=" ", font=(14))
title_Label.place(relx=0.5, rely=0.7, anchor="center")

views_Label = Label(root, text=" ", font=(14))
views_Label.place(relx=0.5, rely=0.8, anchor="center")

status_Label = Label(root, text=" ", font=(18))
status_Label.place(relx=0.5, rely=0.9, anchor="center")

# start the Tkinter event loop
root.mainloop()