import pickle as pkl
import json
import config3
import numpy as np

class MilkQuality():

    def __init__(self, pH, Temprature, Taste, Odor, Fat , Turbidity,Colour) :
        self.pH = pH
        self.Temprature = Temprature
        self.Taste = Taste
        self.Odor = Odor
        self.Fat  = Fat 
        self.Turbidity = Turbidity
        self.Colour = Colour
        return 

    def __load_model(self): # Private Method
        # Load Model File
        with open(config3.MODEL_FILE_PATH, 'rb') as f:
            self.model = pkl.load(f)
            print('self.model >>',self.model)

        # Load Project Data 
        with open(config3.JSON_FILE_PATH,'r') as f:
            self.column_name = json.load( f)
            print("Project Data :",self.column_name)

        # Load Normal Scaler File
        with open(config3.SCALER_PATH, 'rb') as f:
            self.scaler = pkl.load(f)
            print('self.scaler >>',self.scaler)

        # connecting with mongodb

        # import pymongo
        # mongo_client=pymongo.MongoClient("mongodb://localhost:27017")
        # db=mongo_client['medical_data']
        # self.collection=db['user_inputs']


    def get_milk_quality(self): # Public Method
        self.__load_model()

        #self.collection.insert_one({"age":self.age,"Gender":self.gender,"bmi":self.bmi,"children":self.children,"smoker":self.smoker,"region":self.region})

        test_array = np.zeros((1,self.model.n_features_in_))
        test_array[0][0] = self.pH
        test_array[0][1] = self.Temprature
        test_array[0][2] = self.column_name['Taste'][self.Taste]
        test_array[0][3] = self.column_name['Odor'][self.Odor]
        test_array[0][4] = self.column_name['Fat '][self.Fat]
        test_array[0][5] = self.column_name['Turbidity'][self.Turbidity]
        test_array[0][6] = self.Colour

        print("Test Array is :",test_array)
        scaled_test_array = self.scaler.transform(test_array)

        milk_quality =self.model.predict(scaled_test_array)[0]
        print("Milk Quality :", milk_quality )
        return milk_quality 