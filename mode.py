from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Assuming 'target_column' is the column you want to predict
X = data.drop('target_column', axis=1)
y = data['target_column']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
