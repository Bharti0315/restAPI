FROM python:3.11.9-slim

WORKDIR /app

COPY restapi/requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY restapi/ .

CMD ["python", "app.py"]
