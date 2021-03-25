from rest_framework import serializers
from polls.models import Subject, Teacher, User


class SubjectSerializer(serializers.Serializer):
    class Meta:
        model = Subject
        fields = '__all__'
