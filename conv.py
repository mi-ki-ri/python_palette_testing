from PIL import Image

FILE_PATH = "pink.png"
img_png = Image.open(FILE_PATH)

# RGBAに変換する
img_png = img_png.convert('RGBA')

# RGBAのalpha（透過）を取得する
alpha = img_png.getchannel('A')

# alphaのマスクを取得する
mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

# gifへ変換するために減色する
img_gif = img_png.quantize(colors=256)

# gifにマスクを貼り付ける
img_gif.paste(im=255, mask=mask)

# 透過gifをエクスポートする
img_gif.save(f"{FILE_PATH}.gif", transparency=255)