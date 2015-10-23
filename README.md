# Skype school

Template is got here: www.htmlpreviews.com/cloud/education/inition7/index.html

What do you need to have a workspace:
- PC or notebook with windows 7-8
- repository with Python Django project

How to deploy Django project on local WIn7-8 machine:

0. Install git

1. Install python 2.7: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

2. Add to PATH C:\Python27\Scripts;C:\Python27

3. Clone your repository: git clone https://github.com/OleksandrKara/skype_school.git
3.1. Download external modules: cd skype_school/skype_school git clone https://github.com/selevit/mymenu

4. Install Mysql + Workbench http://dev.mysql.com/downloads/windows/installer/

5. Install mysql-python connector https://pypi.python.org/packages/2.7/M/MySQL-python/MySQL-python-1.2.5.win32-py2.7.exe#md5=6f43f42516ea26e79cfb100af69a925e
   Install python compiler if it's needed http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266

6. Create virtualenv
	pip install virtualenv
	virtualenv MY_WEB_SITE_ENC //will create envirement
	copy your repository inside MY_WEB_SITE_ENC folder
	open git bash
	source MY_WEB_SITE_ENC/bin/active //will active your envirement

7. Install all python packages 
   pip install -r requirements.txt --allow-all-external
   List of installed packages: pip list pip freeze

7. Change settings.py with your mysql cridentials.

8. python manage.py runserver
