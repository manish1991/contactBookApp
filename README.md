# contactBookApp
Follow following steps to run this django app:

1.Create a virtual environment with python 3.4:
              virtualenv -p /usr/bin/python3.4 venv
2. Activate virtual environment:
              source venv/bin/activate
3.Install django 1.8:
             pip install django==1.8
4.Install Python Social Auth:
          pip install python-social-auth

5.Create migrations script:
         python manage.py makemigrations

6.Create tables in database migration script:
		python manage.py migrate
7.Finally run server:
        python manage.py runserver 