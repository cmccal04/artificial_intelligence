# AI CS131 - Gardens of Heaven

import pandas as pd
import numpy as np

# Clean Data Step 1: Consolidation and Cleaning, using pandas
def load_and_clean_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Clean Data Step 2: Selection and Preprocessing
def select_and_preprocess(data):
    features = data.iloc[:, :-1].values # convert first three columns to NumPy array
    labels = data.iloc[:, -1].values # convert last column to NumPy array
    # compute mean and std to standardize features
    features_mean = np.mean(features, axis=0)
    features_std = np.std(features, axis=0)
    features_scaled = (features - features_mean) / features_std
    return features_scaled, labels, features_mean, features_std

# Clean Data Step 3: Transformation and Encoding
def transform_and_encode_labels(labels):
    unique_classes = np.unique(labels) # narrow labels to just the unique ones
    # Convert iris names to ints
    label_to_int = {label: i for i, label in enumerate(unique_classes)} 
    labels_encoded = np.array([label_to_int[label] for label in labels])
    num_classes = len(unique_classes) # 3 unique iris names
    # Create one-hot matrix for encoding
    labels_onehot = np.zeros((labels_encoded.size, num_classes)) 
    labels_onehot[np.arange(labels_encoded.size), labels_encoded] = 1
    return labels_encoded, labels_onehot, label_to_int

# Data Splitting - 20% of data is for testing, rest for training
def train_test_split(features, labels, test_size=0.2, random_state=42):
    np.random.seed(random_state) # Get seed with random_state for consistency
    indices = np.arange(len(features)) # create indices for data set (ex. [0, 1,..])
    np.random.shuffle(indices)
    split_idx = int(len(features) * (1 - test_size)) # split data based on test_size
    # split data and return new data
    train_indices, test_indices = indices[:split_idx], indices[split_idx:]
    return features[train_indices], features[test_indices], labels[train_indices], labels[test_indices]

# ANN Implementation
class ANN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases for hidden and output layers
        self.hidden_weights = np.random.randn(input_size, hidden_size) * 0.1
        self.hidden_biases = np.zeros((1, hidden_size))
        self.output_weights = np.random.randn(hidden_size, output_size) * 0.1
        self.output_biases = np.zeros((1, output_size))

    # ReLU (Rectified Linear Unit) activation function
    def relu(self, pre_activations):
        return np.maximum(0, pre_activations)

    # Softmax activation function
    def softmax(self, pre_activations):
        exp_values = np.exp(pre_activations - np.max(pre_activations, axis=1, keepdims=True))
        return exp_values / np.sum(exp_values, axis=1, keepdims=True)

    # Forward Propagation
    def forward(self, inputs):
        # Compute hidden layer pre-activations and activations
        self.hidden_pre_activations = np.dot(inputs, self.hidden_weights) + self.hidden_biases
        self.hidden_activations = self.relu(self.hidden_pre_activations)

        # Compute output layer pre-activations and activations (softmax probabilities)
        self.output_pre_activations = np.dot(self.hidden_activations, self.output_weights) + self.output_biases
        self.output_activations = self.softmax(self.output_pre_activations)

        return self.output_activations

    # Compute Raw Error
    def compute_raw_error(self, true_labels, predicted_labels):
        # Compute the raw error: difference between predicted and true labels
        raw_error = predicted_labels - true_labels
        # Return the mean absolute error for monitoring
        mean_absolute_error = np.mean(np.abs(raw_error))
        return mean_absolute_error

    # Backward Propagation
    def backward(self, inputs, true_labels, predicted_labels, learning_rate):
        num_samples = inputs.shape[0] 

        # Compute output layer error and gradients
        output_layer_error = predicted_labels - true_labels
        gradient_output_weights = np.dot(self.hidden_activations.T, output_layer_error) / num_samples
        gradient_output_biases = np.sum(output_layer_error, axis=0, keepdims=True) / num_samples

        # Propagate error back to hidden layer
        hidden_layer_error_signal = np.dot(output_layer_error, self.output_weights.T)
        hidden_layer_error = hidden_layer_error_signal * (self.hidden_pre_activations > 0)  # ReLU derivative

        # Compute gradients for hidden layer weights and biases
        gradient_hidden_weights = np.dot(inputs.T, hidden_layer_error) / num_samples
        gradient_hidden_biases = np.sum(hidden_layer_error, axis=0, keepdims=True) / num_samples

        # Update weights and biases using gradient descent
        self.output_weights -= learning_rate * gradient_output_weights
        self.output_biases -= learning_rate * gradient_output_biases
        self.hidden_weights -= learning_rate * gradient_hidden_weights
        self.hidden_biases -= learning_rate * gradient_hidden_biases

    # Training Method
    def train(self, training_inputs, training_labels, epochs=1000, learning_rate=0.01):
        for epoch in range(epochs):
            # Forward propagation
            predicted_labels = self.forward(training_inputs)

            # Compute raw error
            mean_absolute_error = self.compute_raw_error(training_labels, predicted_labels)

            # Backward propagation (adjust weights and biases)
            self.backward(training_inputs, training_labels, predicted_labels, learning_rate)

            # Print training progress every 100 epochs
            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Mean Absolute Error: {mean_absolute_error:.4f}")

    # Prediction Method
    def predict(self, inputs):
        # Perform forward propagation and return class predictions
        predicted_probabilities = self.forward(inputs)
        return np.argmax(predicted_probabilities, axis=1)

# Classification
def classify_user_input(nn, feature_mean, feature_std, label_to_int):
    print("Enter the following attributes:")
    sepal_length = float(input("Sepal length (cm): "))
    sepal_width = float(input("Sepal width (cm): "))
    petal_length = float(input("Petal length (cm): "))
    petal_width = float(input("Petal width (cm): "))

    # Scale user input
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    features_scaled = (features - feature_mean) / feature_std

    # Predict class
    prediction = nn.predict(features_scaled)
    int_to_label = {idx: label for label, idx in label_to_int.items()}
    print(f"Predicted Iris species: {int_to_label[prediction[0]]}")

# Main Function
def main():
    # File Path
    file_path = "iris_data.txt"  # Replace with your dataset file

    # Data Preparation
    data = load_and_clean_data(file_path)
    scaled_features, y, feature_means, feature_stds = select_and_preprocess(data)
    labels_encoded, labels_onehot, label_to_int = transform_and_encode_labels(y)

    # Split Data
    train_features, test_features, train_labels, test_labels = train_test_split(scaled_features, labels_onehot, test_size=0.2)

    # Train the ANN
    nn = ANN(input_size=4, hidden_size=8, output_size=3)
    print("Training the neural network...")
    nn.train(train_features, train_labels, epochs=1000, learning_rate=0.01)

    # Evaluate the Model
    test_labels_pred = nn.predict(test_features)
    test_labels_actual = np.argmax(test_labels, axis=1)
    accuracy = np.mean(test_labels_pred == test_labels_actual)
    print(f"Test Accuracy: {accuracy * 100:.2f}%")

    # User Input
    while True:
        print("\nOptions:")
        print("1. Classify a new Iris plant")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            classify_user_input(nn, feature_means, feature_stds, label_to_int)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
