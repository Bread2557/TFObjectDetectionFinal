import os

from step1_init_workspace import paths

if os.name=='nt':
    os.system("pip install wget")
    import wget

if not os.path.exists(os.path.join(paths['APIMODEL_PATH'], 'research', 'object_detection')):
    os.system("git clone https://github.com/tensorflow/models " + paths['APIMODEL_PATH'])

# Install Tensorflow Object Detection
if os.name=='posix':
    os.system("apt-get install protobuf-compiler")
    os.system("cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && cp object_detection/packages/tf2/setup.py . && python -m pip install .")


if os.name=='nt':
    url="https://github.com/protocolbuffers/protobuf/releases/download/v3.15.6/protoc-3.15.6-win64.zip"
    wget.download(url)
    os.system("move protoc-3.15.6-win64.zip " + paths['PROTOC_PATH'])
    os.system("cd " + paths['PROTOC_PATH'] + " && tar -xf protoc-3.15.6-win64.zip")

    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.join(paths['PROTOC_PATH'], 'bin'))

    os.system("cd Tensorflow/models/research && protoc object_detection/protos/*.proto --python_out=. && copy object_detection\\packages\\tf2\\setup.py setup.py && python setup.py build && python setup.py install")
    os.system("cd Tensorflow/models/research/slim && pip install -e . ")

