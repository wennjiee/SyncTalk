import os
import glob
if __name__ == '__main__':
    train_name = 'wwj_2'
    audio_model = 'hubert'
    trial_params = f'trial_{train_name}_{audio_model}'
    cmd0 = f'python data_utils/process.py data/{train_name}/{train_name}.mp4 --asr {audio_model}'
    cmd1 = f'python main.py data/{train_name} --workspace model/{trial_params} -O --iters 90000 --asr_model {audio_model}'
    cmd2 = f'python main.py data/{train_name} --workspace model/{trial_params} -O --iters 160000 --finetune_lips --patch_size 64 --asr_model {audio_model}'
    preprocessed_data = f'data/{train_name}/transforms_train.json'
    if not os.path.exists(preprocessed_data):
        os.system(cmd0)
    print("******************start training head******************")
    os.system(cmd1)
    print("******************finished training head******************")
    print("******************start finetune lips******************")
    os.system(cmd2)
    print("******************finished finetune******************")