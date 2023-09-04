from roboflow import Roboflow
from PIL import Image
import smtplib
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    return render_template('api1.html')

@app.route('/predict' ,methods = ['POST'])
def predict():
    if 'image' in request.files:
        image = request.files['image']
        image.save("your_image.jpg")  # Save the uploaded image

        rf = Roboflow(api_key="z5RFwYOGEiWs6g4JHO85")
        project = rf.workspace().project("aircraft-defects-lm9e3")
        model = project.version(3).model

# infer on a local image
        print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
        prediction_image_path = "prediction.jpg"
        model.predict("your_image.jpg", confidence=40, overlap=30).save('static/'+ prediction_image_path)

# infer on an image hosted elsewhere
#print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
        return render_template('api1.html',Status="SUCCESS",prediction_image_path=prediction_image_path)

@app.route('/form',methods=['POST'])
def inde():
    return render_template('form.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    input_value = request.form.get('input_value')
    message=request.form.get('value1')
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('b210436@skit.ac.in','99426738')
    print(input_value)
    server.sendmail('b210436@skit.ac.in',input_value,message)
    print('mail sent')  
    return render_template('form.html',Status="Mail Send Successfully") 

@app.route('/back',methods=['POST'])
def back():
    return render_template('api1.html')       


'''def see():
    if request.method == 'GET':
        return "heLLo"
    elif request.method == 'POST':
        data = request.form.get('data' , 'No data provided')
        return f"received data from POst is:{data}" '''
    
if __name__=='__main__':
    app.run(debug=True) 

'''rf = Roboflow(api_key="z5RFwYOGEiWs6g4JHO85")
project = rf.workspace().project("aircraft-defects-lm9e3")
model = project.version(3).model

# infer on a local image
print(model.predict("your_image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
#print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())'''