import json

from flask import Flask, request, jsonify
import Products_dao
import categories_dao
from db_connection import get_db_connection

app = Flask(__name__)
connection = get_db_connection()


@app.route('/getcategory', methods=['GET'])
def get_categories():
    response = categories_dao.get_category(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getproducts', methods=['GET'])
def get_all_products():
    products = Products_dao.get_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/addproducts', methods=['POST'])
def add_products():
    add_data = json.loads(request.form['data'])
    add_prd = Products_dao.add_product(connection, add_data)
    response = jsonify({'product_name': add_prd})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteproducts', methods=['POST'])
def delete_products():
    d_product = Products_dao.delete_products(connection, request.form['product_name'])
    response = jsonify({'product_name': d_product})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("Python Server for Clothing Store Management System")
    app.run(port=5000)
