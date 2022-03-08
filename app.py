from flask import Flask, request, jsonify,render_template
from flask_cors import cross_origin
import pickle,joblib

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/App',methods=['POST','GET'])
@cross_origin()
def page():
    if request.method == 'POST':
        try:
            ZN = float(request.form['ZN'])
            INDUS = float(request.form['INDUS'])
            CHAS = float(request.form['CHAS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            AGE = float(request.form['AGE'])
            DIS = float(request.form['DIS'])
            PTRATIO = float(request.form['PTRATIO'])
            B = float(request.form['B'])
            LSTAT = float(request.form['LSTAT'])

            # load file
            filename = 'Boston_model.pickle'
            load_file = joblib.load(open(filename, 'rb'))

            Prediction = load_file.predict([[ZN,INDUS,CHAS,NOX,RM,AGE,DIS,PTRATIO,B,LSTAT]])

            return render_template('results.html',Prediction=Prediction[0].round(2))
        except Exception as e:
            print('The Exception message is: ', e)
            return render_template('error: Something is wrong')




if __name__ =='__main__':
    app.run(debug=True)