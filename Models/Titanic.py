import pandas as pd
import numpy as np
from sklearn.ensemble import *
from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
import scipy

startT = datetime.now()

print("1")
train = pd.DataFrame.from_csv('/home/melissa/A/data/train.csv')
test = pd.DataFrame.from_csv('/home/melissa/A/data/test.csv')
train = train[np.isfinite(train['Age'])]

print("2")
train_result = train[['Survived']]
train_data = train.ix[:, 1:11]  # 891 * 10

from sklearn import preprocessing


def convert_data(data):
    number = preprocessing.LabelEncoder()
    data['Pclass'] = number.fit_transform(data.Pclass)
    data['Name'] = number.fit_transform(data.Name)
    data['Sex'] = number.fit_transform(data.Sex)
    data['Age'] = number.fit_transform(data.Age)
    data['Parch'] = number.fit_transform(data.Parch)
    data['Ticket'] = number.fit_transform(data.Ticket)
    data['Fare'] = number.fit_transform(data.Fare)
    data['Cabin'] = data['Cabin'].factorize()[0]
    data['Cabin'] = number.fit_transform(data.Cabin)
    data['Embarked'] = data['Embarked'].factorize()[0]
    data['Embarked'] = number.fit_transform(data.Embarked)
    data = data.fillna(-999)
    return data


train_data = convert_data(train_data)
test = convert_data(test)

print("3")
rf = RandomForestClassifier(criterion='gini',
                            n_estimators=700,
                            min_samples_split=10,
                            min_samples_leaf=1,
                            max_features='auto',
                            oob_score=True,
                            random_state=1,
                            n_jobs=-1)
rf.fit(train_data, train_result)
test_result = rf.predict(test)
test = test.reset_index()
print("4")
df = pd.DataFrame(dict(PassengerId=test.PassengerId, Survived=test_result))
df.to_csv('/home/melissa/A/data/result.csv', sep=',', encoding='utf-8', index=False)


endT = datetime.now()
print("This run cost %s seconds " % (endT-startT).seconds)