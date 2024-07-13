from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()
class Products(models.Model):
    pass

# ALL THE COMMANDS BELOW WILL BE EXECUTED ON THE PYTHON SHELL
#--------------------------------------------------------------
# create a new object : 
# s = <model_name>(<pass the arguments>)
# s.save() -> this will save

# read the object 
# s = <model_name>.objects.all()
# s -> this will print all the data 

# Get by id
# <model_name>.objects.get(id = 1)  -> if id not exists it will throw error
# So to avoid getting error and breaking of the program , we can use 'filter'
# <model_name>.objects.filter(id= 10) -> if that particular id is not present it will print an empty Querryset


# update an object
# x = <model_name>.objects.get(id=1)  //donot use here filter , it will not work while saving .
# x.<any_field_name_of_the_model> = NewValue
# x.save()

# <model_name>.objects.filter(id=1).update(<model_field_name>=NewValue) -> this will also update


# delete an object
# <model_name>.objects.get(id=1).delete()

# delete all data
# <model_name>.objects.all().delete()