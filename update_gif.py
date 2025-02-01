from PIL import Image

# Paths to your existing GIF and new image
gif_path = '/Downloads/day-25-us-states-game-start/blank_states_img.gif'
new_image_path ='/home/kambalapallysirivennela/PycharmProjects/Us States Game/blank_states_img.gif'

gif = Image.open(gif_path)


# Open the new image
new_image =Image.open(new_image_path)

# Create a list of frames to append to the GIF
frames = [gif.copy()]  # Start with the original GIF's frame

# Add the new image as a new frame
frames.append(new_image)

# Save the new GIF
frames[0].save('path/to/save/updated_image.gif',  # Replace with the desired output path
               save_all=True,
               append_images=frames[1:],
               loop=0)  # Set loop to 0 for infinite loop

print("GIF updated successfully!")
