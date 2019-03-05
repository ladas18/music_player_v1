from Tkinter import *

root = Tk()

# image path variables
play_photo = PhotoImage(file = "/Users/lg/Documents/Coding/Python/Music/music_player_2/assets/play.gif")
stop_photo = PhotoImage(file = "/Users/lg/Documents/Coding/Python/Music/music_player_2/assets/stop.gif")
pause_photo = PhotoImage(file = "/Users/lg/Documents/Coding/Python/Music/music_player_2/assets/pause.gif")

# create play
play_btn = Button(root, image = play_photo)
play_btn.grid(row=0, column=0)

# create stop
stop_btn = Button(root, image = stop_photo)
stop_btn.grid(row=1, column=1)

# create pause
pause_btn = Button(root, image = pause_photo)
pause_btn.grid(row=2, column=2)

root.mainloop()
