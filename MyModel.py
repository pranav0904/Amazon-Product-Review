import ktrain
from ktrain import text

class MyModel(object):

    def __init__(self):
        
        model = ktrain.load_predictor('C:/Users/khist/Documents/GitHub/Amazon-Product-Review/my_predictor').model
        preproc = ktrain.load_predictor('C:/Users/khist/Documents/GitHub/Amazon-Product-Review/my_predictor').preproc
        
        self.classifier = ktrain.get_predictor(model, preproc)
        
        print("Model loaded & initialized...")

    def predict(self,X):
        
        result = self.classifier.predict(X)
        sentiments = zip(X, result)
        
        return list(sentiments)
    
model = MyModel()
input_ = ['waste of money', 
        'beautiful as a gift',
        'I use it all day, everyday',
       'Worst product']

print(model.predict(input_))