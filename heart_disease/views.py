from django.shortcuts import render
import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('staticfiles/data/heartmodel.sav', 'rb'))

# Creating a function for prediction


def heart_disease(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'The person is having heart disease'
    else:
        return 'The person does not have any heart disease'


def heart(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        exang = request.POST.get('exang')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')

        diagnosis = heart_disease(
            [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

        return render(request, 'heart.html', {'diagnosis': diagnosis})

    return render(request, 'heart.html')
