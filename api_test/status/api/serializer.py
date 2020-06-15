from rest_framework import serializers

from status.models import Status
'''
Serializers -> Json 
Serializers -> validate data 
'''

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]


