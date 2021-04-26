from flask import Flask, render_template, request
import joblib
import pandas as pd
app = Flask(__name__)

clf = joblib.load("static/svm_clf.joblib")

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        wbcc = request.form['wbcc']
        bgr = request.form['bgr']
        bu = request.form['bu']
        sc = request.form['sc']
        pcv = request.form['pcv']
        al = request.form['al']
        hem = request.form['hem']
        age = request.form['age']
        sug = request.form['sugar']
        hy = request.form['hy']
        X = [wbcc, bgr, bu, sc, pcv, al, hem, age, sug, hy]
        num_X = []
        for val in X:
            if val == 'low':
                num_X.append(0)
            elif val == 'medium':
                num_X.append(1)
            else:
                num_X.append(2)
        X_df = pd.DataFrame(num_X)
        vals = ['white blood cell count', 'blood glucose random', 'blood urea', 'serum creatinine',
                'packed cell volume', 'albumin', 'hemoglobin', 'age', 'sugar', 'hypertension']
        X_df = X_df.T
        X_df.columns = vals
        pred = (clf.predict(X_df)[0])
        if pred == 1:
            return render_template('result.html', res = 'Cronic Kidney Disease')
        else:
            return render_template('result.html', res='No Disease')
    return render_template('ckd.html')


if __name__ == '__main__':
    app.run()
