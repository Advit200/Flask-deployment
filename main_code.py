from flask import Flask , jsonify
from flask_restful import Api,Resource,reqparse

app=Flask(__name__)
api=Api(app)

data={1:{'first name':'Aditya','second name':'Gaurav','college':"VIT Vellore",'gf':False},
2:{'first name':'shradha','second name':'suman','college':"BIT Mesra",'bf':False}}

class Trying(Resource):

    def get(self,id):
        result=data.get(id)
        return jsonify(result)



api.add_resource(Trying,"/home/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)