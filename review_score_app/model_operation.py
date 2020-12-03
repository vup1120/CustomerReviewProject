from review_score_app import db
from review_score_app.models import Review, Customer
import matplotlib.pyplot as plt


class OperatorReview():

	def get_all(filters):
		allowed_filters = ['product_id', 'doRecommend', 'rating', 'review_text', 'customer_id']
		final_filters = {k: v for k, v in filters.items() if k in allowed_filters}
		reviews = Review.query.filter_by(**final_filters).all()
		return reviews

	def get_ratings_count(product_id):
		reviews = Review.query.filter_by(product_id=product_id).all()
		ratings = []
		rating_range = [1,2,3,4,5]
		for i in reviews:
			if i.rating is not None:
				ratings.append(i.rating)
		ratings_count = {}
		for i in rating_range:
			ratings_count.update({i:ratings.count(i)})
		return ratings_count

	def get_ratings_plot(product_id):
		ratings_count = self.get_ratings_count(product_id)
		lists = sorted(ratings_count.items()) # sorted by key, return a list of tuples
		x, y = zip(*lists) # unpack a list of pairs into two tuples
		plt.bar(x,y)
		plt.xlabel('User Ratings')
		plt.ylabel('Count')
		plt.savefig('rating_plot.png')

	def create(product_id, review_date=None, doRecommend=None, rating=None, review_text=None, review_title=None, sentiment_score=None, customer_id=None):
		new_review = Review(product_id=product_id, review_date=review_date, 
							doRecommend=doRecommend, rating=rating, review_text=review_text, 
							review_title=review_title, sentiment_score=sentiment_score, 
							customer_id=customer_id)
		db.session.add(new_review)
		db.session.commit()


class OperatorCustomer():

	def get(username):
		return Customer.query.filter_by(username=username).first()

	def get_customer_id(username):
		this_customer = Customer.query.filter_by(username=username).first()
		return this_customer.customer_id

	def create(username, gender=None, age=None):
		new_customer = Customer(username=username, gender=gender, age=age)
		db.session.add(new_customer)
		db.session.commit()


