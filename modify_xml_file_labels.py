import os
import re

# the directory containing the XML files
directory = 'C:\\Projekte\\Python\\P310TFODTest\\Tensorflow\\workspace\\images\\test'

# get a list of all the XML files in the directory
filenames = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.xml')]

# iterate over the XML files
for filename in filenames:
    # read the XML file
    with open(filename, 'r') as f:
        xml = f.read()

    # replace "softshell" and "hardshell" with "Koffer"
    xml = re.sub(r'<name>softshell</name>', '<name>Koffer</name>', xml)
    xml = re.sub(r'<name>hardshell</name>', '<name>Koffer</name>', xml)

    # write the modified XML to the file
    with open(filename, 'w') as f:
        f.write(xml)

    print(f'updated {filename}')
