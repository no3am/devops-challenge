FROM python:3.7
COPY ../hello.py ./hello.py
COPY ../requirements.txt ./requirements.txt
EXPOSE 80
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python","hello.py"]
