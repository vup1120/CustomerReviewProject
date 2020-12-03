# CustomerReviewProject
Customer Review Project under Back-End Development course in ReDI digital school

This API provides user rating estimation based on review text using sentiment analysis. 

## Setting up
1. Install dependencies by running: pip install -r requirements.txt
2. Initialize db by running: python review_score_app/DataLayer/models.py

## Running the app
1. python run.py

## Guide to the code
1. The API requests are defined in review_score_app/APILayer/views.py
2. All the database models are defined in review_score_app/DataLayer/models.py
3. The sentiment analysis service is in review_score_app/ServiceLayer/sentiment_api.py
3. Logging configuration is defined in review_score_app/__init__.py
