import os
import cv2
import tqdm

def img2video(img_root, video_ouput):
    img_root = 'model/trial_lc_128_ave/results/imgs_talk_finance'
    video_ouput = 'model/trial_lc_128_ave/results/lc_128_talk_finance_2.mp4'
    fps = 25
    # encoder, vert important, need to understand
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(video_ouput, fourcc, fps, (512, 512))                     
    imgnames = os.listdir(img_root)
    imgnames.sort(key=lambda x: int(int(x.split('_')[2])))
    print("\nstart converting")
    for imgname in tqdm.tqdm(imgnames):
        frame = cv2.imread(img_root + '/' + imgname)
        videoWriter.write(frame)
    videoWriter.release()
    print("converted")

if __name__ == '__main__':
    img2video('','')