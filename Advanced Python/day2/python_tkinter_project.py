import tkinter as tk
# from tkinter import messagebox
import random
# print(dir(tk))
# print(help(tk))

# def show_about_us():  # this is the function to show the about us
#     about_text="our company profile"
#     messagebox.showinfo("About us",about_text) 

# root=tk.Tk() # this is the main window of the tkinter
# root.title("About Us") # this is the title of the window
# root.geometry("400x400")  # this is the size of the window
# button=tk.Button(root,text="About us",command=show_about_us) # this is the button to show the about us
# button.pack() # this is the pack method to show the button


# this is the code to create the grid of the tiles
area_width = 800
area_height = 600
tile_width = 100
tile_height = 100

num_tiles_x = 800 // 100
num_tiles_y = 600 // 100 

# # Create the main window
# root = tk.Tk()
# root.title("Tile Grid")
# root.geometry(f"{area_width}x{area_height}")

# # Create a canvas to draw the tiles
# canvas = tk.Canvas(root, width=area_width, height=area_height)
# canvas.pack()

# # Function to handle tile click event
# def on_tile_click(event):
#     random_number = random.randint(1, 100)
#     # Find the tile's top-left corner
#     x1 = (event.x // tile_width) * tile_width
#     y1 = (event.y // tile_height) * tile_height
#     # Find the center of the tile
#     x_center = x1 + tile_width // 2
#     y_center = y1 + tile_height // 2
#     # Display the random number at the center of the tile
#     canvas.create_text(x_center, y_center, text=str(random_number), fill="red", font=('Helvetica', 16))

# # Loop through rows and columns to create tiles
# for row in range(num_tiles_y):
#     for col in range(num_tiles_x):
#         x_position = col * tile_width
#         y_position = row * tile_height
#         tile = canvas.create_rectangle(x_position, y_position, x_position + tile_width, y_position + tile_height, fill="lightblue", outline="black")
#         canvas.tag_bind(tile, "<Button-1>", on_tile_click)  # Bind left mouse click to the tile

# # Run the application
# # root.mainloop()s
    
# root.mainloop()  # this is the main loop of the tkinter 

# Create the main window
root = tk.Tk()
root.title("Tile Grid")
root.geometry(f"{area_width}x{area_height}")

# Create a canvas to draw the tiles
canvas = tk.Canvas(root, width=area_width, height=area_height)
canvas.pack()

# Function to handle tile click event
def on_tile_click(event):
    random_number = random.randint(1, 100)
    # Find the tile's top-left corner
    x1 = (event.x // tile_width) * tile_width
    y1 = (event.y // tile_height) * tile_height
    # Find the center of the tile
    x_center = x1 + tile_width // 2
    y_center = y1 + tile_height // 2
    # Change the tile color and display the random number at the center
    tile_id = canvas.find_closest(event.x, event.y)[0]
    canvas.itemconfig(tile_id, fill="lightgreen")
    canvas.create_text(x_center, y_center, text=str(random_number), fill="blue", font=('Helvetica', 16, 'bold'))

# Loop through rows and columns to create tiles
for row in range(num_tiles_y):
    for col in range(num_tiles_x):
        x_position = col * tile_width
        y_position = row * tile_height
        tile = canvas.create_rectangle(x_position, y_position, x_position + tile_width, y_position + tile_height, fill="lightblue", outline="white")
        canvas.tag_bind(tile, "<Button-1>", on_tile_click)  # Bind left mouse click to the tile

# Run the application
root.mainloop()