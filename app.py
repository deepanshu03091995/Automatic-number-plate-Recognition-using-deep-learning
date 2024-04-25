import os, shutil
from flask import Flask, render_template,request,Response
from src.ANPR.constants import *
from src.ANPR.pipeline.prediction_pipeline import Optical_character_recognition
import sys
from src.ANPR.exception import ANPRException
from src.ANPR.logger import logging
from src.ANPR.pipeline.training_pipeline import TrainPipeline

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def land():
    return render_template("landing_page.html")

@app.route('/index',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        upload_file =request.files['fileup']
        filename = upload_file.filename

        upload_img_path = os.path.join(os.getcwd(),STATIC_DIR,UPLOAD_SUB_DIR)
        shutil.rmtree(upload_img_path)
        os.makedirs(upload_img_path,exist_ok=True)
        upload_img_path = os.path.join(os.getcwd(),STATIC_DIR,UPLOAD_SUB_DIR,filename)
        upload_file.save(upload_img_path)
        text = Optical_character_recognition(upload_img_path, filename)
        
        return render_template('index.html', upload=True, upload_image=filename, text=text)

    return render_template("index.html")



@app.route("/train",methods=['GET'])
def trainRouteClient():
    try:
        train_obj = TrainPipeline()
        train_obj.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)