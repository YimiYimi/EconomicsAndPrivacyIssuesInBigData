import os
from PIL import Image
# # 图片视频转换
# import cv2
# import torch
# import numpy as np
#
# def ImgToVideo():
#     path = 'input'
#     filelist = os.listdir(path)
#
#     fps = 4  # 视频每秒24帧
#     size = (2048, 1024)  # 需要转为视频的图片的尺寸
#     fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#     video = cv2.VideoWriter('input/input.avi', fourcc, fps, size)
#     # 视频保存在当前目录下
#     for item in filelist:
#         if item.endswith('_gtFine_color.png'):
#             item = path + item
#             # 路径为中文名
#             img = cv2.imdecode(np.fromfile(item, dtype=np.uint8), 1)
#             # 路径为英文名
#             img = cv2.imread(item)
#             video.write(img)
#
#     video.release()
#     cv2.destroyAllWindows()


dirPath = 'input/'
allFile = os.listdir(dirPath)
for i in allFile:
    file = dirPath + i
    img = Image.open(file)
    w, h = img.size

    newWidth = 600
    newHeight = round(newWidth / w * h)

    img = img.resize((newWidth, newHeight), Image.ANTIALIAS)
    img.save('output/%s' % i, optimize=True, quality=85)
