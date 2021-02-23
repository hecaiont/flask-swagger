from flask import Flask
from flask_restx import Resource, Api, Namespace

app = Flask(__name__)
api = Api(app, version='1.2', title='Sample API',
    description='number double API',)


@api.doc(True)
@api.route('/double/<num>')
@api.doc(get={'params': {'number': 'number x 2'}})
class PutImage(Resource):
    def get(self, num):
        return {'number': int(num)*2}


if __name__ == '__main__':
    app.run(debug=True)