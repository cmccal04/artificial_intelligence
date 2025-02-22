import numpy as np

# Replaces NaN values with the median.
def replace_nan(data):
    row_medians = np.nanmedian(data, axis=1, keepdims=True)
    data = np.where(np.isnan(data), row_medians, data)
    return data

# Calculates the standard deviation of speed over 6 second intervals, which 
# is the second classification feature.
def calculate_speed_consistency(training_data):
    # load data from training.txt
    birds = training_data[:10]
    planes = training_data[10:]

    # Calculate standard deviation for each track
    std_dev_birds = np.std(birds.reshape(birds.shape[0], -1, 6), axis=-1)
    std_dev_planes = np.std(planes.reshape(planes.shape[0], -1, 6), axis=-1)

    # Create histograms for speed consistency likelihoods
    bins = np.arange(0, 101, 1)  # Adjust bin size as needed
    hist_birds, _ = np.histogram(std_dev_birds.flatten(), bins=bins)
    hist_planes, _ = np.histogram(std_dev_planes.flatten(), bins=bins)

    # Normalize to probabilities, adding a small constant to avoid zeros
    consistency_birds = hist_birds / hist_birds.sum() + 0.001
    consistency_airplanes = hist_planes / hist_planes.sum() + 0.001

    return consistency_birds, consistency_airplanes

# Classifies a test track using Naïve Bayesian inference.
def classify(test_track, likelihood_data, consistency_birds, consistency_airplanes):
    speed_birds = likelihood_data[0]
    speed_airplanes = likelihood_data[1]

    # Calculate speed consistency for buckets of 6 seconds
    speed_consistency_test = np.std(test_track.reshape(1, -1, 6), axis=-1).flatten()

    prior_birds, prior_airplanes = 0.5, 0.5
    classifications = []

    for i, speed in enumerate(test_track):
        speed_index = min(int(round(speed * 2)), len(speed_birds) - 1)
        consistency_index = min(int(speed_consistency_test[i // 6]), len(consistency_birds) - 1)

        # Compute posterior probabilities
        likelihood_bird = speed_birds[speed_index] * consistency_birds[consistency_index]
        likelihood_airplane = speed_airplanes[speed_index] * consistency_airplanes[consistency_index]
        
        posterior_bird = prior_birds * likelihood_bird / (likelihood_bird + likelihood_airplane)
        posterior_airplane = prior_airplanes * likelihood_airplane / (likelihood_bird + likelihood_airplane)
        
        # Assign class and update priors
        if posterior_bird > posterior_airplane:
            classifications.append('b')
            prior_birds, prior_airplanes = 0.9, 0.1
        else:
            classifications.append('a')
            prior_birds, prior_airplanes = 0.1, 0.9

    final_classification = 'b' if classifications.count('b') > classifications.count('a') else 'a'
    return final_classification

# Main function to load data and classify.
def main():
    # Load files
    likelihood_data = np.loadtxt('likelihood.txt')
    training_data = np.loadtxt('dataset.txt')
    testing_data = np.loadtxt('testing.txt')

    # Replace nan values
    training_data = replace_nan(training_data)
    testing_data = replace_nan(testing_data)

    # Compute speed consistency
    consistency_birds, consistency_airplanes = calculate_speed_consistency(training_data)

    # Classify test tracks and print final classifications
    print("\nClassifications:")
    for i, test_track in enumerate(testing_data):
        final_classification = classify(
            test_track, likelihood_data, consistency_birds, consistency_airplanes
        )
        if final_classification == 'a':
            print(f"Track {i + 1}: airplane")
        elif final_classification == 'b':
            print(f"Track {i + 1}: bird")

if __name__ == "__main__":
    main()


