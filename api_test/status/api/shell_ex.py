from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializer import StatusSerializer
from status.models import Status

'''
Serialize a single object
'''
obj = Status.object.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream      = BytesIO(json_data)
data        = JSONParser().parse(stream)
print(data)

'''
Serializer a queryset
'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs,many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2     = BytesIO(json_data2)
data2       = JSONParser().parse(stream2)
print(data2)

'''
Create obj
'''
data = {'user':1}
serializer = StatusSerializer(data=data)
serializer.is_valid()
serializer.save()


'''
Update 
'''
obj = Status.objects.first()
data = {'content':'update new content','user':1}
update_serializer = StatusSerializer(obj,data=data)
update_serializer.is_valid()
update_serializer.save()

'''
Delete 
'''
obj = Status.objects.last()
get_data = StatusSerializer(obj)
print(get_data.data)
obj.delete() # delete 
