# if __name__=="__main__":
#     #Question 2: Visualize Data
#     # Get the filename from the command line argument
#     filename = sys.argv[1]

#     # Load the data from the CSV file
#     data = pd.read_csv(filename)

#     # Create a plot
#     plt.figure(figsize=(10, 6))
#     plt.plot(data['year'], data['days'])
#     plt.xlabel('Year')
#     plt.ylabel('Number of Frozen Days')
#     plt.title('Lake Mendota Ice Cover')
#     plt.grid(True)

#     # Save the plot as plot.jpg
#     plt.savefig("plot.jpg")



#     #Question 3: Linear Regression
#     #4.1 Q3a - Represent the data as matrix X:
#     data = pd.read_csv("hw5.csv")

#     # Extract the 'year' as X and transform it into a matrix
#     X = np.column_stack((np.ones(len(data)), data['year'].values))

#     print("Q3a:")
#     print(X.astype(np.int64))

#     #4.2 Q3b - Place the corresponding yi values into a vector Y:
#     Y = data['days'].values

#     print("Q3b:")
#     print(Y.astype(np.int64))

#     #4.3 Q3c - Compute the matrix product Z = XT X:
#     Z = np.dot(X.T, X)

#     print("Q3c:")
#     print(Z.astype(np.int64))

#     #4.4 Q3d - Compute the inverse of XT X (I):
#     I = np.linalg.inv(Z)

#     print("Q3d:")
#     print(I)

#     #4.5 Q3e - Compute the pseudo-inverse of X (PI):
#     PI = np.linalg.pinv(X)

#     print("Q3e:")
#     print(PI)

#     #4.6 Q3f - Compute the coefficients ˆβ:
#     beta_hat = np.dot(np.dot(I, X.T), Y)

#     print("Q3f:")
#     print(beta_hat)

#     #Question 4: Prediction
#     # Using the estimated coefficients, predict the number of ice days for 2022-23
#     x_test = 2022  # Test year
#     y_test = beta_hat[0] + beta_hat[1] * x_test  # Predicted number of ice days for 2022-23

#     print("Q4: " + str(y_test))

#     #Question 5: Model Interpretation
#     #a
#     beta1_sign = ">" if beta_hat[1] > 0 else "<" if beta_hat[1] < 0 else "="

#     print("Q5a: " + beta1_sign)

#     #b
#     interpretation = "The sign of β1 indicates the direction of the relationship between the year and the number of ice days on Lake Mendota. "
#     if beta_hat[1] > 0:
#         interpretation += "A greater than sign (>) means that as the year increases, the number of ice days is expected to increase."
#     elif beta_hat[1] < 0:
#         interpretation += "A less than sign (<) means that as the year increases, the number of ice days is expected to decrease."
#     else:
#         interpretation += "A equal sign (=) means that there is no significant linear relationship between the year and the number of ice days."

#     print("Q5b: " + interpretation)


#     #Question 6: Model Limitation
#     #a
#     x_star = -beta_hat[0] / beta_hat[1]

#     print("Q6a: " + str(x_star))

#     #b
#     explanation = "The predicted year x∗ represents an estimate of when Lake Mendota will no longer freeze based on the linear regression model using the data in 'hw5.csv'. However, it's essential to note that this prediction has limitations. It assumes a linear trend in the data, which may not capture the complex and potentially nonlinear patterns of ice formation and thawing in the lake. Additionally, there could be external factors, such as climate change, that might influence the trends in Lake Mendota's ice cover. Therefore, while x∗ provides an estimate, it should be interpreted with caution and considered as a simplified projection rather than a definitive forecast."

#     print("Q6b: " + explanation)


#Question 2: Visualize Data
# # Get the filename from the command line argument
# filename = sys.argv[1]

# # Load the data from the CSV file
# data = pd.read_csv(filename)

# # Create a plot
# plt.figure(figsize=(10, 6))
# plt.plot(data['year'], data['days'])
# plt.xlabel('Year')
# plt.ylabel('Number of Frozen Days')
# plt.title('Lake Mendota Ice Cover')
# plt.grid(True)

# # Save the plot as plot.jpg
# plt.savefig("/Users/yash/Desktop/School/VSCode/hw5/plotTest.jpg")