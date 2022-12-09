from flask import Flask,request
from flask_pymongo import PyMongo

app=Flask(__name__)

app.config['MONGO_URI']='mongodb+srv://admin-staging:J3QUMICMQE9T3vnl@dropshipping-staging.6meionj.mongodb.net/mongo-dropshipping-staging?authSource=admin&replicaSet=atlas-s8w3w5-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'
mongo=PyMongo(app)


@app.route('/getguides', methods=['GET'])
def  getguides():
    
    guides=request.json['guides']
    shiiping=mongo.db.shippingOrders.find_one({"guides":guides})
    return str(shiiping)





@app.route('/uptadeguides', methods=['POST'])
def  updateguides():
    try:
        guides=request.json['guides']
        status=request.json['status']
        shiiping=mongo.db.shippingOrders.update_one({"guides":guides},{"$set":{"status":status}})
        return {"message":" cambio hecho"}
    except Exception as e:
        return {"message":e}
       

if __name__== "__main__":
    app.run(debug=True)