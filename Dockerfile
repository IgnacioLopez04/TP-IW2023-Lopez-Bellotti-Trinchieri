FROM python:3.9.18

ENV PYTHONUNBUFFERED 1

ENV DOCKER=True

RUN mkdir /app_grupo3
RUN mkdir /data


WORKDIR /app_grupo3

COPY requirements.txt /app_grupo3/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app_grupo3

EXPOSE 8000

CMD python PlanificadorViajes/manage.py migrate; \
    python PlanificadorViajes/manage.py loaddata data.json ; \
    python PlanificadorViajes/manage.py rebuild_index --noinput ; \
    python PlanificadorViajes/manage.py runserver 0.0.0.0:8000; \