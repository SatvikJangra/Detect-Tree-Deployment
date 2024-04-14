from flask import Flask, render_template, request
import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# define the flask app
app = Flask(__name__)

# load the model
model = load_model(r'models\model2.h5')


def model_predict(img_path, model):
    # print("HELLO")
    test_image = image.load_img(img_path, target_size=(224, 224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    test_image = np.vstack([test_image])
    result = model.predict(test_image)
    return result


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # get the file from post request
        f = request.files['file']

        # save the file to uploads folder
        basepath = os.path.dirname(os.path.realpath('_file_'))
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        result = model_predict(file_path, model)

        categories = ["It is not a Tree", "It is a Tree"]

        # process your result for human

        pred_class = int(result)

        output = categories[pred_class]
        return output
    return None


if __name__ == '__main__':
    app.run(debug=False, port=5926)


