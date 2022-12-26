import os

os.system("pip install pyqt5 lxml")

labels = ['Koffer']
number_imgs = 55

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

if not os.path.exists(IMAGES_PATH):
    if os.name == 'posix':
        os.system("mkdir -p " + IMAGES_PATH)
    if os.name == 'nt':
        os.system("mkdir " + IMAGES_PATH)
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    if not os.path.exists(path):
        os.system("mkdir " + path)

LABELIMG_PATH = os.path.join('Tensorflow', 'labelimg')

if not os.path.exists(LABELIMG_PATH):
    os.system("mkdir " + LABELIMG_PATH)
    os.system("git clone https://github.com/tzutalin/labelImg " + LABELIMG_PATH)

if os.name == 'posix':
    os.system("brew install qt qt5") # Für mac evtl relevant
    os.system("cd Tensorflow && cd labelimg && make qt5py3")
if os.name =='nt':
    os.system("cd {LABELIMG_PATH} && pyrcc5 -o libs/resources.py resources.qrc".format(LABELIMG_PATH=LABELIMG_PATH))

os.system("cd {LABELIMG_PATH} && python labelImg.py".format(LABELIMG_PATH=LABELIMG_PATH))
