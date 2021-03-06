import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate,identity
from resource.user import UserRegister
from resource.item import Item,ItemList
from resource.store import Store, StoreList

app= Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key='akalya'
api=Api(app)

jwt=JWT(app,authenticate,identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)








