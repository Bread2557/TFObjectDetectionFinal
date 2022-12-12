import os
import sys

from step1_init_workspace import paths

train = sys.argv[1] == 'train'

print("Starting Tensorboard " + ("Training" if train else "Evaluation"))

path = os.path.join(paths['CHECKPOINT_PATH'], 'train' if train else 'eval')


os.system("cd {} && python3 -m tensorboard.main --logdir=.".format(path))
