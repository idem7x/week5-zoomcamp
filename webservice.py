import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open('model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)

with open('dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

app = Flask('credit')

@app.route('/predict', methods=["POST"])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
       'score': float(y_pred)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
