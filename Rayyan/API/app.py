import json
from tokenize import Number
from unicodedata import name
from flask import Flask, request, jsonify, make_response
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from sqlalchemy.sql import func
from sqlalchemy import update, asc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@127.0.0.1:3306/store'
db = SQLAlchemy(app)

class customer_store(db.Model):
    __tablename__ = "customer_store"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(30))
    name = db.Column(db.String(30))
    gender = db.Column(db.String(3))
    phone_number = db.Column(db.String(15))
    image = db.Column(db.String(100))
    email = db.Column(db.String(30))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, id , title, name, gender, phone_number, image, email, created_at, updated_at):
        self.id = id
        self.title = title
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.image = image
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"{self.id}"
    
class address_store(db.Model):
    __tablename__ = "address_store"
    id = db.Column(db.Integer(), primary_key=True)
    customer_id = db.Column(db.Integer(), foreign_key=True)
    address = db.Column(db.String(30))
    district = db.Column(db.String(20))
    city = db.Column(db.String(20))
    province = db.Column(db.String(20))
    postal_code = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def __init__(self, id , customer_id, address, district, city, province, postal_code, created_at, updated_at):
        self.id = id
        self.customer_id = customer_id
        self.address = address
        self.district = district
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"{self.id}"

class customerSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = customer_store
        sqla_session = db.session

    id = fields.Integer(required=True)
    title = fields.String(required=True)
    name = fields.String(required=True)
    gender = fields.String(required=True)
    phone_number = fields.String(required=True)
    image = fields.String(required=True)
    email = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

class addressSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = address_store
        sqla_session = db.session

    id = fields.Integer(required=True)
    customer_id = fields.Integer(required=True)
    address = fields.String(required=True)
    district = fields.String(required=True)
    city = fields.String(required=True)
    province = fields.String(required=True)
    postal_code = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

##1. List Of Customer
@app.route('/customer', methods=['GET'])
def listCustomer():

    get_customer = customer_store.query.order_by(asc(customer_store.name))
    customer_schema = customerSchema(many=True)
    customer = customer_schema.dump(get_customer)

    return make_response(jsonify({"data": customer}))

##2. Detail Of Customer
@app.route('/customer/<int:id>', methods=['GET'])
def getCustomer(id):
    
    get_customer = customer_store.query.filter_by(id=id)
    id = request.view_args['id']
    customer_schema = customerSchema(many=True)
    customer = customer_schema.dump(get_customer)
    get_address = address_store.query.filter_by(customer_id=id)
    address_schema = addressSchema(many=True)
    address = address_schema.dump(get_address)
    return make_response(jsonify({"address": address, "data": customer}))

## List Of Address
@app.route('/getAddress', methods=['GET'])
def getAddress():

    get_address = address_store.query.all()
    address_schema = addressSchema(many=True)
    address = address_schema.dump(get_address)

    return make_response(jsonify({"data": address}))

## 3. Add New Customer
@app.route('/customer', methods=['POST'])
def addCustomer():
    data = request.get_json()
  
    customer_schema = customerSchema()
    customer = customer_schema.load(data)
    result = customer_schema.dump(customer.create())

    return make_response(jsonify({"message":result}), 200)

## 4. Add New Address
@app.route('/address', methods=['POST'])
def addAddress():
    data = request.get_json()
  
    address_schema = addressSchema()
    address = address_schema.load(data)
    result = address_schema.dump(address.create())
    return make_response(jsonify({"message":result}), 200)

## 5. Update Customer
@app.route('/customer/<int:id>', methods=['PATCH'])
def updateCustomer(id):
    id = request.json.get("id")
    title = request.json.get("title")
    name = request.json.get("name")
    gender = request.json.get("gender")
    phone_number = request.json.get("phone_number")
    image = request.json.get("image")
    email = request.json.get("email")
    created_at = request.json.get("created_at")
    updated_at = request.json.get("updated_at")
    customer = customer_store.query.filter_by(id=id).first()
    customer.title = title
    customer.name = name
    customer.gender = gender
    customer.phone_number = phone_number
    customer.image = image
    customer.email = email
    customer.created_at = created_at
    customer.updated_at = updated_at

    db.session.commit()
    return make_response(jsonify({"message": "Success"}), 200)

## 6. Update Address
@app.route('/address/<int:id>', methods=['PATCH'])
def updateAddress(id):
    id = request.json.get("id")
    customer_id = request.json.get("customer_id")
    address = request.json.get("address")
    district = request.json.get("district")
    city = request.json.get("city")
    province = request.json.get("province")
    postal_code = request.json.get("postal_code")
    created_at = request.json.get("created_at")
    updated_at = request.json.get("updated_at")
    items = address_store.query.filter_by(id=id).first()
    items.custromer_id = customer_id
    items.address = address
    items.district = district
    items.city = city
    items.province = province
    items.postal_code = postal_code
    items.created_at = created_at
    items.updated_at = updated_at

    db.session.commit()
    return make_response(jsonify({"message": "Success"}), 200)

## 7. Delete Customer
@app.route('/customer/<int:id>', methods=['DELETE'])
def deleteCustomer(id):
    id = request.json.get("id")
    get = customer_store.query.get(id)

    db.session.delete(get)
    db.session.commit()

    return make_response(jsonify({"message": "Deleted"}), 200)

## 8. Delete Address
@app.route('/address/<int:id>', methods=['DELETE'])
def deleteAddress(id):
    id = request.json.get("id")
    get = address_store.query.get(id)

    db.session.delete(get)
    db.session.commit()
    return make_response(jsonify({"message": "Deleted"}), 200)

if __name__ == "__main__":
    app.run(debug=True)