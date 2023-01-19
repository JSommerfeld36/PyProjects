#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:22:50 2023

@author: joelsommerfeld
"""

import yfinance as yf

# Define the stock symbol and the date range for the historical data
stock_symbol = 'AAPL'
start_date = '2010-01-01'
end_date = '2020-12-31'

# Download the historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Print the first few rows of the data
print(stock_data.head())

from sklearn.model_selection import train_test_split

# Divide the data into input and output variables
# I will assume that you have the closing price of the stock in the 'Close' column
X = stock_data.drop(['Close'], axis=1) 
y = stock_data[['Close']]

# Split the data into training and test sets
# I will use 80% of the data for training and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


import torch
import torch.nn as nn

# Define the number of units in the LSTM layer and the number of features in the input data
units = 50
features = 5
num_epochs = 1

# Reshape the input data into the shape (sequence_length, batch_size, features)
X_train = torch.from_numpy(X_train.values).float()
X_train = X_train.view(-1, 1, features)

# Create the LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.fc(x[-1])
        return x

model = LSTMModel(input_size=features, hidden_size=units, num_layers=1, output_size=1)

# Define the loss function and the optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

# Train the model
for i in range(num_epochs):
    # Forward pass
    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

import matplotlib.pyplot as plt

# Make predictions on the test data
X_test = torch.from_numpy(X_test.values).float()
y_pred = model(X_test)

# Plot the predicted and actual stock prices
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred.detach().numpy(), label='Predicted')
plt.legend()
plt.show()


# The reason for this crash could be that the output of the model is not the same shape as the expected output, this can happen if the input data is not preprocessed or if the model architecture is not suitable for the data.

# You can check the shapes of the input and output data before passing them to the model, and make sure they match.

# Another reason could be that the model's output has too big values, which can cause overflow errors, in this case, you can try normalizing the data before passing it to the model, and un-normalize the output to get the real values.

# Also, you can check the performance of your model by plotting the training and validation loss during the training process. This will allow you to detect if the model is overfitting or underfitting, and make the necessary adjustments to improve the performance.

# You can also try to reduce the number of epochs and see if that solves the problem.