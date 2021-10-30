FROM python:3.7
RUN mkdir /app
WORKDIR /app/
COPY . /app
ADD . /app/
RUN pip install -r requirements.txt
CMD ["python", "/app/flask_app.py"]