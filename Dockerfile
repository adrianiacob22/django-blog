# Tragem din dockerhub o imagine de python3
FROM python:3.8-buster

# Seteaza si expune portul pe care va rula aplicatia
ENV LISTEN_PORT=8000
EXPOSE 8000
# Instaleaza uWSGI
RUN pip install uwsgi
# Indica locul unde se gaseste uwsgi.ini
ENV UWSGI_INI uwsgi.ini

# Copiaza fisierele aplicatiei in locatia de unde vor fi executate
WORKDIR /app
ADD . /app

# # Adauga pasii de activare si executie a mediului virtual python3
# RUN python3 -m venv venv
# RUN source venv/bin/activate

# Ma asigur ca dependintele sunt instalate
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Setez permisiuni de scriere pe directorul in care am instalat aplicatia
RUN chmod g+w /app

ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
