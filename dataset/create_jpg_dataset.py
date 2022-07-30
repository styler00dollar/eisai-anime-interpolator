import os.path
import glob
import os
from tqdm import tqdm
import cv2

number = 0
for name in tqdm(glob.glob("data/*/*")):
    base = int(os.path.split(name)[1][:6])
    two = f"{str(base).zfill(6)}-{str(base+2).zfill(6)}-{str(base+4).zfill(6)}"
    if os.path.split(name)[1] == two:
        im1 = cv2.imread(f"{name}/{str(base).zfill(6)}.png")
        im2 = cv2.imread(f"{name}/{str(base+2).zfill(6)}.png")
        im3 = cv2.imread(f"{name}/{str(base+4).zfill(6)}.png")
        datasetpath = "1" + os.path.split(name)[0]
        os.makedirs(datasetpath + "/" + str(number))
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im1.jpg",
            im1,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im2.jpg",
            im2,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im3.jpg",
            im3,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        number += 1
    else:
        pass

    third = f"{str(base).zfill(6)}-{str(base+3).zfill(6)}-{str(base+6).zfill(6)}"
    if os.path.split(name)[1] == third:
        im1 = cv2.imread(f"{name}/{str(base).zfill(6)}.png")
        im2 = cv2.imread(f"{name}/{str(base+3).zfill(6)}.png")
        im3 = cv2.imread(f"{name}/{str(base+6).zfill(6)}.png")
        datasetpath = "1" + os.path.split(name)[0]
        os.makedirs(datasetpath + "/" + str(number))
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im1.jpg",
            im1,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im2.jpg",
            im2,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        cv2.imwrite(
            datasetpath + "/" + str(number) + "/im3.jpg",
            im3,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100],
        )
        number += 1
    else:
        pass
