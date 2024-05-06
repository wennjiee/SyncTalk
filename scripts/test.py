import os
if __name__ == '__main__':
    # test on the test split
    train_name = 'wwj_half'
    audio_model = 'ave'
    trial_params = f'trial_{train_name}_{audio_model}'
    print("******************start testing******************")
    cmd = f'python main.py data/{train_name} --workspace model/{trial_params} -O --test --asr_model {audio_model} --portrait' 
    os.system(cmd)
    print("******************finished testing******************")