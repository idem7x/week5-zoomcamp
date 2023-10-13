import pickle

with open('model1.bin', 'rb') as f_model:
    model = pickle.load(f_model)

with open('dv.bin', 'rb') as f_dv:
    dv = pickle.load(f_dv)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([client])
result = model.predict_proba(X)[0, 1]
rounded_result = round(result, 3)
print(rounded_result)
