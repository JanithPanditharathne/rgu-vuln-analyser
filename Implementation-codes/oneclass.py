# Import necessary packages

import pandas as pd
import re
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
# import RF model
from sklearn.ensemble import RandomForestClassifier
# import SVM model
from sklearn import svm
# import NB model
from sklearn.naive_bayes import GaussianNB
# import the LR model
from sklearn.linear_model import LogisticRegression
# import KNN model
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# importing the Dataset
vuln_dataset = pd.read_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\vuln_dataset.csv', index_col=0)

#Data cleaning and preprocessing

lemmatizer = WordNetLemmatizer()

corpus = []
for i in range(0, len(vuln_dataset)):
    review = re.sub('[^a-zA-Z]', ' ', str(vuln_dataset['code'][i]))
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review] # add lemmatization
    review = ' '.join(review)
    corpus.append(review)
  
# TFIDF Model 

tf_idf = TfidfVectorizer()
X_test_both = tf_idf.fit_transform(corpus).toarray()

# Set y value

y_test_both=vuln_dataset.category

# importing the Dataset
vulnbenign_dataset = pd.read_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\even\\vulnbenign_dataset.csv', index_col=0)

#Data cleaning and preprocessing

lemmatizer = WordNetLemmatizer()

corpus = []
for i in range(0, len(vulnbenign_dataset)):
    review = re.sub('[^a-zA-Z]', ' ', str(vulnbenign_dataset['code'][i]))
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review] # add lemmatization
    review = ' '.join(review)
    corpus.append(review)
  
# TFIDF Model 

tf_idf = TfidfVectorizer()
X_train_benign = tf_idf.fit_transform(corpus).toarray()

# Set y value

y_train_benign=vulnbenign_dataset.category

# Training model using RF

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train_benign,y_train_benign)

y_pred=clf.predict(X_test_both)

# Model Accuracy, how often is the classifier correct?
print("RF Accuracy:",metrics.accuracy_score(y_test_both, y_pred))

# View the classification report for test data and predictions
print("RF CLassification Report")
print(classification_report(y_test_both, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89']))

print("RF Confusion Metrix")
print(metrics.confusion_matrix(y_test_both, y_pred))

# SVM

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train_benign, y_train_benign)

#Predict the response for test dataset
y_pred = clf.predict(X_test_both)

# Model Accuracy: how often is the classifier correct?
print("SVM Accuracy:",metrics.accuracy_score(y_test_both, y_pred))

# View the classification report for test data and predictions
print("SVM CLassification Report")
print(classification_report(y_test_both, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89']))

print("SVM Confusion Metrix")
print(metrics.confusion_matrix(y_test_both, y_pred))

# NB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train_benign, y_train_benign)

#Predict the response for test dataset
y_pred = gnb.predict(X_test_both)

# Model Accuracy, how often is the classifier correct?
print("NB Accuracy:",metrics.accuracy_score(y_test_both, y_pred))

# View the classification report for test data and predictions
print("NB CLassification Report")
print(classification_report(y_test_both, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89']))

print("NB Confusion Metrix")
print(metrics.confusion_matrix(y_test_both, y_pred))

# Logistic Regression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(solver='lbfgs', max_iter=10000)

# fit the model with data
logreg.fit(X_train_benign,y_train_benign)

#
y_pred=logreg.predict(X_test_both)

# Model Accuracy, how often is the classifier correct?
print("LR Accuracy:",metrics.accuracy_score(y_test_both, y_pred))

# View the classification report for test data and predictions
print("LR CLassification Report")
print(classification_report(y_test_both, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89']))

print("LR Confusion Metrix")
print(metrics.confusion_matrix(y_test_both, y_pred))
