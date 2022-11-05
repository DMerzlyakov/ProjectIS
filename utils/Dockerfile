#FROM python:3.9.7-slim
#
#ENV PYTHONUNBUFFERED 1
#
#EXPOSE 8000
#WORKDIR /code
#COPY ./requirements.txt /code/requirements.txt
#
#RUN apt-get update \
#    && apt-get -y install libpq-dev gcc \
#    && pip install psycopg2
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#COPY . /code
#COPY server.py /code
#CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
