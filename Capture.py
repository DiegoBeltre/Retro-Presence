import time
import base64

import cv2
import numpy as np

from obsws_python import ReqClient
from PIL import Image
import imagehash

obs = ReqClient(
    host="localhost",
    port=4455,
    password="MLyX8iRrNGbGBWRE"
)

def get_frame():
    response = obs.get_source_screenshot(
        name="PS2 Capture",
        img_format="jpg",
        width=640,
        height=480,
        quality=100
    )

    data = response.image_data.split(",")[1]

    image_bytes = base64.b64decode(data)

    frame = cv2.imdecode(
        np.frombuffer(image_bytes, np.uint8),
        cv2.IMREAD_COLOR
    )

    return frame

def get_frame_hash():
    frame = get_frame()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb)

    p_hash = imagehash.phash(pil_image)
    d_hash = imagehash.dhash(pil_image)

    return p_hash, d_hash 

if __name__ == "__main__":

    while True:

        frame = get_frame()

        print(get_frame_hash())
        print(frame.shape)

        time.sleep(1)
