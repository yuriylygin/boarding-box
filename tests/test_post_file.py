import sys
sys.path.append('/src/')

import pytest
import requests
import magic
import os


def test_one_face_01_post():
    file_ = '/src/tests/files/01.jpg'
    file_name = os.path.basename(file_)
    response = requests.post(url='http://localhost/', files={'file': (file_name, open(file_,'rb'), magic.from_file(file_, mime=True))})
    assert response.status_code == 200
    assert response.json() == [
        {
            "faceLocation": {
                "topLeftPoint": {
                    "x": 248,
                    "y": 514
                },
                "bottomRightPoint": {
                    "x": 1046,
                    "y": 1313
                }
            },
            "facePoints": [
                {
                    "x": 893,
                    "y": 757
                },
                {
                    "x": 766,
                    "y": 748
                },
                {
                    "x": 451,
                    "y": 709
                },
                {
                    "x": 577,
                    "y": 725
                },
                {
                    "x": 636,
                    "y": 997
                }
            ]
        }
    ]


def test_one_face_04_post():
    file_ = '/src/tests/files/04.jpeg'
    file_name = os.path.basename(file_)
    response = requests.post(url='http://localhost/', files={'file': (file_name, open(file_,'rb'), magic.from_file(file_, mime=True))})
    assert response.status_code == 200
    assert response.json() == [
        {
            "faceLocation": {
                "topLeftPoint": {
                    "x": 111,
                    "y": 82
                },
                "bottomRightPoint": {
                    "x": 379,
                    "y": 350
                }
            },
            "facePoints": [
                {
                    "x": 311,
                    "y": 167
                },
                {
                    "x": 271,
                    "y": 170
                },
                {
                    "x": 172,
                    "y": 170
                },
                {
                    "x": 211,
                    "y": 171
                },
                {
                    "x": 241,
                    "y": 250
                }
            ]
        }
    ]


def test_two_faces_post():
    file_ = '/src/tests/files/06.jpg'
    file_name = os.path.basename(file_)
    response = requests.post(url='http://localhost/', files={'file': (file_name, open(file_,'rb'), magic.from_file(file_, mime=True))})
    assert response.status_code == 200
    assert response.json() == [
        {
            "faceLocation": {
                "topLeftPoint": {
                    "x": 141,
                    "y": 290
                },
                "bottomRightPoint": {
                    "x": 409,
                    "y": 558
                }
            },
            "facePoints": [
                {
                    "x": 350,
                    "y": 358
                },
                {
                    "x": 309,
                    "y": 362
                },
                {
                    "x": 201,
                    "y": 355
                },
                {
                    "x": 246,
                    "y": 361
                },
                {
                    "x": 279,
                    "y": 450
                }
            ]
        },
        {
            "faceLocation": {
                "topLeftPoint": {
                    "x": 551,
                    "y": 222
                },
                "bottomRightPoint": {
                    "x": 737,
                    "y": 407
                }
            },
            "facePoints": [
                {
                    "x": 700,
                    "y": 270
                },
                {
                    "x": 666,
                    "y": 277
                },
                {
                    "x": 583,
                    "y": 280
                },
                {
                    "x": 616,
                    "y": 281
                },
                {
                    "x": 637,
                    "y": 354
                }
            ]
        }
    ]


def test_no_face_post():
    file_ = '/src/tests/files/05.jpg'
    file_name = os.path.basename(file_)
    response = requests.post(url='http://localhost/', files={'file': (file_name, open(file_,'rb'), magic.from_file(file_, mime=True))})
    assert response.status_code == 200
    assert response.json() == []


def test_wrong_file_format_post():
    file_ = '/src/tests/files/02.webp'
    file_name = os.path.basename(file_)
    response = requests.post(url='http://localhost/', files={'file': (file_name, open(file_,'rb'), magic.from_file(file_, mime=True))})
    assert response.status_code == 400
    assert response.json() == {
        "message": {
            "file": "JPEG JPG formats are required"
        }
    }


def test_no_file_post():
    response = requests.post(url='http://localhost/', files=None)
    assert response.status_code == 400
    assert response.json() == {
        "message": {
            "file": "Missing required parameter in an uploaded file"
        }
    }


def test_empty_post():
    response = requests.post(url='http://localhost/')
    assert response.status_code == 400
    assert response.json() == {
        "message": {
            "file": "Missing required parameter in an uploaded file"
        }
    }

