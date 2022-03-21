FROM python:3.9

ADD sus.py .
ADD requirements.txt .
ADD .env .

RUN pip install -r requirements.txt

CMD ["python", "sus.py"]