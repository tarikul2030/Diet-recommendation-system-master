from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FitnessInputSerializer
from django.shortcuts import get_object_or_404
import numpy as np
import pickle
from foodrec.settings import BASE_DIR

# Loading the saved model
loaded_model = pickle.load(open('staticfiles/data/active1.sav', 'rb'))


class FitnessPredictionAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FitnessInputSerializer(data=request.data)
        if serializer.is_valid():
            input_data = [
                serializer.validated_data['step_count'],
                serializer.validated_data['mood'],
                serializer.validated_data['calories_burned'],
                serializer.validated_data['hours_of_sleep'],
                serializer.validated_data['weight_kg']
            ]

            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

            prediction = loaded_model.predict(input_data_reshaped)

            if prediction[0] == 1:
                result = 'The person is Heavy active'
            elif prediction[0] == 2:
                result = 'The person is very Heavy active'
            elif prediction[0] == 3:
                result = 'The person is Light active'
            elif prediction[0] == 4:
                result = 'The person is Very Light active'
            else:
                result = 'The person is Low active'

            return Response({'diagnosis': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
