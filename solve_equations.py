from scipy.optimize import fsolve

def solve_system_of_equations(equations, initial_guess):
    """
    Solves a system of equations with two unknowns.
    
    Args:
        equations (list): List of two lambda functions representing equations.
        initial_guess (tuple): Initial guesses for the variables (x, y).
    
    Returns:
        dict: Dictionary with fields 'X' and 'Y' for the solutions.
    """
    solution = fsolve(lambda vars: [eq(vars) for eq in equations], initial_guess)
    return {"X": solution[0], "Y": solution[1]}