import os
import glob
from ffmpy import FFmpeg
import sys
from datetime import datetime
if __name__ == '__main__':
    start_time = datetime.now()
    digitalHumanName = ''
    audio_model = 'ave'
    testAudioName = ''
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
        -O --test --test_train --asr_model {audio_model} --portrait --aud {audio_data}'
    if is_write_imgs:
        cmd = cmd + ' --write_image'
    print(cmd)
    os.system(cmd)
    print('cmd processed')
    end_time = datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    print(f"Cost：{elapsed_time} seconds")
    # 6min18s ~ 1763s (image True) ~ 30min
