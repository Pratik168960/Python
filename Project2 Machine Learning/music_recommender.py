# Import the necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. Import the data from the CSV file
music_data = pd.read_csv('music.csv')

# 2. Split the data into Input (X) and Output (y)
# X contains only the features (age, gender), y contains only the answers (genre)
X = music_data.drop(columns=['genre'])
y = music_data['genre']

# 3. Create a new instance of the Decision Tree model
model = DecisionTreeClassifier()

# 4. Train the model using our input and output data
model.fit(X, y)

# 5. Make predictions (e.g., predicting for a 21-year-old male and 22-year-old female)
predictions = model.predict([ [21, 1], [22, 0] ])

# 6. Output the predictions
print(f"The model predicts these users will like: {predictions}")