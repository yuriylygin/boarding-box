# Run Application

docker container run -it --rm --name boarding-box -p 80:80  yuriylygin/boarding-box

# Development run

docker container run -it --rm --name boarding-box -p 80:80 -v ${pwd}:/src yuriylygin/boarding-box bash

# Development run under docker-compose and testing

1) Firstly run docker-compose:\
<code>docker-compose</code>

2) Next you should run bash inside the running 'flask' container:\
<code>docker container exec -it flask bash</code>

3) Before running pytests you have to install packages that are used for development process only:\
<code>pipenv install --dev --skip-lock</code>

4) Now run tests in the created environment:\
<code>pipenv run pytest -v</code>

# Description

Flask wep application 'boarding_box' process POST requests with 'file' field which should contain JPEG image.

Response is an array of face locations and five face points for each face.

# Example

curl -F "file=@path/to/a/file.jpg" http://127.0.0.1:80/

Response:
<pre>
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
</pre>


# Requests to fail

curl -F "file=" http://127.0.0.1:80/

curl -F http://127.0.0.1:80/
