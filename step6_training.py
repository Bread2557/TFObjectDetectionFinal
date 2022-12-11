import os

from step1_init_workspace import paths, files, TRAINING_SCRIPT

eval = True

command = "python {} --model_dir={} --pipeline_config_path={} --num_train_steps=2000".format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'], files['PIPELINE_CONFIG'])

print(command)

os.system(command)

if eval:
    print("\n\n\n\n ---------------------------------- EVAL ---------------------------------- \n\n\n\n")

    command = "python {} --model_dir={} --pipeline_config_path={} --checkpoint_dir={}".format(TRAINING_SCRIPT, paths['CHECKPOINT_PATH'],files['PIPELINE_CONFIG'], paths['CHECKPOINT_PATH'])

    print(command)

    os.system(command)