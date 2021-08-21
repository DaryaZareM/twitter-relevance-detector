# twitter-relatedness-analysis

in this code we used libebarys:
- tensorflow
- sklearn
- re
- nltk

### preprocessed:
preprocessed data was saved at dataF.csv which the punctuation, stopwords, and links have been removed from data and words have stemmed.
### models:
7 models have trained with oversampled data(to balance the number of class samples) and the prediction results for validation data was:

|model|accuracy|
|---|---|
|RNN|97%|
|CNN|96%|
|sequential NN model | 94%|
|Linear Support Vector Machine | 93%|
|Random Forest Classifier| 90%|
|Multinomial Navy Base| 88%|
|Logistic Regression | 84%|

![image](https://user-images.githubusercontent.com/51965862/128639691-ff695161-c74f-4a62-a37a-0b216743cbf9.png)

_________________________________________________________________

# more details about models:
random forest classification model max depth is equal to 5 and The number of trees in the forest is equal to 200.

and the summary of the sequential model is:

|Layer (type)        |         Output Shape        |      Param    |
|---|---|---|
|embedding (Embedding)|        (None, 100, 16)      |     160000    |
|global_average_pooling1d| (None, 16)          |      0        | 
|dense (Dense)        |        (None, 24)      |          408|
|dense_1 (Dense)      |        (None, 1)       |          25  |




