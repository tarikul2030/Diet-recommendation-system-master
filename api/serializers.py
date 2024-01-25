# api/serializers.py
from rest_framework import serializers


class FitnessInputSerializer(serializers.Serializer):
    step_count = serializers.IntegerField()
    mood = serializers.IntegerField()
    calories_burned = serializers.IntegerField()
    hours_of_sleep = serializers.IntegerField()
    weight_kg = serializers.FloatField()
