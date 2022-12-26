import os
from PIL import Image

# the folder containing the JFIF images
folder = 'F:\DW\ig_bilder_koffer'

# get a list of all the JFIF image files in the folder
filenames = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.jfif')]

# iterate over the image files
for filename in filenames:
    # open the image file
    with Image.open(filename) as im:
        # convert the image to JPEG format
        im = im.convert('RGB')

        # save the image in JPEG format
        jpeg_filename = os.path.splitext(filename)[0] + '.jpg'
        im.save(jpeg_filename)
        print(f'converted {filename} to {jpeg_filename}')

        # delete the original JFIF image
        os.remove(filename)
        print(f'deleted {filename}')
