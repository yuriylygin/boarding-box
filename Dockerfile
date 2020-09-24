FROM  yuriylygin/dlib-python:dlib19.21.0-py3.7

RUN pip install pipenv setuptools wheel

WORKDIR /src/

COPY boarding_box boarding_box

COPY model model

COPY Pipfile Pipfile

RUN pipenv install --site-packages --skip-lock --clear

CMD ["pipenv", "run", "python", "boarding_box/app.py" ]