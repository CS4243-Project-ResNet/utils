import os
import subprocess

base_path = [
    '/home/t/tianqi/CS4243_proj/baseline/data/train/carrying/',
    '/home/t/tianqi/CS4243_proj/baseline/data/train/threat/',
    '/home/t/tianqi/CS4243_proj/baseline/data/train/normal/',
    '/home/t/tianqi/CS4243_proj/baseline/data/val/carrying/',
    '/home/t/tianqi/CS4243_proj/baseline/data/val/threat/',
    '/home/t/tianqi/CS4243_proj/baseline/data/val/normal/',
]

save_path = [
    '/home/t/tianqi/CS4243_proj/baseline/seg/train/carrying/',
    '/home/t/tianqi/CS4243_proj/baseline/seg/train/threat/',
    '/home/t/tianqi/CS4243_proj/baseline/seg/train/normal/',
    '/home/t/tianqi/CS4243_proj/baseline/seg/val/carrying/',
    '/home/t/tianqi/CS4243_proj/baseline/seg/val/threat/',
    '/home/t/tianqi/CS4243_proj/baseline/seg/val/normal/',
]


for i in range(6):
    files = os.listdir(base_path[i])

    for f in files:
        print(f)
        subprocess.call(
            ['python', 
            '/home/t/tianqi/CS4243_proj/PaddleSeg/contrib/PP-HumanSeg/src/my_seg_demo.py', 
            '--config', 
            '/home/t/tianqi/CS4243_proj/PaddleSeg/contrib/PP-HumanSeg/human_pp_humansegv2_mobile_192x192_inference_model_with_softmax/deploy.yaml',
            '--img_path',
            base_path[i] + f,
            '--save_dir',
            save_path[i] + f
            ])
        

