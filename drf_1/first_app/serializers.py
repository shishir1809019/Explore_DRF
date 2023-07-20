from rest_framework import serializers
from . import models

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'
        
        
class StudentSerializers(serializers.ModelSerializer):
    # course = CourseSerializers(many=True, read_only=True)
    course = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='course_details'
    )
    # course = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.StudentData
        fields = '__all__'