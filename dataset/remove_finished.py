import os.path
import glob
import os

for name in glob.glob("data/*"):
    print(os.path.split(name)[1])
    try:
        os.remove("/workspace/tensorrt/data/" + os.path.split(name)[1])
    except:
        print("not found")
