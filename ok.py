from PIL import Image
from flask import Flask, url_for, request, render_template
app = Flask(__name__)
# dir(Image)
img = 'layer 2 coloroed and smudged.jpg'
picture = Image.open(img)
picture.save("Compressed_" + img ,optimize=True,quality=15) 

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)