# Project Report
## Data Preparation
The dataset consisted of labelled text samples across multiple languages, including English, Swahili, Kikuyu, Somali and Sheng. The data was cleaned and balanced to reduce class bias and ensure fair model evaluation. Sheng sentences were rare to find and to balance the dataset,  other languages were downsampled to match Sheng(1039 sentences).

## Preprocessing
Text normalization was applied to improve consistency and reduce noise:
1. Conversion to lowercase 
2.  Unicode normalization (removal of diacritics, particularly for Kikuyu) 
3. Removal of irregular character variations 
4. Lightweight Sheng normalization to standardize spelling and slang variants while preserving linguistic identity 
This step ensured that variations of the same word were treated as a single feature without altering the underlying language. This is of course not the case with Kikuyu dataset as ASCII normalization stripped it of diacritics, for this trade-off was deliberate.

## Feature Extraction
Text data was transformed using TF-IDF vectorization with character n-grams.
1. Analyzer: Character-level 
2. N-gram range: (1–5) 

Character n-grams were selected because they are effective for language detection, especially in handling:
1. Short text inputs 
2. Spelling variation 
3. Code-mixed language (in this case, Sheng) 

## Model Training
The dataset was split into training and testing sets. Three models were trained:
1. Logistic Regression 
2. Linear SVM 
3. Naive Bayes 

Each model was evaluated using accuracy on the test set.

### Accuracy Comparison
  Model  -> 	Accuracy
1. Logistic Regression -> 0.9846
2. Linear SVM	-> 0.9894
3. Naive Bayes	-> 0.9423

Linear SVM achieved the highest overall accuracy and was initially selected as the primary model for the system.

## Model Behavior and Observations
Although Naive Bayes recorded the lowest overall accuracy, it demonstrated stronger performance on Sheng, a low-resource and highly variable language in the dataset. A sentence like “Rada bro, uko mboka kesho?”(What’s up bro, are you going to work tommorow?) was incorrectly detected as Swahili by Linear SVM while Naive Bayes correctly classified as Sheng.

This behavior can be attributed to:
1. Naive Bayes being more sensitive to distinctive lexical features (e.g., slang tokens) 
2. SVM prioritizing dominant patterns across all classes, which can lead to misclassification of mixed or informal inputs 

As a result, SVM performed better on well-represented languages (e.g., English, Swahili), while Naive Bayes showed improved detection of informal and less frequent patterns such as Sheng.

## Final Model Selection
The system supports both single-model inference and dual-model comparison (SVM and Naive Bayes).
1. Linear SVM  (for high overall accuracy)
2. Naive Bayes  (for improved detection of Sheng )

This dual-model approach allows the system to balance general performance with sensitivity to underrepresented linguistic patterns.

## Model Deployment
To reflect these differences, the user interface supports:
1. Selection between models during inference 
2. Optional comparison of predictions from both models 
