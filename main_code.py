from flask import Flask , jsonify
from flask_restful import Api,Resource,reqparse
import pandas as pd
import os

app=Flask(__name__)
api=Api(app)

# data={1:{'first name':'Aditya','second name':'Gaurav','college':"VIT Vellore",'gf':False},
# 2:{'first name':'shradha','second name':'suman','college':"BIT Mesra",'bf':False}}
path_name = r"\\ts.accenture.com@SSL\DavWWWRoot\sites\softwares419\Shared Documents\General"

files_list = []

for files in os.listdir(path_name):
	if os.path.splitext(files) == ".xlsx":
		files_list.append(files)


path=files_list[0]
df=pd.read_excel(path,sheet_name='Asset')
x=df.to_dict('index')


class Trying(Resource):

    def get(self,id):
        global x
        result=x.get(id)
        return jsonify(result)

api.add_resource(Trying,"/home/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
