import os
from PIL import Image
import imagehash

folder = 'F:\\DW\\ig_bilder_koffer'  # the folder containing the images
cutoff = 5  # maximum bits that could be different between the hashes

# get a list of all the image files in the folder
filenames = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.jpg') or f.endswith('.jpeg')]

# iterate over all pairs of images
for i, filename1 in enumerate(filenames):
  for filename2 in filenames[i+1:]:
    # compute the hashes for the images
    hash1 = imagehash.average_hash(Image.open(filename1))
    hash2 = imagehash.average_hash(Image.open(filename2))

    # compare the hashes
    if hash1 - hash2 < cutoff:
      print(f'images {filename1} and {filename2} are similar')

#else:
#print(f'images {filename1} and {filename2} are not similar')
