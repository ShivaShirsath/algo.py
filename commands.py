Assingment 1(DATA WRANGLING)
#.............
import pandas as pd
import numpy as np
dataset=pd.read_csv("/content/archive (1).zip")
dataset
#..........
dataset.shape
#.............
dataset.head(5)
#...........
dataset.tail(10)
#...........
dataset.index
#..........
dataset.columns
#.........
dataset.dtypes
#.........
dataset['5.1']
#..........
dataset.T
#..............
dataset.transpose
#............
dataset.isnull()
#.............
dataset.notnull()
#..............
dataset.notnull().sum()
#...............
dataset.notnull().sum().sum()
#......................
dataset.iloc[1:100]
#...............
dataset.iloc[3:5, :2]
#..............
dataset.iloc[2:3, 1:2]
#...........
dataset.iloc[2,1]
#...............
dataset.iloc[[2,3,5],[0,2]]
#....................
dataset.rename(columns={"Sepal.Width":"Length"},inplace=True)
dataset
---------------------------------------------------------------------------------------------------------------------------------2

Assingment 2  (DATA WRANGLING 2)
import pandas as pd
import numpy as np

dataset=pd.read_csv("/content/studentinfo.csv")
dataset
#.................
dataset.dropna()
#................
dataset.dropna().shape
#.............
dataset.dropna(axis=1)
#............
dataset.dropna(how='any')
#...........
dataset.dropna(how='all').shape
#.............
dataset.dropna(subset=['WT'])
#...............
dataset.fillna(0)
#................
dataset['AI'].fillna(method='ffill')
#.................
dataset['DS&BDA'].fillna(method='bfill')
#................
dataset.isnull().sum()
#.............
import seaborn as sns
sns.boxplot(y=dataset['WT'])
#.................
import pandas as pd
import numpy as np
dataset=pd.read_csv("/content/studentinfo.csv")
dataset
#...................
df2=dataset.drop(dataset.index[dataset['WT']>=120])
#.................
import matplotlib.pyplot as plt
#............
plt.hist(df2['WT'], bins = 9)
plt.show()
#...............
import numpy as np
df2.insert(len(df2.columns), 'WT1',
         np.log(df2['Roll No']))
#.................
df2
#..............
plt.hist(df2['WT'], bins = 9)
plt.show()

--------------------------------------------------------------------------------------------------------------------------------3

Assingment 3 (DISCRIPTIVE STATISTICS)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from math import sqrt
import ipywidgets as widgets
from ipywidgets import interact
from ipywidgets import interact_manual
#......................................
data = pd.read_csv('/content/xAPI-Edu-Data.csv')
#...................................
data.head(20)
#...............................
mean = np.mean(data["WT"])
print(mean)
#.................................
median = np.median(data['Roll No'])
print(median)
#.............................
from statistics import mode
print("Mode is:",mode(data['WT']))
#................................
import numpy as np
x=[2,4,6,7,20,10,22]
y=np.array(data['WT'])
#................................
data['WT'].min()
#..........................
data['WT'].max()
#..........................
variance = data['WT'].var()
print(variance)
#.......................
std = sqrt(variance)
print(std)
#....................
gk = data.groupby('WT')
gk.first()
#..................
gkk = data.groupby(['WT', 'AI'])
gkk.first()

-------------------------------------------------------------------------------------------------------------------------4
Assingment 4(DATA ANALYTICS 1)

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing Data
from sklearn.datasets import load_boston
boston = load_boston()
#......................................
boston.data.shape
#..........................
boston.feature_names
#...........................
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names

data.head(10)
#..............................

# Adding 'Price' (target) column to the data
boston.target.shape
#.................................
data['Price'] = boston.target
data.head()
#..................................
data.describe()
#..............................
data.info()
#.................


# Input Data
x = boston.data


# Output Data
y = boston.target


# splitting data to training and testing dataset.

#from sklearn.cross_validation import train_test_split
#the submodule cross_validation is renamed and reprecated to model_selection

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size =0.2,
													random_state = 0)

print("xtrain shape : ", xtrain.shape)
print("xtest shape : ", xtest.shape)
print("ytrain shape : ", ytrain.shape)
print("ytest shape : ", ytest.shape)

