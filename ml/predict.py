from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)

model = joblib.load('taximodel.joblib')

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    
    prediction = model.predict(data)

    response = {'prediction': prediction}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
