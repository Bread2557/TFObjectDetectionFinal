import os

from step1_init_workspace import paths, PRETRAINED_MODEL_NAME, PRETRAINED_MODEL_URL

os.system("pip install tensorflow==2.10.0")
os.system("pip install matplotlib")
os.system("pip install pyyaml")
os.system("pip install gin-config")
os.system("pip install tensorflow-addons")
os.system("pip install pycocotools")
os.system("pip install opencv-python")

VERIFICATION_SCRIPT = os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection', 'builders', 'model_builder_tf2_test.py')
# Verify Installation

os.system("python {VERIFICATION_SCRIPT}".format(VERIFICATION_SCRIPT=VERIFICATION_SCRIPT))

os.system("pip uninstall protobuf matplotlib -y")
os.system("pip install protobuf matplotlib==3.5.0rc1")

import object_detection

os.system("pip list")


if os.name == 'posix':
    os.system("wget {PRETRAINED_MODEL_URL}".format(PRETRAINED_MODEL_URL=PRETRAINED_MODEL_URL))
    os.system("mv " + PRETRAINED_MODEL_NAME + '.tar.gz' + " " + paths['PRETRAINED_MODEL_PATH'])
    os.system("cd " + paths['PRETRAINED_MODEL_PATH'] + " && tar -zxvf " + PRETRAINED_MODEL_NAME+'.tar.gz')
if os.name == 'nt':
    import wget
    wget.download(PRETRAINED_MODEL_URL)
    os.system("move " + PRETRAINED_MODEL_NAME+'.tar.gz' + " " + paths['PRETRAINED_MODEL_PATH'])
    os.system("cd " + paths['PRETRAINED_MODEL_PATH'] + " && tar -zxvf " + PRETRAINED_MODEL_NAME+'.tar.gz')

