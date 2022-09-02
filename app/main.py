'''importing Flask and other modules'''
from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)

# load the model
model = load("model2.joblib") 


@app.route('/', methods=["GET", "POST"])
def prediction():
    '''
    This will get data from html form and will do prediction.

    Returns
    -------
    html
        html code for render
    '''

    #Age  Sex  BP  Cholesterol  Na_to_K   Drug
    form_items = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']
                
   # form_items = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
   #               'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    data = []
    pred = None
    if request.method == "POST":
        # getting input with name = fname in HTML form
        for item in form_items:
            try:
                temp = request.form.get(item)
                temp = temp.strip()
                temp = float(temp)
                data.append(temp)
            except Exception as ex:
                print(ex)
        print(data)
        pred = model.predict([data])
        '''
        if pred[0] == 0:
            pred = "has no diabetes 👍"
        elif pred[0] == 1:
            pred = "has diabetes 😥"
        '''
    return render_template("home.html", result=pred)


if __name__ == '__main__':
    app.run()
