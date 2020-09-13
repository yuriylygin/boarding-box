FROM  yuriylygin/dlib-python:latest

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY app /src/app

COPY model /src/model

WORKDIR /src/workspace

CMD [ "python", "/src/app/boarding_box.py" ]