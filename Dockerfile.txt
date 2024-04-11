FROM python:3.11.9-slim

WORKDIR /app

COPY restAPI/requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY restAPI/ .

CMD ["python", "app.py"]
