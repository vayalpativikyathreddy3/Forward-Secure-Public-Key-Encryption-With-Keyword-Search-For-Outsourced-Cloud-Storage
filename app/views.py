from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.core.files.storage import FileSystemStorage
# from .crypto import generate_rsa_keys, encrypt_data, encrypt_keyword, generate_peks_token, search_with_peks
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def datasenderregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        contact = request.POST['contact']
        address = request.POST['address']
        profile = request.FILES['profile']
        
        if DataSenderModel.objects.filter(email=email).exists():
            messages.success(request, 'Email already existed')
            return redirect('datasenderregister')
        else:
            DataSenderModel.objects.create(name=name, email=email, password=password, dob=dob, gender=
                                      gender, contact=contact, address=address, profile=profile).save()
            messages.success(request, 'Registration Successfull')
            return redirect('datasenderregister')
    return render(request, 'datasenderregister.html')

def datasenderlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
       
        # if DataSenderModel.objects.filter(email=email,status='pending').exists(): 
        #     messages.error(request, 'Admin is Not Authorized You') 
        #     return redirect('datasenderlogin')
        if DataSenderModel.objects.filter(email=email, password=password).exists():
            request.session['email']=email
            request.session['login']='sender'
            return redirect('home')
        else:
            messages.success(request, 'Invalid Email or Password')
            return redirect('datasenderlogin')
    return render(request, 'datasenderlogin.html')


def home(request):
    login = request.session['login']
    return render(request, 'home.html',{'login':login})

def logout(request):
    del request.session['email']
    del request.session['login']
    return redirect('index')


def datareceiverregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        contact = request.POST['contact']
        address = request.POST['address']
        profile = request.FILES['profile']
        
        if DataReceiverModel.objects.filter(email=email).exists():
            messages.success(request, 'Email already existed')
            return redirect('datareceiverregister')
        else:
            DataReceiverModel.objects.create(name=name, email=email, password=password, dob=dob, gender=
                                      gender, contact=contact, address=address, profile=profile).save()
            messages.success(request, 'Registration Successfull')
            return redirect('datareceiverregister')
    return render(request, 'datareceiverregister.html')

def datareceiverlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if DataReceiverModel.objects.filter(email=email, password=password).exists():
            request.session['email']=email
            request.session['login']='receiver'
            return redirect('home')
        else:
            messages.success(request, 'Invalid Email or Password')
            return redirect('datareceiverlogin')
    return render(request, 'datareceiverlogin.html')

def cloudlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == "cloud@gmail.com" and password == "cloud":
            request.session['email']=email
            request.session['login']='cloud'
            return redirect('home')
        else:
            messages.success(request, 'Invalid Email or Password')
            return redirect('cloudlogin')
    return render(request, 'cloudlogin.html')


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
from django.http import HttpResponse

# Simplified PEKS encryption and decryption
def peks_encrypt(keyword):
    return base64.b64encode(keyword.encode()).decode()

def peks_decrypt(encrypted_keyword):
    return base64.b64decode(encrypted_keyword.encode()).decode()

# Simplified ABE encryption and decryption
def abe_encrypt(file):
    # Generate a random key for AES encryption
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)   # Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt file content
    file_content = file.read()
    encrypted_content = encryptor.update(file_content) + encryptor.finalize()
    
    # Encode encrypted content and key for storage
    return (base64.b64encode(encrypted_content).decode(), base64.b64encode(key).decode(), base64.b64encode(iv).decode())

def abe_decrypt(encrypted_file, key, iv):
    encrypted_content = base64.b64decode(encrypted_file)
    key = base64.b64decode(key)
    iv = base64.b64decode(iv)
    
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_content = decryptor.update(encrypted_content) + decryptor.finalize()
    return decrypted_content





import hashlib

def hash_string(input_string):
    # Create a new sha256 hash object
    sha_signature = hashlib.sha256()
    
    # Update the hash object with the bytes of the input string
    sha_signature.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal representation of the digest
    return sha_signature.hexdigest()


def uploadfile(request):
    # UploadFileModel.objects.all().delete()
    login = request.session['login']
    if request.method == 'POST':
        file = request.FILES.get('file')
        keyword = request.POST.get('Keyword')
        filename=file.name
        if file and keyword:
            x=hash_string(keyword)
            if UploadFileModel.objects.filter(cdk=x).exists():
                messages.error(request, 'Keyword exists!')
                return redirect('uploadfile')
            
            # Encrypt the keyword using PEKS
            encrypted_keyword = peks_encrypt(keyword)
            print(file)
            # Encrypt the file using ABE
            encrypted_file, key, iv = abe_encrypt(file)
            
            # Save the encrypted file and keyword to the database
            UploadFileModel.objects.create(
                file=file,
                uploaderemail=request.session['email'],
                file_name=filename,
                encrypted_keyword=encrypted_keyword,
                encrypted_data=encrypted_file,
                privatekey=key,
                iv=iv,
                cdk=x

            ).save()
            messages.success(request, 'File uploaded and encrypted successfully.')
            return redirect('uploadfile')
        else:
            return HttpResponse('File or keyword missing.')
    
    return render(request, 'uploadfile.html',{"login":login})

