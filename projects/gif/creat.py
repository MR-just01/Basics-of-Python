import imageio.v3 as iio
from PIL import Image
import os

frames = []
SIZE = (400, 400)  # pick ONE size

for file in sorted(os.listdir("images")):
    if file.endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(os.path.join("images", file)).convert("RGB")
        img = img.resize(SIZE)
        frames.append(img)

iio.imwrite(
    "test.gif",
    frames,
    duration=0.5,  # seconds (imageio uses seconds, not ms)
    loop=0
)

print("GIF created successfully")
