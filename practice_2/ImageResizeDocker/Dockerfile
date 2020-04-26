FROM python:3.6

RUN pip3 install python-resize-image boto3

WORKDIR /app
COPY app.py /app/
COPY resize.sh /app/

VOLUME ["/app/images"]


