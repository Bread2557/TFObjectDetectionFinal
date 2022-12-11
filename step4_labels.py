import os

from step1_init_workspace import files, paths, PRETRAINED_MODEL_NAME

labels = [{'name':'Koffer', 'id':1}]

os.system("pip install pytz")
os.system("pip install protobuf==3.20.0")

with open(files['LABELMAP'], 'w') as f:
    for label in labels:
        f.write('item { \n')
        f.write('\tname:\'{}\'\n'.format(label['name']))
        f.write('\tid:{}\n'.format(label['id']))
        f.write('}\n')

ARCHIVE_FILES = os.path.join(paths['IMAGE_PATH'], 'archive.tar.gz')
if os.path.exists(ARCHIVE_FILES):
  os.system("tar -zxvf {ARCHIVE_FILES}".format(ARCHIVE_FILES=ARCHIVE_FILES))

if not os.path.exists(files['TF_RECORD_SCRIPT']):
    os.system("git clone https://github.com/nicknochnack/GenerateTFRecord " + paths['SCRIPTS_PATH'])

os.system("python " + files['TF_RECORD_SCRIPT'] + " -x " + os.path.join(paths['IMAGE_PATH'], 'train') + " -l " + files['LABELMAP'] + " -o " + os.path.join(paths['ANNOTATION_PATH'], 'train.record'))
os.system("python " + files['TF_RECORD_SCRIPT'] + " -x " + os.path.join(paths['IMAGE_PATH'], 'test') + " -l " + files['LABELMAP'] + " -o " + os.path.join(paths['ANNOTATION_PATH'], 'test.record'))