# Skype school

Template is got here: www.htmlpreviews.com/cloud/education/inition7/index.html

What do you need to have a workspace:
- PC or notebook with windows 7-8
- repository with Python Django project

How to deploy Django project on local WIn7-8 machine:

1.Install git

2.Install python 2.7: https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi

3.Add to PATH C:\Python27\Scripts;C:\Python27

4.Clone your repository: git clone https://github.com/OleksandrKara/skype_school.git

5.Download external modules: cd skype_school/skype_school git clone https://github.com/selevit/mymenu

6.Install Mysql + Workbench http://dev.mysql.com/downloads/windows/installer/

7.Install mysql-python connector https://pypi.python.org/packages/2.7/M/MySQL-python/MySQL-python-1.2.5.win32-py2.7.exe#md5=6f43f42516ea26e79cfb100af69a925e
   Install python compiler if it's needed http://www.microsoft.com/en-us/download/confirmation.aspx?id=44266

8.Create virtualenv
<code>pip install virtualenv</code>

<code>virtualenv MY_WEB_SITE_ENC //will create envirement</code>

<code>copy your repository inside MY_WEB_SITE_ENC folder</code>

<code>open git bash</code>

<code>source MY_WEB_SITE_ENC/bin/active //will active your envirement</code>

9.Install all python packages:  
<code>pip install -r requirements.txt --allow-all-external</code>
   
List of installed packages: <code>pip list pip freeze</code>

10.Change settings.py with your mysql cridentials.

11.python manage.py runserver
