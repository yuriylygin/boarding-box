FROM  yuriylygin/dlib-python:dlib19.21.0-py3.7

RUN pip install pipenv

WORKDIR /src/

COPY app app

COPY model model

COPY Pipfile Pipfile

COPY Pipfile.lock Pipfile.lock

RUN pipenv install --site-packages

CMD ["pipenv", "run", "python", "app/boarding_box.py" ]