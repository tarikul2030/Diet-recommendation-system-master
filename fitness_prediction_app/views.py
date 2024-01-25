from django.shortcuts import render
import numpy as np
import pickle
from foodrec.settings import BASE_DIR

# Loading the saved model
loaded_model = pickle.load(open('static/data/active1.sav', 'rb'))

# Creating a function for prediction


def fitness_prediction(input_data):
    # Changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'The person is Heavy active'
    elif prediction[0] == 2:
        return 'The person is very Heavy active'
    elif prediction[0] == 3:
        return 'The person is  Light active'
    elif prediction[0] == 4:
        return 'The person is Very Light active'
    else:
        return 'The person is Low  active'


def active(request):
    if request.method == 'POST':
        step_count = request.POST.get('step_count')
        mood = request.POST.get('mood')
        calories_burned = request.POST.get('calories_burned')
        hours_of_sleep = request.POST.get('hours_of_sleep')
        weight_kg = request.POST.get('weight_kg')

        diagnosis = fitness_prediction(
            [step_count, mood, calories_burned, hours_of_sleep, weight_kg])

        return render(request, 'active.html', {'diagnosis': diagnosis})

    return render(request, 'active.html')
