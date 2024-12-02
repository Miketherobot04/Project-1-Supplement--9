from scipy.integrate import quad

def integrate_linear_function(coefficients, start, end):
    """
    Integrates a linear function of the form ax + b over a specified range.
    
    Args:
        coefficients (tuple): Coefficients (a, b) for the linear function ax + b.
        start (float): Start of the integration range.
        end (float): End of the integration range.
    
    Returns:
        float: The definite integral value.
    """
    a, b = coefficients

    # Define the linear function
    def linear_func(x):
        return a * x + b

    # Perform the integration
    result, _ = quad(linear_func, start, end)
    return result