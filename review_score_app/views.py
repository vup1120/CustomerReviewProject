
"""
Description: Requests supported by the flask app.
"""
import logging

import sqlalchemy
from flask import jsonify, request, make_response

from review_score_app import app
from review_score_app.models import Product, Review
from review_score_app.sentiment_api import sentiment_score


@app.route('/')
def index():
    return "Welcome to the Customer Rating Suggestor"



# get all product overview
@app.route('/product', methods=['GET'])
def all_product_view():
	if request.method == 'GET':
		product = Product.query.all()

		#product = Product.query.filter(Product.name.like('a%')).all()

		#query = session.query(Books).filter(Books.title.like('____')).all()

		#product = product.get_all(filters=request.args)

	return jsonify(data=Product.serialize_list(product))

#get a specific product
@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def single_product_view(product_id):
	if request.method == 'GET':

		logging.info(f'User has given input product_id as: {product_id}')
		#product_result = Product.query.filter(Product.product_id == product_id).all()
		product_result = Product.query.join(Review).filter(Product.product_id == product_id).all()
		# how to call rating? 
		for i in list(product_result):
			print(i.product_id)
		logging.info(f'Product from db is: {product_result}')
		return f'User has given input product_id as: {product_id}, {product_result}'

		if product_result is None:
			return make_response(jsonify(response=f'Product with id {product_id} not found'), 404)
def single_product_give_review(product_id, review_text):

	if request.method == 'POST':
		logging.info(f'User has given input product_id as: {product_id}')
		polar, score_value = sentiment_score(review_text)
		return f'review text sentiment: {polar}, {score_value}'
		
		if product_result is None:
			return make_response(jsonify(response=f'Product with id {product_id} not found'), 404)


# def product_view():
#     if request.method == 'GET':
#         product = product.get_all(filters=request.args)
#         return jsonify(data=Product.serialize_list(product))

# @app.route('/product/<int:product_id>', methods=['GET'])
# def product_view(product_id):
#     logging.info(f'User has given input product_id as: {product_id}')
#     product_result = product.get(product_id)
#     logging.info(f'Product from db is: {product_result}')
#     if author_result is None:
#         return make_response(jsonify(response=f'Product with id {product_id} not found'), 404)
