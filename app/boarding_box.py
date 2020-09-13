from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
import dlib
import tempfile

app = Flask(__name__)
api = Api(app)


class BoardingBox(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True)

    def post(self):
        args = self.parser.parse_args()

        if args.file.mimetype in ['image/jpeg']:

            with tempfile.NamedTemporaryFile() as temp:
                temp.write(args.file.read())
                image = dlib.load_rgb_image(temp.name)
                
            face_detector = dlib.get_frontal_face_detector()
            faces = face_detector(image, 1)
            predictor = dlib.shape_predictor('/src/model/shape_predictor_5_face_landmarks.dat')  # эту модель надо скачать https://github.com/davisking/dlib-models/blob/master/shape_predictor_5_face_landmarks.dat.bz2

            res = []

            for face in faces:
                shape = predictor(image, face)
                face_points = list(map(lambda i: {'x': shape.part(i).x, 'y': shape.part(i).y}, range(shape.num_parts)))
                tl_corner = face.tl_corner()
                br_corner = face.br_corner()

                res.append({
                    'faceLocation': {'topLeftPoint': {'x': tl_corner.x, 'y': tl_corner.y}, 'bottomRightPoint': {'x': br_corner.x, 'y': br_corner.y}},
                    'facePoints': face_points
                })

            return res

        return {'message': {'file': 'JPEG JPG formats are required'}}, 400
        
        

api.add_resource(BoardingBox, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=False)