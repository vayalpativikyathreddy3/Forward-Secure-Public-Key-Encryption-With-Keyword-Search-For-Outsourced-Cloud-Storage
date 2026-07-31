from django.db import models
import os

# Create your models here.
class DataSenderModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    profile = models.FileField(upload_to=os.path.join('static', 'datasenderprofiles'))
    status = models.CharField(max_length=100,default='pending',null=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "DataSenderModel"



class DataReceiverModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    profile = models.FileField(upload_to=os.path.join('static', 'datareceiverprofiles'))
    status = models.CharField(max_length=100,default='pending',null=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "DataReceiverModel"


class UploadFileModel(models.Model):
    file = models.FileField(upload_to=os.path.join('static', 'Files'),null=True)
    uploaderemail = models.EmailField()
    file_name = models.CharField(max_length=255)  # Store the original file name
    encrypted_data = models.TextField()  # Store the encrypted file content
    encrypted_keyword = models.CharField(max_length=255)  # Store the encrypted keyword
    privatekey = models.TextField(max_length=255, null=True)  # Store optional attributes (for ABE)
    iv = models.TextField(max_length=255, null=True)
    cdk=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.file_name
    
    class Meta:
        db_table = "UploadFileModel"

class RequestFileModel(models.Model):
    email = models.EmailField()
    file = models.FileField(upload_to=os.path.join('static', 'ReqFiles'),null=True)
    uploaderemail = models.EmailField()
    file_name = models.CharField(max_length=255)  
    encrypted_data = models.TextField()  
    encrypted_keyword = models.CharField(max_length=255)  
    privatekey = models.TextField(max_length=255, null=True)  
    iv = models.TextField(max_length=255, null=True)
    cdk=models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=100,default='pending',null=True)
    def __str__(self):
        return self.file_name
    
    class Meta:
        db_table = "RequestFileModel"
