from flask import Flask
from flask import jsonify,send_file
from flask import request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
import json

app = Flask(__name__,template_folder='templates')

config = json.loads(open('config.json').read())
app.config["MONGO_DBNAME"] = config["configuration"]["DB_Name"]
#if config["configuration"]["DB_URI"]:
#    app.config["MONGO_URI"]=config["configuration"]["DB_URI"]
collection_name=config["configuration"]["DB_COLLECTION_NAME"]
mongo = PyMongo(app)

class User(Resource):

    def get(self,user_name):
        #data=mongo.db.repos.fin
        user_detail={}
        user_detail["repos"]=[]
        data =mongo.db.repos.find({"payload.pull_request.base.repo.owner.login":user_name})
        for i in data:
            user_detail["repos"].append(i["payload"]["pull_request"]["base"]["repo"])
        return jsonify({"Status":"Ok","response":{"user_name":user_name,"data":user_detail}})
        pass

class Repository(Resource):

    def get(self, language_name):
        html_url={}
        html_url["repos"]=[]
        data = mongo.db.repos.find({"payload.pull_request.base.repo.language":language_name})
        for i in data:
            html_url["repos"].append(i["payload"]["pull_request"]["base"]["repo"])

        return jsonify({"Status":"Ok","response":{"language_name":language_name,"data":html_url}})


class Technology(Resource):
    def get(self):

        #data = mongo.db.repos.find()
        count_val=[]
        print(collection_name)
        language=mongo.db.repos.distinct("payload.pull_request.base.repo.language")
        for i in language:
            count_val.append(mongo.db.repos.find({"payload.pull_request.base.repo.language":i}).count())

        return jsonify({"status": "ok", "data": {"language_Name":language , "Count":count_val}})
        # return render_template('index.html',data=jsonify({"status": "ok", "data": {"language_Name":language , "Count":count_val}}))



class Index(Resource):
    def get(self):
        return send_file('templates/index.html')


api = Api(app)
api.add_resource(Index, "/", endpoint="index")
api.add_resource(Technology,"/technology",endpoint="technology")
api.add_resource(Repository, "/repo/<string:language_name>", endpoint="Repository")
api.add_resource(User, "/user/<string:user_name>", endpoint="User")




if __name__ == "__main__":
    app.run(debug=config["configuration"]["Debug_Option"])