#...............................

# Fitting Multi Linear regression model to training model

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain, ytrain)

# predicting the test set results
y_pred = regressor.predict(xtest)

#...............................

# Plotting Scatter graph to show the prediction
# results - 'ytrue' value vs 'y_pred' value
plt.scatter(ytest, y_pred, c = 'green')
plt.xlabel("Price: in $1000's")
plt.ylabel("Predicted value")
plt.title("True value vs predicted value : Linear Regression")
plt.show()
#..............................
# Results of Linear Regression.
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(ytest, y_pred)
print("Mean Square Error : ", mse)

---------------------------------------------------------------------------------------------------------------------------------------------------5

Assingment 5 (DATA ANALYTICS 2)
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#.......................................
dataset = pd.read_csv(r'C:\Users\admin\Desktop\Logistic-Regression-Social-Network-Ads-master\Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values
#........................................
dataset.describe()
#.....................................
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
#........................................
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#...........................................
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(random_state = 0)
log_reg.fit(X_train, y_train)
#...........................................
y_pred = log_reg.predict(X_test)
#............................................
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
#..............................................
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, log_reg.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Logistic Regression (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
#..........................................
from sklearn.svm import SVC

svm = SVC(kernel='rbf', random_state=0)
svm.fit(X_train, y_train)

predicted = svm.predict(X_test)

cm = confusion_matrix(y_test, predicted)
plt.clf()
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
classNames = ['Negative','Positive']
plt.title('SVM RBF Kernel Confusion Matrix - Test Data')
plt.ylabel('True label')
plt.xlabel('Predicted label')
tick_marks = np.arange(len(classNames))
plt.xticks(tick_marks, classNames, rotation=45)
plt.yticks(tick_marks, classNames)
s = [['TN','FP'], ['FN', 'TP']]

for i in range(2):
    for j in range(2):
        plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))
plt.show()
#..................................................
print(accuracy_score(y_test, predicted))
#..................................................
precision = precision_score(y_test, predicted, average='macro')
print("precision")
print(precision)

------------------------------------------------------------------------------------------------------------------------------------6

ASSIGNMENT NO. 6(DATA ANALYTICS 3)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1=pd.read_csv('iris.csv')
df1
#..............................
df=pd.DataFrame(df1)
df.head()
#.........................
df.describe()
#.......................
df.info()
#...............
df.columns
#...............
sns.jointplot(x='SepalWidthCm',y='SepalLengthCm',data=df,hue='Species')
#..............................
sns.jointplot(x='PetalWidthCm',y='PetalLengthCm',data=df,hue='Species')
#..............................
sns.pairplot(data=df,hue='Species')
#.............................................
from sklearn.model_selection import train_test_split
X=df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
Y=df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
from sklearn.naive_bayes import MultinomialNB
nb=MultinomialNB()
nb.fit(X_train,y_train)
predictions=nb.predict(X_test)
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
print('Classification Report')
print('\n')
print(classification_report(y_test,predictions))
#......................................................................
print('Accuracy')
print(accuracy_score(y_test,predictions))
#.........................................................
print('Confusion Matrix')
print('\n')
print(confusion_matrix(y_test,predictions))
#.........................................................

.----------------------------------------------------------------------------------------------------------------------------------------------------7

ASSIGNMENT NO 7 (TEST ANALYTICS)

import nltk
nltk.download('punkt') 

#...............................................................................
from nltk.tokenize import sent_tokenize 
text = "Hello everyone. Welcome to NLP and the NLTK module introduction" 
sent_tokenize(text) 
#.......................................
from nltk.tokenize import word_tokenize 
text = "Hello everyone. Welcome to NLP and the NLTK module introduction" 
word_tokenize(text) 
#........................................
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

#............................................................
txt = "Sukanya, Rajib and Naba are my good friends. " \
    "Sukanya is getting married next year. " \
    "Marriage is a big step in oneâ€™s life." \
    "It is both exciting and frightening. " \
    "But friendship is a sacred bond between people." \
    "It is a special kind of love between us. " \
    "Many of you must have tried searching for a friend "\
    "but never found the right one."


tokenized = sent_tokenize(txt)

