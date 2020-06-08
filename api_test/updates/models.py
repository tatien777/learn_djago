import json 

from django.conf import settings
from django.db import models
from django.core.serializers import serialize 

def upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)
# Create your models here.
list_fields = ('user','content','image','id')

class UpdateQuerySet(models.QuerySet):
    # def serialize(self): 
    #     qs = self
    #     return  serialize('json',qs,fields=list_fields) ## array dictionary data [{data,"fields"}]

    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         final_array.append(obj.serialize())
    #     return final_array            ##  dict data {"fields"}

    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         struct = json.loads(obj.serialize())
    #         print("stuct",struct)
    #         final_array.append(struct)
    #     return json.dumps(final_array) # array dict better [{"field0":},{"field1":}]

    def serialize(self):
        list_values = list(self.values('user','content','image','id'))
        return json.dumps(list_values) # the same with above way but shortly 

class UpdateManage(models.Manager):
    def get_querySet(self):
        return UpdateQuerySet(self.model,using=self._db)

class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING)
    content     = models.TextField()
    image       = models.ImageField(upload_to="")
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects     = UpdateManage()
    def __str__(self):
        return self.content or ""
    def serialize(self):
        # json_data = serialize("json",[self],fields=list_fields)
        # struct = json.loads(json_data)
        # print(struct)
        # data = json.dumps(struct[0]['fields'])
        # return data
        print("print self ",self.image.url)
        try:
            image = self.image.url
        except:
            image = ""
        # image = self.image
        data = {
            'id':self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image,
        }
        json_data = json.dumps(data)
        return  json_data