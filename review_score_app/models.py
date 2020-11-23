from review_score_app.app import db


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
    reviews = db.relationship('Reivew', backref= "product")


    #def __repr__(self):
    #    return "<Tag (name='%s')>" % (self.name)

class Customer(db.Model, Serializer):

    customer_id =   db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    username    =   db.Column(db.String(255))
    gender      =   db.Column(db.String(255))
    age         =   db.Column(db.Integer)
    reviews = db.relationship('Reivew', backref= "customer")

class Reivew(db.Model, Serializer):
    
    review_id  =  db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    product_id =  db.Column(db.Integer, db.ForeignKey('product.product_id'))
    review_date = db.Column(db.DateTime)
    doRecommend = db.Column(db.String)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String)
    review_title = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    #customer = db.relationship('Customer', backref= "review")
    #product = db.relationship('Product', backref= "review")


if __name__ == '__main__':
    db.create_all()
    db.session.commit()


