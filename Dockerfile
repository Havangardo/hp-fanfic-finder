FROM python:3.9-slim-buster

COPY . /ficbook
WORKDIR /ficbook

RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
