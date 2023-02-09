from flask import Flask, render_template, jsonify, request
import config3
from utils import MilkQuality
import traceback
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_milk_quality', methods = ['GET','POST'])
def predict_milk_quality():
    try:
        if request.method == 'POST':
            data = request.form.get

            print("User Data is :",data)
            pH = eval(data('pH'))
            Temprature = eval(data('Temprature'))
            Taste = data('Taste')
            Odor = data('Odor')
            Fat = data('Fat')
            Turbidity = data('Turbidity')
            Colour = int(data('Colour'))

            if Temprature>90 or Temprature<34:
                #return  jsonify({"Message" : "enter correct value of Temprature"})
                return  render_template('index.html',prediction2 = 'Enter the Valid Value of Temprature')

            else:

                milk_predict = MilkQuality(pH, Temprature, Taste, Odor, Fat , Turbidity,Colour)
                quality = milk_predict.get_milk_quality()

                #return  jsonify({"Result" : f"quality of milk is: {quality}"})
                return  render_template('index.html',prediction = 'Your quality of milk is '+quality)

        else:
            data = request.args.get
            print("User Data is :",data)

            pH = eval(data('pH'))
            Temprature = eval(data('Temprature'))
            Taste = data('Taste')
            Odor = data('Odor')
            Fat = data('Fat')
            Turbidity = data('Turbidity')
            Colour = int(data('Colour'))

            if Temprature>90 or Temprature<34:
                #return  jsonify({"Message" : "enter correct value of Temprature"})
                return  render_template('index.html',prediction2 = 'Enter the Valid Value of Temprature')

            else:
                milk_predict = MilkQuality(pH, Temprature, Taste, Odor, Fat , Turbidity,Colour)
                quality = milk_predict.get_milk_quality()

            
            
                #return  jsonify({"Result" : f"quality of milk is: {quality}"})
                return  render_template('index.html',prediction = 'Your quality of milk is '+quality)

            

            

            
        
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config3.PORT_NUMBER,debug=True)