from PIL import Image
import time, shutil
from pathlib import Path

# dir(Image)

def imgSmush(importPic, qual):
    img = str(Path("uploads/"+importPic))
    print(img)
    picture = Image.open(img)
    picture.save(f"static/compressed/compressed{qual}{importPic}", optimize=True,quality=qual)
    shutil.move(img, f'static/originials/{importPic}')