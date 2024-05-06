import os
import glob
from ffmpy import FFmpeg
import sys

if __name__ == '__main__':
    digitalHumanName = 'wwj'
    audio_model = 'ave'
    testAudioName = 'beiying'
    test_audio = f'{testAudioName}.wav'
    checkpoints_paths = sorted(glob.glob(os.path.join(f'model/trial_{digitalHumanName}_{audio_model}/checkpoints/', '*.pth')), reverse=True)
    ck_path = checkpoints_paths[0].replace('\\', '/')
    cmd = f'python main.py data/{digitalHumanName} --workspace model/trial_{digitalHumanName}_{audio_model} \
        -O --test --test_train --asr_model {audio_model} --portrait --aud ./demo/{test_audio}'
    os.system(cmd)
    print('cmd processed')