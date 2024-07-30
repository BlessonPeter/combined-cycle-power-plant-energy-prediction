from flask import Flask, render_template, request
import pickle
import numpy as np
 
app = Flask(__name__)

model = pickle.load(open('gradientboostingmodelpowerplant.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
           Temp = float(request.form['Temperature'])
           Temperature=Temp**(1/2)
           Exhaust_Vacuum=float(request.form['Exhaust_Vacuum'])
           Ambient_pressure=float(request.form['Ambient_pressure'])
           Relative_humidity=float(request.form['Relative_humidity'])
           

           prediction=model.predict([[Exhaust_Vacuum,Ambient_pressure,Relative_humidity,Temperature]])
           output=np.round(prediction,2)   #rounded_prediction = np.round(prediction, 2)
           if output<0:
                return render_template('index.html',prediction_texts="Sorry prediction is not possible")
           else:
                return render_template('index.html',prediction_text="The expected Energy Production(In MW) is {} ".format(output))
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)

    
