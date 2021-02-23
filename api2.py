from flask import Flask
from flask_restx import Resource, Api, Namespace

from werkzeug.datastructures import FileStorage

app = Flask(__name__)
api = Api(app, version='1.0', title='File API',
    description='File upload API',
    )

# api.add_namespace(Namespace('upload API', path='/upload'))


upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

@api.route('/upload/')
@api.expect(upload_parser)
class Upload(Resource):
    def post(self):
        """파일을 업로드 합니다."""
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # This is FileStorage instance
        url = do_something_with_file(uploaded_file)
        return {'url': url}, 201





if __name__ == '__main__':
    app.run(debug=True)