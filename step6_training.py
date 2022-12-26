import os
import sys

from step1_init_workspace import paths, files, TRAINING_SCRIPT

eval = True

BASE = 289000
INTERVAL = 2000

steps = int(sys.argv[1])

print("Starting Training with {} steps to {}".format(steps*INTERVAL, BASE + steps*INTERVAL))

for i in range(1, steps + 1):
    command = "python {} --model_dir={} --pipeline_config_path={} --num_train_steps={}"\
        .format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'], files['PIPELINE_CONFIG'], BASE + (i * INTERVAL))
    print(command)
    os.system(command)

    folder_name = str(BASE + (i * INTERVAL)) + "_" + str(os.urandom(4).hex())
    os.system("mkdir {}".format(os.path.join(paths['BACKUP_PATH'], folder_name)))
    os.system("copy {} {}".format(paths['CHECKPOINT_PATH'], os.path.join(paths['BACKUP_PATH'], folder_name)))
    print("Backup complete, folder name: {}".format(folder_name))

print("Base steps: " + str(BASE + (steps * INTERVAL)))

if eval:
    print("\n\n\n\n ---------------------------------- EVAL ---------------------------------- \n\n\n\n")
    command = "python {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}"\
        .format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'], files['PIPELINE_CONFIG'], paths['CHECKPOINT_PATH'])
    print(command)
    os.system(command)
