import numpy as np
import pandas as pd
import pickle

class Recommendation:
    def __init__(self):
        # Model Path
        self.logit=pickle.load(open('pickle/logistic_model.pkl', 'rb'))
        self.word_vectorizer= pickle.load(open('pickle/word_vectorizer.pkl', 'rb'))
        self.user_predicted_ratings = pd.read_pickle("pickle/user_predicted_ratings.pkl")
        self.df_latest=pd.read_csv("dataset/final_data.csv")

    def top_5_recommendation(self, user_input):
        arr = self.user_predicted_ratings.loc[user_input].sort_values(ascending=False)[0:20]
        i= 0
        a = {}
        
        for prod_name in arr.index.tolist():
            product = prod_name
            product_name_review_list =self.df_latest[self.df_latest['name']== product]['Reviews_Text_and_Title'].tolist()
            features= self.word_vectorizer.transform(product_name_review_list)
            self.logit.predict(features)
            a[product] = self.logit.predict(features).mean()*100
        
        b= pd.Series(a).sort_values(ascending = False).head(5).index.tolist()
        result= pd.Series(a).sort_values(ascending = False).head(5).index.tolist()
        
        return result