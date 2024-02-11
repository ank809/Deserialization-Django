from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=20)
#     age=serializers.IntegerField()
#     city=serializers.CharField(max_length=30)
#     rno=serializers.IntegerField()

#     def create(self, validated_data):
#        return Student.objects.create(**validated_data)


# OR
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['name','age','city','rno']

    def create(self, validated_data):
       return Student.objects.create(**validated_data)