import numpy as np

def generate_normal_samples(mean, std_dev, num_samples):
    """
    Generates a specified number of samples from a normal distribution.
    
    Args:
        mean (float): Mean of the distribution.
        std_dev (float): Standard deviation of the distribution.
        num_samples (int): Number of samples to generate.
    
    Returns:
        list: List of samples from the normal distribution.
    """
    return list(np.random.normal(mean, std_dev, num_samples))