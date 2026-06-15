import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Size': [500, 800, 1200, 1500, 1800],
    'Price': [100000, 150000, 200000, 250000, 300000]
})
data

plt.scatter(data['Size'], data['Price'])
plt.xlabel('Size (sq ft)')
plt.ylabel('Price')
plt.title('House Price vs Size')
plt.show()

X = data[['Size']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)

predicted_price = model.predict([[1000]])
print("Predicted price for 1000 sq ft:", predicted_price[0])

plt.scatter(data['Size'], data['Price'])
plt.plot(data['Size'], model.predict(X))
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Prediction Line')
plt.show()