Project Title: Forward Secure Public Key Encryption with Keyword Search for Outsourced Cloud Storage-

1. Project Overview:
This project was developed as part of my final year engineering project. It provides a secure cloud storage system where files are encrypted before being uploaded, and users can search encrypted files using keywords without revealing the actual data. The project is implemented using Django and demonstrates the concepts of Public Key Encryption with Keyword Search (PEKS) and Key-Policy Attribute-Based Encryption (KP-ABE).

2. Project Modules- 
2.1 Data Sender:

- Register and Login
- Upload files
- Encrypt files before uploading
- View uploaded files

2.2 Data Receiver:

- Register and Login
- Search files using keywords
- Request files from the cloud
- Download approved files using the generated key

2.3 Cloud Server

- Login
- View uploaded files
- Process file requests
- Generate secret keys
- Maintain file transactions

3. Technologies Used-

- Python
- Django
- HTML
- CSS
- Bootstrap
- JavaScript
- SQLite
- Cryptography Library

4. Installation-

Clone the repository
bash
git clone https://github.com/vayalpativikyathreddy3/Forward-Secure-Public-Key-Encryption-With-Keyword-Search-For-Outsourced-Cloud-Storage.git
Move into the project folder
cd Forward-Secure-Public-Key-Encryption-With-Keyword-Search-For-Outsourced-Cloud-Storage
Install the required packages
pip install -r requirements.txt
Run the project
python manage.py runserver
Open your browser
http://127.0.0.1:8000/

5. Project Screenshots-

5.1 Home Page
[Home Page](Images/home-page.png.png)

5.2 About Page
[About Page](Images/about-page.png.png)

5.3 Data Sender Login
[Data Sender Login](Images/datasender-login.png)

5.4 Data Sender Registration
[Data Sender Registration](Images/datasender-register.png)

5.5 Data Receiver Login
[Data Receiver Login](Images/datareceiver-login.png)

5.6 Data Receiver Registration
[Data Receiver Registration](Images/datareceiver-register.png)

5.7 Cloud Login
[Cloud Login](Images/cloud-login.png)

5.8 Upload File
[Upload File](Images/upload-file.png)

5.9 Search File
[Search File](Images/receiver-search-file.png)

5.10 View Uploaded Files
[View Uploaded Files](Images/view-my-files.png)

5.11 Cloud Transactions
[Cloud Transactions](Images/transactions.png)

5.12 View Responses
[View Responses](Images/view-responses.png)

5.13 Cloud View Files
[Cloud View Files](Images/cloud-view-files.png)

6. Future Improvements-

- Improve the user interface.
- Replace SQLite with MySQL or PostgreSQL.
- Implement a stronger Attribute-Based Encryption scheme.
- Add role-based access control.
- Improve cloud-side security.

7.Author: Vikyath Reddy

8.GitHub: https://github.com/vayalpativikyathreddy3
