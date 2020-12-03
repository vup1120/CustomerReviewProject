
"""
Description: Requests supported by the flask app.
"""
import logging

import sqlalchemy
from flask import jsonify, request, make_response, send_file

from review_score_app import app, utils
from review_score_app.models import Product, Review, Customer
from review_score_app.sentiment_api import sentiment_score
from review_score_app.model_operation import OperatorReview, OperatorCustomer
from review_score_app.regression import scale
from datetime import date


@app.route('/')
def index():
    return "Welcome to the Customer Rating Suggestor"

@app.route('/site-map')
def site_map():
    urls = {utils.werkzeug_rule_endpoint(url): str(url.methods) for url in app.url_map.iter_rules()}
    return jsonify(urls)


# get all product overview

@app.route('/product')
def all_product_view():
	product = OperatorReview.get_all(filters=request.args)
	return jsonify(data=Review.serialize_list(product))

# plot figures

@app.route('/product/<int:product_id>', methods=['GET'])
def product_rating(product_id):
	if request.method == 'GET':
		ratings_count = OperatorReview.get_ratings_count(product_id)
		return jsonify(ratings=ratings_count)


@app.route('/product/<int:product_id>/get_image', methods=['GET'])
def get_image(product_id):
	if request.method == 'GET':
		OperatorReview.get_ratings_plot(product_id)
		filename = '../rating_plot.png'
		return send_file(filename, mimetype='image/png')


@app.route('/user/<username>', methods=["GET", "POST"])
def check_user(username):
	if request.method == 'GET':
		username = str(username)
		this_user = OperatorCustomer.get(username)
		if this_user:
			return jsonify(message = "User exists.", userID=this_user.customer_id)

		if not this_user:
			return jsonify(message = "No this user. Please create a new user with user information by a POST request")
			
	if request.method == 'POST':
		data = request.get_json()
		if not data:
			abort(400, {"message": "there is no json body"})
		username = str(username)
		this_user = OperatorCustomer.get(username)
		if this_user:
			return jsonify(message = "User exists.", userID=this_user.customer_id)
		if not this_user:
			new_name = username
			new_age = data.get("age")
			new_gender = data.get("gender")
			OperatorCustomer.create(username=username, age=new_age, gender=new_gender)

			return make_response(jsonify(response='New user created'), 201)

@app.route('/review/<int:product_id>/<username>', methods=["POST"])
def write_review(product_id, username):
	if request.method == 'POST':
		try:
			allowed_fields = ['doRecommend', 'review_text', 'review_title']
			extra_fields = {k:v for k,v in request.json.items() if k not in allowed_fields}
			if len(extra_fields) > 0:
				return make_response(jsonify(response="Only doRecommend, review text and review title are allowed"), 400)
			score = sentiment_score(request.json.get('review_text'))
			rating=int(round(scale(score, -1., 1., 1., 5.)))

			OperatorReview.create(product_id=product_id,
								  review_date=str(date.today()),
		                          doRecommend=request.json.get('doRecommend'),
		                          rating=rating,
		                          review_text=request.json.get('review_text'),
		                          review_title=request.json.get('review_title'),
		                          sentiment_score=score,
		                          customer_id=OperatorCustomer.get_customer_id(username))

			logging.info(f'The sentiment_score of the review is {sentiment_score}. The suggesting rating is {rating}')

			return jsonify(message = "Review info saved.", sentiment_score=score, suggesting_rating=rating)

		except sqlalchemy.exc.InvalidRequestError as error:
			return make_response(jsonify(error_message=str(error)), 400)

