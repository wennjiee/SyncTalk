import os
import glob
from ffmpy import FFmpeg
import sys

if __name__ == '__main__':
    digitalHumanName = 'wwj_2'
    audio_model = 'hubert'
    testAudioName = 'test'
    test_audio = f'{testAudioName}.wav'
    is_write_imgs = False
    checkpoints_paths = sorted(glob.glob(os.path.join(f'model/trial_{digitalHumanName}_{audio_model}/checkpoints/', '*.pth')), reverse=True)
    ck_path = checkpoints_paths[0].replace('\\', '/')
    audio_data = f'demo/{test_audio}'
    if audio_model == 'hubert':
        hubert_data = f'demo/{testAudioName}_hu.npy'
        if not os.path.exists(hubert_data):
            cmd0 = f'python data_utils/hubert.py --wav {audio_data}'
            os.system(cmd0)
    cmd = f'python main.py data/{digitalHumanName} --workspace model/trial_{digitalHumanName}_{audio_model} \
        -O --test --test_train --asr_model {audio_model} --portrait --aud {audio_data} --write_image {is_write_imgs}'
    os.system(cmd)
    print('cmd processed')