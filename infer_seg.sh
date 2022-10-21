#bin/bash

folder=/home/t/tianqi/CS4243_proj/cs4243_smallest_0
save_folder=/home/t/tianqi/CS4243_proj/dataset_seg
for subfolder in $folder/*; do
    for file in $subfolder/*; do
        save_filename=${save_folder}/$(basename ${subfolder})/$(basename ${file})
        echo ${save_filename}
        python /home/t/tianqi/CS4243_proj/PaddleSeg/contrib/PP-HumanSeg/src/seg_demo.py \
            --config /home/t/tianqi/CS4243_proj/PaddleSeg/contrib/PP-HumanSeg/human_pp_humansegv2_mobile_192x192_inference_model_with_softmax/deploy.yaml \
            --img_path ${file} \
            --save_dir ${save_filename}
    done
done
