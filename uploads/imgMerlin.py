from PIL import Image
import time
from pathlib import Path

# dir(Image)

def imgSmush(importPic, qual):
    img = str(Path("uploads/"+importPic))
    print(img)
    picture = Image.open(img)
    picture.save(f"static/compressed/compressed{qual}" + importPic ,optimize=True,quality=qual)
    picture.save(f"static/originials/original" + importPic ,optimize=True,quality=100)
