import os
import xml.etree.ElementTree as ET

# Directory containing the XML files
directory = 'C:\\Projekte\\Python\\P310TFODTest\\Tensorflow\\workspace\\images\\train'

# Initialize the counters for "softshell" and "hardshell"
softshell_count = 0
hardshell_count = 0

# Loop over all XML files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(directory, filename))
        root = tree.getroot()

        # Loop over all elements in the XML file
        for element in root.iter():
            # Increment the counters if the element text is "softshell" or "hardshell"
            if element.text == 'softshell':
                softshell_count += 1
            elif element.text == 'hardshell':
                hardshell_count += 1

# Print the total number of occurrences of "softshell" and "hardshell"
print('Number of occurrences of "softshell":', softshell_count)
print('Number of occurrences of "hardshell":', hardshell_count)
