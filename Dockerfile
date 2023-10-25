FROM python:3.11.4

ENV PYTHONUNBUFFERED 1

ENV DOCKER=True

RUN mkdir /app_grupo3
RUN mkdir /data


WORKDIR /app_grupo3

COPY requirements.txt /app_grupo3/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app_grupo3/

EXPOSE 8000

RUN python PlanificadorViajes/manage.py makemigrations
RUN python PlanificadorViajes/manage.py migrate
RUN python PlanificadorViajes/manage.py rebuild_index --noinput

CMD python PlanificadorViajes/manage.py makemigrations; python PlanificadorViajes/manage.py migrate; python PlanificadorViajes/manage.py runserver 0.0.0.0:8000