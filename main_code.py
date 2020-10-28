from flask import Flask , jsonify
from flask_restful import Api,Resource,reqparse
import pandas as pd

app=Flask(__name__)
api=Api(app)

# data={1:{'first name':'Aditya','second name':'Gaurav','college':"VIT Vellore",'gf':False},
# 2:{'first name':'shradha','second name':'suman','college':"BIT Mesra",'bf':False}}
path=r'AP322_Executive Sales and Operations  Planning_1909__DetailedReport.xlsx'
df=pd.read_excel(path,sheet_name='Doc Summary')
x=df.to_dict('index')


class Trying(Resource):

    def get(self,id):
        global x
        result=x.get(id)
        return jsonify(result)

api.add_resource(Trying,"/home/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
