from flask import Flask, render_template,request,flash,redirect, url_for
from werkzeug.utils import secure_filename
import subprocess
# from your_ml_model import predict_text
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/getrelation')
def getrelation():
    return render_template('getrelation.html')

@app.route('/getrelation', methods=['POST'])
def predict():
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    # Save uploaded file to disk
    file.save('input.txt')
    # Call predict.py script using subprocess
    subprocess.call(['python', 'predict.py', '--input_file', 'input.txt', '--output_file', 'output.txt', '--model_dir', 'atis_model/'])
    # Read output file and extract prediction
    with open('output.txt', 'r') as f:
        prediction = f.readlines()
    return render_template('result.html', prediction=prediction)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)