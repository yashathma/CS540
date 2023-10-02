from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    # Your implementation goes here!
    data = np.load(filename)
    data = data-np.mean(data,axis=0)
    return data

def get_covariance(dataset):
    # Your implementation goes here!
    left = np.dot(np.transpose(dataset), dataset)
    right = 1/(len(dataset)-1)
    covariance_data = np.multiply(left, right)
    return covariance_data

def get_eig(S, m):
    # Your implementation goes here!
    final_eigen = np.zeros((m,m))

    values, vectors = eigh(S, subset_by_index=[len(S)-m, len(S)-1])
    new_values = np.flip(values)

    for i in range(m):
            final_eigen[i][i] = new_values[i]

    return final_eigen, np.fliplr(vectors)

def get_eig_prop(S, prop):
    # Your implementation goes here!
    eig_values = eigh(S, subset_by_index=[0, len(S)-1], eigvals_only=True)
    sum_of_eig_values = np.sum(eig_values)
    minimum_value = prop*sum_of_eig_values

    minimum_eigen_values, minimum_eigen_vectors = eigh(S, subset_by_value=[minimum_value, np.inf])
    minimum_eigen_values = np.flip(minimum_eigen_values)
    minimum_eigen_vectors = np.fliplr(minimum_eigen_vectors)

    set_values = np.zeros((len(minimum_eigen_values), len(minimum_eigen_values)))

    for i in range(len(minimum_eigen_values)):
         set_values[i][i] = minimum_eigen_values[i]
    return set_values, minimum_eigen_vectors

def project_image(image, U):
    # Your implementation goes here!
    return np.dot(U,np.dot(np.transpose(U), image))

def display_image(orig, proj):
    # Your implementation goes here!
    # Please use the format below to ensure grading consistency
    # fig, (ax1, ax2) = plt.subplots(figsize=(9,3), ncols=2)
    # return fig, ax1, ax2

    original = np.rot90(np.reshape(orig, (32, 32)), k=3)
    projection = np.rot90(np.reshape(proj, (32, 32)), k=3)

    fig, (ax1,ax2) = plt.subplots(figsize=(9,3), ncols=2)

    ax1.set_title("Original")
    ax2.set_title("Projection")
    original_ax1 = ax1.imshow(original, aspect = "equal")
    projection_ax2 = ax2.imshow(projection, aspect = "equal")
    fig.colorbar(original_ax1, ax=ax1)
    fig.colorbar(projection_ax2, ax=ax2)
    return fig, ax1, ax2