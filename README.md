# Skype school

Template is got here: www.htmlpreviews.com/cloud/education/inition7/index.html

What do you need to have a workspace:
- PC or notebook with windows 7-8
- repository with Python Django project

Steps to deploy:

1. Install cygwin with packages:(python2.7/python-paramiko/python-crypto/gcc/wget/openssh)

2. Install git from site: https://git-scm.com/downloads

3. Download your repository in folder with work:
git clone https://github.com/OleksandrKara/skype_school.git

4. Install easy_install and pip:
wget https://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11-py2.7.egg#md5=fe1f997bc722265116870bc7919059ea
sh setuptools-0.6c11-py2.7.egg
easy_install pip

5. Install virualenv:
pip install virualenv
virtualenv NAME_OF_YOUR_APP
source NAME_OF_YOUR_APP/bin/active
6. List of installed apps:
pip list
pip freeze
7. Download external modules:
cd skype_school/skype_school
git clone https://github.com/selevit/mymenu
8. Install apps using reqirements.txt or one module by one:
pip install -r requirements.txt --allow-all-external
	or
pip install Django==1.6.5
pip install django-ckeditor==4.4.7
	...
9. Download and install mysql server and workbench:
http://dev.mysql.com/downloads/windows/installer/
10. Try to run your app:
puthon manage.py runserver
