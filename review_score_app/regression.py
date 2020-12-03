#Using linear regression to build the relationship between title sentiment and rating


def scale(an, a0, a1, b0, b1):
    bn = (an-a0) * ((b1-b0)/(a1-a0)) +1 
    return bn

#import numpy as np
#from sklearn.linear_model import LinearRegression
# def regression(x, y, y_predi):
# 	# x = rating
# 	# y = sentiment score
# 	# y_predi = target sentiment score
# 	x = np.array(x).reshape(len(x),1)
# 	y = np.array(y).reshape(len(y),1)

# 	new_model = LinearRegression().fit(x, y.reshape((-1, 1)))

# 	x_predi = (y_predi - new_model.intercept_) / new_model.coef_

# 	return(x_predi)


