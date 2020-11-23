"""
Description: Requests supported by the flask app.
"""
import logging

import sqlalchemy
from flask import jsonify, request, make_response

from review_score_app import app
from review_score_app.models import Product


@app.route('/')
def index():
    return "Welcome to Library app"

@app.route('/product', methods=['GET'])
def product_view():
    if request.method == 'GET':
        product = product.get_all(filters=request.args)
        return jsonify(data=Product.serialize_list(product))

@app.route('/product/<int:product_id>', methods=['GET'])
def product_view(product_id):
    logging.info(f'User has given input product_id as: {product_id}')
    product_result = product.get(product_id)
    logging.info(f'Product from db is: {product_result}')
    if author_result is None:
        return make_response(jsonify(response=f'Product with id {product_id} not found'), 404)
