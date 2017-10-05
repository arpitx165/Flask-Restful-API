FROM python:3.6.2
LABEL maintainer="Arpit"

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

COPY . /opt/
WORKDIR /opt/

EXPOSE 5000

CMD ["python", "app.py"]
