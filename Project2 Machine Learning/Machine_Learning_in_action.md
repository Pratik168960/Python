# Machine Learning Pipeline Example

This markdown file demonstrates the 7 steps of a basic Machine Learning pipeline using Python, `pandas`, and `scikit-learn`. We will load a dataset, clean it, split it into training and testing sets, create a Decision Tree model, train it, make predictions, and evaluate its accuracy.

### 1. Import the Data

We start by loading our dataset into a `pandas` DataFrame. Let's assume we have a file called `music.csv` containing user data (like age and gender) and the genre of music they like.

```python
import pandas as pd

# Load the dataset
music_data = pd.read_csv('music.csv')
```

### 2. Clean the Data

Real-world datasets often have missing or messy data. For this example, let's assume our data is clean, but a common step would be to drop empty rows:

```python
# Drop rows with missing values (if any)
# music_data = music_data.dropna()
```

### 3. Split the Data into Training and Testing Sets

We need to separate our data into features (inputs, like age and gender) and the target variable (what we want to predict, like the genre). Then, we split these into training and testing sets to evaluate our model later.

```python
from sklearn.model_selection import train_test_split

# Separate features (X) and target (y)
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# Split into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

### 4. Create a Model

We choose a Machine Learning algorithm. For this example, we will use a Decision Tree Classifier.

```python
from sklearn.tree import DecisionTreeClassifier

# Initialize the model
model = DecisionTreeClassifier()
```

### 5. Train the Model

We train the model using our training data so it can learn the relationship between the features and the target.

```python
# Train the model
model.fit(X_train, y_train)
```

### 6. Make Predictions

Now, we use the trained model to predict the genres for our testing data.

```python
# Make predictions on the test set
predictions = model.predict(X_test)
```

### 7. Evaluate and Improve

Finally, we compare the model's predictions with the actual genres in the test set to calculate its accuracy.

```python
from sklearn.metrics import accuracy_score

# Calculate accuracy
score = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {score * 100:.2f}%")
```

---
*This is a basic example. Real-world machine learning involves more complex data cleaning, feature engineering, and model tuning.*