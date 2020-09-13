# Run Application

docker container run -it -p 80:80  yuriylygin/boarding-box

# Development run

docker container run -it -p 80:80 -v ${pwd}:/src/workspace yuriylygin/boarding-box bash

# Description

Flask wep application 'boarding_box.py' process POST requests with 'file' field which should contain JPEG image.

Response is an array of face locations and five face points for each face.

# Example

curl -F "file=@/mnt/d/py-projects/boarding-box/tests/files/two-persons-3034796.jpg" http://127.0.0.1:80/

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


# Failed requests

curl -F "file=" http://127.0.0.1:80/

curl -F http://127.0.0.1:80/