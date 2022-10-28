from array import array
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2

# 減色処理


def sub_color(src, K):
    # 次元数を1落とす
    Z = src.reshape((-1, 3))

    # float32型に変換
    Z = np.float32(Z)

    # 基準の定義
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # K-means法で減色
    ret, label, center = cv2.kmeans(
        Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # UINT8に変換
    center = np.uint8(center)

    res = center[label.flatten()]

    # 配列の次元数と入力画像と同じに戻す
    return res.reshape((src.shape))


# FILE_PATH = "pink.png"
FILE_PATH = "kirby.png"

# 入力画像を取得
img = cv2.imread(f"{FILE_PATH}")

# 減色処理(三値化)
dst = sub_color(img, K=8)
cv2.imwrite(f"{FILE_PATH}.tmp.png", dst)

pil_img = Image.open(f"{FILE_PATH}.tmp.png")


# RGBAに変換する
img_png = pil_img.convert('RGBA')

# RGBAのalpha（透過）を取得する
# alpha = img_png.getchannel('A')

# alphaのマスクを取得する
# mask = Image.eval(alpha, lambda a: 255 if a <= 128 else 0)

# gifへ変換するために減色する
img_gif = img_png.quantize(colors=8)

# gifにマスクを貼り付ける
# img_gif.paste(im=255, mask=mask)


# カラーパレットを取り出す
palette = img_gif.getpalette()


# リストの値は index=0 から順番に [R, G, B, R, G, B, ...]のフラットな配列なので[R, G, B]単位にreshape
palette = np.array(palette).reshape(-1, 3)

print(palette)

with open("palette.tmp.json", mode="w") as f:
    for color in palette:
        f.write(f"{str(color.tolist())},")

img_gif.save(f"{FILE_PATH}.tmp.gif")
