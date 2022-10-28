from array import array
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import json


FILE_PATH = "kirby.png"

img_gif = Image.open(f"{FILE_PATH}.tmp.gif")

# RGBAに変換する
# img_png = pil_img.convert('RGBA')

# # RGBAのalpha（透過）を取得する
# alpha = img_png.getchannel('A')

# # alphaのマスクを取得する
# mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

# # gifへ変換するために減色する
# img_gif = pil_img.quantize(colors=8)

# # gifにマスクを貼り付ける
# img_gif.paste(im=255, mask=mask)

with open("palette.tmp.json", mode="r") as f:
    palette_string = f.read()
    palette = json.loads(f"[{palette_string[:-1]}]")

    # print(palette)

    palette = [np.array(color) for color in palette]
    palette = np.array(palette)
    # print(palette)

    palette = palette.reshape(1, -1)[0].tolist()

    print(palette)

    print(img_gif.getpalette())

    img_gif.putpalette(palette)

    img_gif.save(f"{FILE_PATH}_fin.gif", format="gif")
