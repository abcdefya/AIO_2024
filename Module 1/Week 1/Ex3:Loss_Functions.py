import numpy as np
import random
import math

def calculate_mae(target, predict):
    """
    Calculate Mean Absolute Error (MAE)
    """
    return abs(target - predict)

def calculate_mse(target, predict):
    """
    Calculate Mean Squared Error (MSE)
    """
    return (target - predict) ** 2

def calculate_rmse(target, predict):
    """
    Calculate Root Mean Squared Error (RMSE)
    """
    mse = calculate_mse(target, predict)
    return math.sqrt(mse)

def main():
    num_samples = input("Enter the number of samples: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)
    loss_name = input("Enter the loss name (MAE, MSE, RMSE): ").upper()

    # Initialize lists for storing samples
    targets = []
    predicts = []
    losses = []

    # Generate random samples and calculate loss for each sample
    for i in range(num_samples):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        targets.append(target)
        predicts.append(predict)
        
        if loss_name == "MAE":
            loss = calculate_mae(target, predict)
        elif loss_name == "MSE":
            loss = calculate_mse(target, predict)
        elif loss_name == "RMSE":
            loss = calculate_rmse(target, predict)
        else:
            print("Invalid loss name")
            return
        
        losses.append(loss)
        
        print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")

if __name__ == "__main__":
    main()
