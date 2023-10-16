import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Question 1: Data Curation
# Specify the input and output file paths
# input_file_path = "/Users/yash/Desktop/School/VSCode/hw5/hw5.csv"
# output_file_path = "/Users/yash/Desktop/School/VSCode/hw5/hw5Text.csv"

# # Open the input and output files
# with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
#     # Write the header to the output file
#     output_file.write("years,days\n")

#     # Skip the header line in the input file
#     next(input_file)

#     # Process each line of the input file
#     for line in input_file:
#         # Split the line into columns
#         columns = line.strip().split("\t")

#         # Extract the relevant information and write it to the output file
#         years = columns[0].split("-")[0]
#         days = columns[3]
#         # print(days)
#         if (days != '–'):
#             output_file.write(f"{years},{days}\n")
#         else:
#             print(years+","+days)

# print("Reformatted data has been written to", output_file_path)

if __name__ == "__main__":
    # Question 2: Visualize Data
    #filename = sys.argv[1]
    filename = "hw5.csv"


    # Load the data from the CSV file
    data = pd.read_csv(filename)

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(data['year'], data['days'])
    plt.xlabel('Year')
    plt.ylabel('Number of Frozen Days')
    plt.title('Lake Mendota Ice Cover')
    plt.grid(True)

    # Save the plot as plot.jpg
    plt.savefig("plot.jpg")

    # Question 3: Linear Regression
    #data = pd.read_csv("hw5.csv")
    data = pd.read_csv("toy.csv")
    
    # Extract the 'year' and 'days' values
    years = data['year'].values
    days = data['days'].values
    
    # Calculate the number of data points (n)
    n = len(years)
    
    # Create the design matrix X
    X = np.column_stack((np.ones(n), years))
    
    # Compute the vector Y
    Y = days
    
    # Calculate X^T
    X_T = X.T
    
    # Calculate X^T * X
    X_T_X = np.dot(X_T, X)
    
    # Calculate the inverse of X^T * X
    X_T_X_inv = np.linalg.inv(X_T_X)
    
    # Calculate X^T * Y
    X_T_Y = np.dot(X_T, Y)
    
    # Calculate the coefficients beta_hat
    beta_hat = np.dot(X_T_X_inv, X_T_Y)
    
    # Print the values for Q3
    print("Q3a:")
    print(X.astype(np.int64))
    print("Q3b:")
    print(Y.astype(np.int64))
    print("Q3c:")
    print(X_T_X.astype(np.int64))
    print("Q3d:")
    print(X_T_X_inv)
    print("Q3e:")
    #print(np.dot(X_T_X_inv, X_T).astype(np.int64))
    print(np.dot(X_T_X_inv, X_T))
    print("Q3f:")
    print(beta_hat)

    # Question 4: Prediction
    x_test = 2022
    y_test = beta_hat[0] + beta_hat[1] * x_test

    print("Q4: " + str(y_test))

    # Question 5: Model Interpretation
    beta1_sign = ">" if beta_hat[1] > 0 else "<" if beta_hat[1] < 0 else "="
    
    print("Q5a: " + beta1_sign)

    interpretation = "The sign of beta1 suggests the direction of the relationship between the year and the number of ice days. "
    
    if beta_hat[1] > 0:
        interpretation += "A greater than sign (>) implies that as the year increases, the number of ice days is expected to increase."
    elif beta_hat[1] < 0:
        interpretation += "A less than sign (<) implies that as the year increases, the number of ice days is expected to decrease."
    else:
        interpretation += "An equal sign (=) suggests no significant linear relationship between the year and the number of ice days."
    
    print("Q5b: " + interpretation)

    # Question 6: Model Limitation
    x_star = -beta_hat[0] / beta_hat[1]
    
    print("Q6a: " + str(x_star))

    explanation = "The predicted year x* represents an estimate of when Lake Mendota will no longer freeze based on the linear regression model. However, it's essential to note that this prediction has limitations. It assumes a linear trend in the data, which may not capture the complex and potentially nonlinear patterns of ice formation and thawing in the lake. Additionally, external factors, such as climate change, could influence trends in Lake Mendota's ice cover. Therefore, while x* provides an estimate, it should be interpreted with caution and considered as a simplified projection."

    print("Q6b: " + explanation)
