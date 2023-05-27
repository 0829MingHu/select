import json
import os.path
import shutil

with open('final_annotations.json', 'r') as f:
    data = json.load(f)

src_path = r'/home/chenj0g/2fps25/rgb/feature/all_convert'
dst_path = r'/home/chenj0g/2fps25/rgb/feature/all_select'
txt_path = r'/home/chenj0g/2fps25/rgb/feature'

with open(txt_path, 'w') as txt_file:
    for key, value in data.items():
        url = value['url']
        file_name = url.split('=')[1].split(':')[0] + '.npy'
        # 构造npy文件的路径
        npy_path = os.path.join(src_path, file_name)
        # 判断npy文件是否存在
        if os.path.exists(npy_path):
            # 如果存在，将文件移动到目标文件夹
            shutil.copy(npy_path, dst_path)
            txt_file.write(file_name + '\n')  # 将 file_name 写入 txt 文件中
