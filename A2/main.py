import os
from PIL import Image,  UnidentifiedImageError
import numpy as np

# 假设的图像所在根目录，您需要根据自己的文件系统更新这个路径
root_dir = 'trafficsigns_dataset'

def get_image_sizes(root_dir):
    sizes = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith('.png') or file.lower().endswith('.jpg'):
                try:
                    with Image.open(os.path.join(subdir, file)) as img:
                        # 只记录图像的大小
                        sizes.append(img.size)
                except (IOError, UnidentifiedImageError):
                    # 如果图像损坏，就跳过
                    continue
    return sizes

# 获取图像尺寸数据
image_sizes = get_image_sizes(root_dir)

# 计算统计数据
sizes_np = np.array(image_sizes)
min_size = sizes_np.min(axis=0)
max_size = sizes_np.max(axis=0)
mean_size = sizes_np.mean(axis=0)
std_dev_size = sizes_np.std(axis=0)
median_size = np.median(sizes_np, axis=0)

print(min_size, max_size, mean_size, std_dev_size, median_size)

