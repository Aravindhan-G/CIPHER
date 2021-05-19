# CIPHER
## A Social Media Simulation implemented using Django Framework in Python and MySQL as Backend.</br>

## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Install MySQL
Install ```mysql-8.0.15```. Follow the steps form the below reference document based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)
#### 3. Setup virtual environment
```bash
# Install virtual environment
pip install virtualenvwrapper -win

# Make a virtual environment
mkvirtualenv environmentname

# Activate virtual environment
workon environmentname

# Deactivate virtual environment
deactivate
```

#### 4. Clone git repository
```bash
git clone "https://github.com/Aravindhan-G/cipher.git"
```

#### 5. Install requirements
```bash
cd cipher/
pip install -r requirements.txt
```

#### 6. Create database and tables
```bash
# Open MySQL commandline
# Create database
create database cipher
```

#### 7. Edit project settings
```bash
# open settings file
 cipher/settings.py

# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cipher',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}

# save the file
```
#### 8. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py sqlmigrate login 0001

# Collect static folder into assets
python manage.py collectstatic

# Run the server
python manage.py runserver

```
Try opening [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in the browser.
Now you are good to go.

### 8. URLs
#### Login: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
![](https://github.com/Aravindhan-G/cipher/blob/master/Screenshots/Login.png)
#### Signup: [http://127.0.0.1:8000/signup](http://127.0.0.1:8000//signup)
![](https://github.com/Aravindhan-G/cipher/blob/master/Screenshots/Sign%20Up.png)
