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

dataset = pd.read_csv('C:\\Users\\User\\Desktop\\Java\\codes\\Cleaned\\dataset.csv', index_col=0)

#Data cleaning and preprocessing

lemmatizer = WordNetLemmatizer()

corpus = []
for i in range(0, len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', str(dataset['code'][i]))
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review] # add lemmatization
    review = ' '.join(review)
    corpus.append(review)
  
# TFIDF Model 

tf_idf = TfidfVectorizer()
X = tf_idf.fit_transform(corpus).toarray()

# Set y value

y=dataset.category

# Train Test Split

# X.shape
# y.shape
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=1)


# Training model using RF

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("RF Accuracy:",metrics.accuracy_score(y_test, y_pred))

# View the classification report for test data and predictions
print("RF CLassification Report")
print(classification_report(y_test, y_pred,target_names=['CWE15','CWE23','CWE36','CWE78','CWE89','CWE80','CWE113','CWE129','Non-Vuln']))

print("RF Confusion Metrix")
print(metrics.confusion_matrix(y_test, y_pred))


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get and reshape confusion matrix data
matrix = confusion_matrix(y_test, y_pred)
matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]

# Build the plot
plt.figure(figsize=(16,7))
sns.set(font_scale=1.4)
sns.heatmap(matrix, annot=True, annot_kws={'size':10},
            cmap=plt.cm.Greens, linewidths=0.2)

# Add labels to the plot
class_names = ['CWE15', 'CWE29', 'CWE36', 'CWE78', 'CWE89','CWE80','CWE113','CWE129','Non-Vuln']
tick_marks = np.arange(len(class_names))
tick_marks2 = tick_marks + 0.5
plt.xticks(tick_marks, class_names, rotation=25)
plt.yticks(tick_marks2, class_names, rotation=0)
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.title('Confusion Matrix for Random Forest Model')
plt.show()


# SVM

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("SVM Accuracy:",metrics.accuracy_score(y_test, y_pred))

# View the classification report for test data and predictions
print("SVM CLassification Report")
print(classification_report(y_test, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89', 'CWE80','CWE113','CWE129','Non-Vuln']))

print("SVM Confusion Metrix")
print(metrics.confusion_matrix(y_test, y_pred))

# NB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("NB Accuracy:",metrics.accuracy_score(y_test, y_pred))

# View the classification report for test data and predictions
print("NB CLassification Report")
print(classification_report(y_test, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89', 'CWE80','CWE113','CWE129','Non-Vuln']))

print("NB Confusion Metrix")
print(metrics.confusion_matrix(y_test, y_pred))


# Logistic Regression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(solver='lbfgs', max_iter=10000)

# fit the model with data
logreg.fit(X_train,y_train)

#
y_pred=logreg.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("LR Accuracy:",metrics.accuracy_score(y_test, y_pred))

# View the classification report for test data and predictions
print("LR CLassification Report")
print(classification_report(y_test, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89', 'CWE80','CWE113','CWE129','Non-Vuln']))

print("LR Confusion Metrix")
print(metrics.confusion_matrix(y_test, y_pred))

# KNN

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("KNN Accuracy:",metrics.accuracy_score(y_test, y_pred))

# View the classification report for test data and predictions
print("KNN CLassification Report")
print(classification_report(y_test, y_pred,target_names=['CWE15', 'CWE23','CWE36','CWE78','CWE89', 'CWE80','CWE113','CWE129','Non-Vuln']))

print("KNN Confusion Metrix")
print(metrics.confusion_matrix(y_test, y_pred))