for i in tokenized:
     
    # Word tokenizers is used to find the words
    # and punctuation in a string
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    #  Using a Tagger. Which is part-of-speech
    # tagger or POS-tagger.
    tagged = nltk.pos_tag(wordsList)
 
    print(tagged)
#................................
nltk.download('wordnet')

# import these modules
from nltk.stem import WordNetLemmatizer
 
lemmatizer = WordNetLemmatizer()
 
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
 
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))
#...................................................
import nltk
from nltk.stem import PorterStemmer
words=["python","pythoner","pythoning","pythoned","pythonly"]
ps=PorterStemmer( )
for word in words:
  print(f"{word}: {ps.stem(word)}")
#.......................................................
# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
# assign documents
d0 = 'Geeks for the an meeting of using geeks'
d1 = 'Geeks'
d2 = 'r2j use for the purpose of  '
  
# merge documents into a single corpus
string = [d0, d1, d2]


# create object
tfidf = TfidfVectorizer()
  
# get tf-df values
result = tfidf.fit_transform(string)
print('\nidf values:')
for ele1, ele2 in zip(tfidf.get_feature_names(), tfidf.idf_):
    print(ele1, ':', ele2)
#................................................
# get indexing
print('\nWord indexes:')
print(tfidf.vocabulary_)
#...........................................
# display tf-idf values
print('\ntf-idf value:')
print(result)
#..................................................
# in matrix form
print('\ntf-idf values in matrix form:')
print(result.toarray())
#....................................

----------------------------------------------------------------------------------------------------------------------------------------------------8

ASSIGNMENT NO 8. (DATA VISUALIZATION 1)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
#..........................
dataset = sns.load_dataset('titanic') 
dataset.head() 
#...........................
sns.distplot (x = dataset['age'], bins = 10) 
#...........................
sns.distplot (dataset['age'], bins = 10, kde=False) 
#...........................
sns.jointplot (x = dataset['age'], y = dataset['fare'], kind = 'hex')
#...........................
sns.rugplot (dataset['fare'])
#...........................
sns.barplot (x='sex', y='age', data=dataset)
#............................
sns.barplot (x='sex', y='age', data=dataset, estimator=np.std) 
#............................
sns.countplot (x='sex', data=dataset)
#.............................
sns.boxplot (x='sex', y='age', data=dataset)
#.............................
sns.boxplot (x='sex', y='age', data=dataset, hue="survived") 
#.............................
sns.violinplot (x='sex', y='age', data=dataset)
#..............................
sns.violinplot (x='sex', y='age', data=dataset, hue='survived') 
#...............................
sns.stripplot (x='sex', y='age', data=dataset, jitter=True)
#...............................
sns.stripplot (x='sex', y='age', data=dataset, jitter=False) 
#...............................
sns.swarmplot (x='sex', y='age', data=dataset) 
#...............................
sns.swarmplot (x='sex', y='age', data=dataset, hue='survived')
#...............................
--------------------------------------------------------------------------------------------------------------------------------------9
ASSIGNMENT NO 9 (DATA VISUALIZATION 2)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
#................................
dataset = sns.load_dataset('titanic') 
#...............................
dataset
#...........................
sns.boxplot(x="sex", y="age" , data=dataset)
#...............................
sns.boxplot(x="sex", y="age" , data=dataset, hue="survived")
#.................................

-------------------------------------------------------------------------------------------------------------------------------10
ASSIGNMENT NO 10 (DATA VISUALIZATION 3)

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline
#................................
dataset = sns.load_dataset('iris') 
#..............................
dataset
#................................
df=pd.DataFrame(dataset)
#............................
df.head(10)
#.................................
df.info()
#..............................
df.columns
#......................
len(list(df))
#....................
df["sepal_length"].max()
#................................
df["sepal_length"].min()
#.............................
df["sepal_length"].hist(bins=30)
#................................
df["sepal_width"].hist(bins=30)
#.................................
df["petal_length"].hist(bins=30)
#...............................
df["sepal_width"].hist(bins=30)
#................................
df["species"].hist(bins=30)
#.................................
sns.boxplot("sepal_length" , data=dataset)
#.................................
sns.boxplot("sepal_width" , data=dataset)
#...............................
sns.boxplot("petal_length" , data=dataset)

