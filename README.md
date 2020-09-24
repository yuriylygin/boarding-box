# Run Application

docker container run -it --rm --name boarding-box -p 80:80  yuriylygin/boarding-box

# Development run

docker container run -it --rm --name boarding-box -p 80:80 -v ${pwd}:/src yuriylygin/boarding-box bash

# Development run under docker-compose and testing

1) Firstly run docker-compose:
docker-compose

2) Next you should run bash inside the running 'flask' container:
docker container exec -it flask bash

3) Before running pytests you have to install packages that are used for development process only:
pipenv install --dev --skip-lock

4) Now run tests in the created environment:
pipenv run pytest -v

# Description

Flask wep application 'boarding_box' process POST requests with 'file' field which should contain JPEG image.

Response is an array of face locations and five face points for each face.

# Example

curl -F "file=@path/to/a/file.jpg" http://127.0.0.1:80/

Response:

[
    {
        "faceLocation": {"topLeftPoint": {"x": 141, "y": 290}, "bottomRightPoint": {"x": 409, "y": 558}}, 
        "facePoints": [{"x": 350, "y": 358}, {"x": 309, "y": 362}, {"x": 201, "y": 355}, {"x": 246, "y": 361}, {"x": 279, "y": 450}]
    }, 
    {
        "faceLocation": {"topLeftPoint": {"x": 551, "y": 222}, "bottomRightPoint": {"x": 737, "y": 407}}, 
        "facePoints": [{"x": 700, "y": 270}, {"x": 666, "y": 277}, {"x": 583, "y": 280}, {"x": 616, "y": 281}, {"x": 637, "y": 354}]
    }
]


# Requests to fail

curl -F "file=" http://127.0.0.1:80/

curl -F http://127.0.0.1:80/