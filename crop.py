# -*- coding: utf-8 -*-0
"""
Created on Tue Jul 16 12:24:29 2024

@author: KRISH
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:05:29 2024

@author: KRISH
"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
import pandas as pd
df = pd.read_csv(r"C:\Users\KRISH\Downloads\archive (2)\Crop_recommendation.csv")
print(df)

#pre0processing
#print(df.isna.sum())
#print(df.isnull.sum())
#info
#print(df.corr())



#extracting features and target

x = df.drop('label' , axis = 1)
y = df['label']


from sklearn.preprocessing import LabelEncoder

l = LabelEncoder()
q =l.fit_transform(df['label'])

print(q)



#Splitting

x_train , x_test , y_train , y_test = tts(x , y , train_size= 0.8)



#RandomForest Classifier
from sklearn.ensemble import RandomForestClassifier 

r = RandomForestClassifier()


r.fit(x_train , y_train)
pred = r.predict(x_test)

from sklearn.metrics import accuracy_score 
acc = accuracy_score(pred, y_test)

#confusion matrix
from sklearn.metrics import confusion_matrix
con = confusion_matrix(pred, y_test)
#print(con)


#classification report
#confusion matrix
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred , y_test) 
# print(acc)
# connectivity
import pickle

with open("Model.pkl" , "wb") as file:
    pickle.dump(r ,file)  #pickle.dump(source , destination)  -> syntax
    
    
#EDA
'''
print("\nUnique values in 'label' column (Crop Types):")
print(df['label'].unique())


# Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title("Correlation Matrix")
plt.show() '''

# Pairplot to visualize feature relationships
sns.pairplot(df, hue="label", palette="Set1", plot_kws={'alpha': 0.6})
plt.suptitle("Pairplot of Features", y=1.02)
plt.show()



# Box plots to detect outliers
plt.figure(figsize=(15, 10))
for i, col in enumerate(features, 1):
    plt.subplot(3, 3, i)
    sns.boxplot(data=df, y=col)
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()
'''
# Scatter plots for relationships with label
plt.figure(figsize=(15, 10))
for i, col in enumerate(features, 1):
    plt.subplot(3, 3, i)
    sns.scatterplot(data=df, x=col, y="label")
    plt.title(f"Scatter plot of {col} vs Label")
plt.tight_layout()
plt.show()

# Display any feature correlations with the target (if applicable)
if 'label' in df.columns:
    label_encoder = LabelEncoder()
    df['label_encoded'] = label_encoder.fit_transform(df['label'])
    correlations = df.corr()['label_encoded'].sort_values(ascending=False)
    print("\nCorrelations of features with the label:")
    print(correlations)
    '''