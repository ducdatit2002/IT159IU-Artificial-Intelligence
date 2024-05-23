import pandas as pd
from naiveBayesClassifier import NaiveBayesFilter
import numpy, sys

#Load the data

filepath = 'SMSSpamCollection.csv'
df = pd.read_csv(filepath, sep='\t', header=None, names=['Label', 'SMS'])

print(df.shape)
print("------------------BEFORE CLEANING DATA-------------------------")
print(df.head())

#Load message and label; then split it to train and test set
X = df['SMS']
y = df['Label']
print('Total message: ', len(y))
# Randomize the dataset
data_randomized = df.sample(frac=1, random_state=1)

# Calculate index for split
training_test_index = round(len(data_randomized) * 0.8)
print('training_test_index: ', training_test_index)

# Training/Test split
training_set = data_randomized[:training_test_index].reset_index(drop=True)
test_set = data_randomized[training_test_index:].reset_index(drop=True)


X_train = training_set['SMS']
y_train = training_set['Label']

X_test = test_set['SMS']
y_test = test_set['Label']
print('Length of test data: ', len(X_test))

#Remove all punctuation marks
X_train = X_train.str.replace('\W', ' ')
#Change all letters to small case
X_train = X_train.str.lower()
#split the sms column on white space and convert each row to a list
X_train = X_train.str.split()



#Remove all punctuation marks
X_test = X_test.str.replace('\W', ' ')
#Change all letters to small case
X_test = X_test.str.lower()
#split the sms column on white space and convert each row to a list
X_test = X_test.str.split()


print("----AFTER CLEANING AND SPLIT TRAIN AND TEST DATA----")
print(X_train.head())

NB = NaiveBayesFilter()

#==========Training the Naive Bayes====
NB.fit(X_train, y_train)
predict_labels_train = NB.predict(X_train)
recall_train = NB.score(y_train, predict_labels_train)
print("recall train of NB: ", recall_train)


#=========Testing the Naive Bayes======
NB.predict_proba(X_test)
predict_labels_test = NB.predict(X_test)
recall_test = NB.score(y_test, predict_labels_test)
print("recall test of NB: ", recall_test)








