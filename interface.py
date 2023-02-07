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
    #try:
    if request.method == 'POST':
        data = request.form.get

        print("User Data is :",data)
        pH = int(data('pH'))
        Temprature = int(data('Temprature'))
        Taste = data('Taste')
        Odor = data('Odor')
        Fat = data('Fat')
        Turbidity = data('Turbidity')
        Colour = int(data('Colour'))


        milk_predict = MilkQuality(pH, Temprature, Taste, Odor, Fat , Turbidity,Colour)
        quality = milk_predict.get_milk_quality()

        # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
        return  render_template('index.html',prediction = quality)

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

        milk_predict = MilkQuality(pH, Temprature, Taste, Odor, Fat , Turbidity,Colour)
        quality = milk_predict.get_milk_quality()

        # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
        return  render_template('index.html',prediction = quality)
        
    # except:
    #     print(traceback.print_exc())
    #     return  jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config3.PORT_NUMBER,debug=True)