def searchfile(request):
    login = request.session.get('login')
    if request.method == 'POST':
        encrypted_keyword = request.POST.get('Keyword')
        print(encrypted_keyword)
        if encrypted_keyword:
            
            keyword1 = peks_encrypt(encrypted_keyword)
            # keyword = peks_decrypt(keyword1)
     
            files = UploadFileModel.objects.filter(encrypted_keyword=keyword1)
            
            return render(request, 'viewsearchedfiles.html', {'data': files, 'login':login})
        else:
            return HttpResponse('Keyword missing.')
    
    return render(request, 'searchfile.html', {"login": login})

def requestfile(request, id):
    login = request.session.get('login')
    email= request.session['email']
    file_entry = UploadFileModel.objects.get(id=id)
    RequestFileModel.objects.create(
        file=file_entry.file,
        uploaderemail=file_entry.uploaderemail,
        file_name=file_entry.file_name,
        encrypted_keyword=file_entry.encrypted_keyword,
        encrypted_data=file_entry.encrypted_data,
        privatekey=file_entry.privatekey,
        iv=file_entry.iv,
        cdk=file_entry.cdk,
        email=email
        ).save()
    messages.success(request, 'File request sent. The Cloud will process this request.')
    return redirect('searchfile')
   
    

def viewmyfiles(request):
    login = request.session['login']
    email = request.session['email']
   
    data = UploadFileModel.objects.filter(uploaderemail=email)

    return render(request, 'viewmyfiles.html',{'data':data,'login':login})

def viewallfiles(request):
    login = request.session['login']
    data = UploadFileModel.objects.all()
    return render(request, 'viewallfiles.html',{'data':data,'login':login})


def viewrequestedfiles(request):
    login = request.session['login']
    data = RequestFileModel.objects.filter(status='pending')
    return render(request, 'viewfilesrequests.html',{'data':data,'login':login})

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from .models import RequestFileModel  # Replace with your actual model import

def acceptrequestfile(request, id):
    # Get login info (if needed)
    login = request.session.get('login')

    # Fetch the request object
    req = RequestFileModel.objects.get(id=id)
    
    # Decrypt the content (assuming `abe_decrypt` is properly defined elsewhere)
    decrypted_content = abe_decrypt(req.encrypted_data, req.privatekey, req.iv)
    
    # Update the request object
    req.encrypted_data = decrypted_content
    req.status = 'accepted'
    req.save()

    # Email subject and message
    email_subject = 'Key Details'
    email_message = f'Hello {req.email},\n\nWelcome To Our Website!\n\nHere are your Key details:\nEmail: {req.email}\nKey: {req.cdk}\n\nPlease keep this information safe.\n\nBest regards,\nYour Website Team'

    try:
        # Sending email
        send_mail(
            email_subject,
            email_message,
            'appcloud887@gmail.com',  # Your Gmail address
            [req.email],  # Recipient's email
            fail_silently=False  # Set to False to see error messages
        )
    except Exception as e:
        # Handle any exceptions that occur during email sending
        print(f"Error sending email: {e}")

    # Display success message and redirect
    messages.success(request, 'Key Generated Successfully')
    return redirect('viewrequestedfiles')



def viewfiletransactions(request):
    login = request.session['login']
    data = RequestFileModel.objects.filter(status='accepted')
    return render(request, 'viewfiletransactions.html',{'data':data,'login':login})


def viewresponses(request):
    login = request.session['login']
    email =request.session['email']
    data = RequestFileModel.objects.filter(status='accepted',email=email)
    return render(request, 'viewresponses.html',{'data':data,'login':login})

def download(request, id):
    login = request.session['login']
    email = request.session['email']
    context = RequestFileModel.objects.get(id=id)

    if request.method == 'POST':
        key = request.POST['Key']
        if key == context.cdk:
            file_path = context.file.path  # Get the file path
            file_name = context.file_name.split('/')[-1]  # Extract the file name
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=file_name)
            return response
        else:
            messages.success(request, 'You Entered key is Wrong')
            return redirect('download', id)

    return render(request, 'download.html', {'login': login, 'id': id})
