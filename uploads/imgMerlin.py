from PIL import Image
import time
from pathlib import Path

# dir(Image)

def imgSmush(importPic, qual):
    img = str(Path("uploads/"+importPic))
    print(img)
    time.sleep(2)
    picture = Image.open(img)
    picture.save("static/compressed/compresses"+ qual + importPic ,optimize=True,quality=15) 

