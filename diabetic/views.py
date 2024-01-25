from django.shortcuts import render
import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('static/data/diabetic.sav', 'rb'))

# Creating a function for prediction


def diabetic_disease(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'The person is having Diabetes  disease'
    else:
        return 'The person does not have any Diabetes  disease'


def diabetic(request):
    if request.method == 'POST':
        Age = request.POST.get('Age')
        Gender = request.POST.get('Gender')
        Family_Diabetes = request.POST.get('Family_Diabetes')
        highBP = request.POST.get('highBP')
        PhysicallyActive = request.POST.get('PhysicallyActive')
        BMI = request.POST.get('BMI')
        Smoking = request.POST.get('Smoking')
        Alcohol = request.POST.get('Alcohol')
        Sleep = request.POST.get('Sleep')
        SoundSleep = request.POST.get('SoundSleep')
        RegularMedicine = request.POST.get('RegularMedicine')
        JunkFood = request.POST.get('JunkFood')
        Stress = request.POST.get('Stress')
        BPLevel = request.POST.get('BPLevel')
        Pregancies = request.POST.get('Pregancies')
        Pdiabetes = request.POST.get('Pdiabetes')
        UriationFreq = request.POST.get('UriationFreq')

        diagnosis = diabetic_disease(
            [Age, Gender, Family_Diabetes, highBP, PhysicallyActive, BMI, Smoking, Alcohol, Sleep, SoundSleep, RegularMedicine, JunkFood, Stress, BPLevel, Pregancies, Pdiabetes, UriationFreq])

        return render(request, 'diabetic.html', {'diagnosis': diagnosis})

    return render(request, 'diabetic.html')
