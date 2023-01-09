import xml.etree.ElementTree as ET
from pathlib import Path

data_dir = "C:\\Projekte\\Python\\P310TFODTest\\Tensorflow\\workspace\\images\\train"

for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix == ".xml":
        # Parse the XML file
        tree = ET.parse(str(filepath))

        # Get the root element
        root = tree.getroot()

        # Iterate through the 'object' elements
        for obj in root.findall('object'):
            name = obj.find('name').text
            # If the name is 'hardshell', remove the element
            if name == 'softshell':
                root.remove(obj)
                print("Found one")

        # Write the modified XML tree to a file
        tree.write(str(filepath))
        print(str(filepath))
