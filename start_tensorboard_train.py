import os

from step1_init_workspace import paths

train = True

path = os.path.join(paths['CHECKPOINT_PATH'], 'train' if train else 'eval')


os.system("cd {} && python3 -m tensorboard.main --logdir=.".format(path))
