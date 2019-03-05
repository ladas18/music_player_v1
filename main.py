import os
from Tkinter import *
import tkMessageBox, tkFileDialog, ttk
from ttkthemes import themed_tk as tk
from pygame import mixer
from mutagen.mp3 import MP3
# from PIL import TkImage, Image

# Starting States
muted = FALSE # set mute state to false
paused = FALSE
index = 0
playlist = []

# functions
def add_to_playlist(file):
    global index
    file = os.path.basename(file)
    list_box.insert(index,file)
    playlist.insert(index, file_path)
    # print(playlist)
    index += 1

def del_from_playlist():
    selected_song = list_box.curselection()
    selected_song = int(selected_song[0])
    list_box.delete(selected_song)
    playlist.pop(selected_song)

def browse_file():
    global file_path # allows play_music function to recognize file_path
    file_path = tkFileDialog.askopenfilename()
    add_to_playlist(file_path)
    # print(file_path)

# def show_details(current_song):
#     filelabel['text'] = "Playing - " + os.path.basename(file_path)
#
#     file_data = os.path.splitext(current_song)
#
#     if file_data[1] == '.mp3':
#         audio = MP3(file_path)
#         total_length = audio.info.length
#     else:
#         pass
#         # a = mixer.Sound(file_path)
#         # total_length = a.get_length()
#     mins, secs = divmod(total_length, 60) # divids total_length by 60 and stores in mins and calculates remainder and stores in secs
#     mins = round(mins)
#     secs = round(secs)
#     # # print(mins)
#     # # print(secs)
#     # timeformat =  '{:02d}:{02d}'.format(mins, secs)
#     # # print(timeformat)

def play_music():
    global paused
    if paused: # if paused is true then unpause
        mixer.music.unpause()
        status_bar['text'] = "Playing - " + os.path.basename(file_path)
        paused = FALSE
    else: # else then just play music
        try:
            # stop_music()
            #time.sleep(1)
            selected_song = list_box.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            status_bar['text'] = "Playing - " + os.path.basename(play_it)
            #show_details(play_it)
        except:
            tkMessageBox.showerror('File not found','Could not find a file. Please open a song.')

def stop_music():
    mixer.music.stop()
    status_bar['text'] = "Music Stopped"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    status_bar['text'] = "Music Paused"

def set_vol(val):
    # val is current sound volume number which comes in as a string and must be converted to float
    volume = float(val) / 100 # must divide by 100 to intergrate 0-1 scale from set_volume
    # print(volume)
    mixer.music.set_volume(volume) # 0 - 1; 0, 0.11, 0.55, 0.97, 1

def about_us():
    tkMessageBox.showinfo('About LG Music Player','This is a music player built using Python Tkinter. Created by Ladarius Greene.')

def rewind_music():
    play_music()

def mute_music():
    global muted
    if muted: # if muted is true unmute the music
        mixer.music.set_volume(0.7)
        volume_btn.configure(image=volume_photo)
        scale.set(70)
        muted = FALSE
    else: # else make make true and mute the music
        mixer.music.set_volume(0)
        volume_btn.configure(image=mute_photo)
        scale.set(0)
        muted = TRUE

def on_closing():
    # tkMessageBox.showinfo("Prank", "This is a prank!")
    stop_music()
    root.destroy()

# Initialize Mixer from Pygame
mixer.init()

# creates the window
#root = Tk()
root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
# root.geometry('400x400')
root.title("LG Music Player")
root.iconbitmap(r'assets/music_icon.ico')

# create the menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# create sub menus
sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="Open", command=browse_file)
sub_menu.add_command(label="Exit", command=root.destroy)

sub_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=sub_menu)
sub_menu.add_command(label="About Us", command=about_us)

# # add text to window
# filelabel = Label(root, text= "Let's make some noise!")
# filelabel.pack(pady=10)

# create status bar
status_bar = ttk.Label(root, text="LG Music Player", relief=SUNKEN, anchor=W, font='Times 12 italic')
status_bar.pack(side=BOTTOM, fill = X) # X is for x-axis; fills left to right

# Main Frames
left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=30, pady=20)
right_frame = Frame(root)
right_frame.pack(pady=20)
# Sub Frames
top_frame = Frame(right_frame)
top_frame.pack()
middle_frame = Frame(right_frame)
middle_frame.pack(padx=30, pady=30)
bottom_frame = Frame(right_frame)
bottom_frame.pack()

# Music Time Length Display
lengthlabel = ttk.Label(top_frame, text= "Total length: --:--")
lengthlabel.pack()

# image path variables
play_photo = PhotoImage(file = "assets/play.gif")
stop_photo = PhotoImage(file = "assets/stop.gif")
pause_photo = PhotoImage(file = "assets/pause.gif")
rewind_photo = PhotoImage(file = "assets/rewind.gif")
volume_photo = PhotoImage(file = "assets/volume.gif")
mute_photo = PhotoImage(file = "assets/mute.gif")

# Playlist
list_box = Listbox(left_frame)
list_box.pack()
add_btn = ttk.Button(left_frame, text="+ Add", command=browse_file)
add_btn.pack(side=LEFT)
del_btn = ttk.Button(left_frame, text="- Del", command=del_from_playlist)
del_btn.pack(side=LEFT)

# create play
play_btn = ttk.Button(middle_frame, image = play_photo, command = play_music)
play_btn.grid(row=0, column=0, padx=10)
# play_btn.pack(side=LEFT, padx=10)

# create stop
stop_btn = ttk.Button(middle_frame, image = stop_photo, command = stop_music)
stop_btn.grid(row=0, column=1, padx=10)
# stop_btn.pack(side=LEFT, padx=10)

# create pause
pause_btn = ttk.Button(middle_frame, image = pause_photo, command = pause_music)
pause_btn.grid(row=0, column=2)
# pause_btn.pack(side=LEFT, padx=10)

# create rewind
rewind_btn = ttk.Button(bottom_frame, image = rewind_photo, command = rewind_music)
rewind_btn.grid(row=0, column=0)

# create volume and mute
volume_btn = ttk.Button(bottom_frame, image = volume_photo, command = mute_music)
volume_btn.grid(row=0, column=1)
# mute_btn = Button(bottom_frame, image = mute_photo, command = rewind_music)
# mute_btn.grid(row=0, column=0, padx=10)

# create volume
scale = ttk.Scale(bottom_frame, from_=0,to=100, orient=HORIZONTAL, command = set_vol)
scale.set(70) # default volume pt1
mixer.music.set_volume(0.7) # default volume pt2
scale.grid(row=0, column=2, pady=15, padx=30)

# Event binding the close window button
root.protocol("WM_DELETE_WINDOW", on_closing)

# keeps the window persistant
root.mainloop()
