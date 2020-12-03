from review_score_app import db
from sqlalchemy.inspection import inspect as inspect


class Serializer(object):
    """Class for serializing SQLAlchemy objects into dicts."""

    @staticmethod
    def is_primitive(obj):
        return type(obj) in (int, float, str, bool)

    def serialize(self):
        fields = inspect(self).attrs.keys()
        return {c: getattr(self, c) for c in fields if Serializer.is_primitive(getattr(self, c))}

    @staticmethod
    def serialize_list(list_obj):
        return [m.serialize() for m in list_obj]


class Product(db.Model, Serializer):

    product_id  =  db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    product_key =  db.Column(db.String(255), unique=True, nullable=False)
    brand = db.Column(db.String(255))
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    reviews_product = db.relationship('Review', backref= "product")


    def __repr__(self):
        return f'Product name:{self.name}, Brand:{self.brand}, Category: {self.category}'

class Customer(db.Model, Serializer):

    customer_id =   db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    username    =   db.Column(db.String(255))
    gender      =   db.Column(db.String(255))
    age         =   db.Column(db.Integer)
    reviews_customer = db.relationship('Review', backref= "customer")
    def __repr__(self):
        return f'Customer ID: {self.customer_id}, User name: {self.username}, Gender:{self.gender}, Age: {self.age}'


class Review(db.Model, Serializer):
    
    review_id  =  db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    product_id =  db.Column(db.Integer, db.ForeignKey('product.product_id'))
    review_date = db.Column(db.String)
    doRecommend = db.Column(db.String)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String)
    review_title = db.Column(db.String)
    sentiment_score = db.Column(db.Float)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

if __name__ == '__main__':
    db.create_all()   
    db.session.commit()


