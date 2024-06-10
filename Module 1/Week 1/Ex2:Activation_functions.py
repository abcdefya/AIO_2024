import numpy as np

def is_number(value):
    """
    Check if the input value is a number.

    Args:
    value: Any value to be checked.

    Returns:
    bool: True if the value is a number, False otherwise.
    """
    try:
        float(value)  # Attempt to convert to float
        return True
    except ValueError:
        return False

def is_valid_activation_function(func_name):
    """
    Check if the activation function name is valid.

    Args:
    func_name (str): The name of the activation function to be checked.

    Returns:
    bool: True if the activation function name is valid, False otherwise.
    """
    valid_activation_functions = ['sigmoid', 'relu', 'elu']

    if func_name.lower() in valid_activation_functions:
        return True
    else:
        print(f"{func_name} is not supported")
        return False

def sigmoid(x):
    """
    Compute the sigmoid function for the input x.

    Args:
    x: A scalar or numpy array.

    Returns:
    sigmoid(x): The sigmoid of x.
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    Compute the ReLU function for the input x.

    Args:
    x: A scalar or numpy array.

    Returns:
    relu(x): The ReLU of x.
    """
    return np.maximum(0, x)

def elu(x, alpha=1.0):
    """
    Compute the ELU function for the input x.

    Args:
    x: A scalar or numpy array.
    alpha (float): The alpha value for ELU function, defaults to 1.0.

    Returns:
    elu(x): The ELU of x.
    """
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def calc_activation_func(x, act_name):
    """
    Calculate the result of the activation function based on the input x and function name.

    Args:
    x: The input value for the activation function.
    act_name (str): The name of the activation function.

    Returns:
    result: The result of the activation function.
    """
    if not is_valid_activation_function(act_name):
        return None

    if not is_number(x):
        print(f"x must be a number")
        return None

    x = float(x)
    
    if act_name.lower() == 'sigmoid':
        result = sigmoid(x)
    elif act_name.lower() == 'relu':
        result = relu(x)
    elif act_name.lower() == 'elu':
        result = elu(x)
    
    return result


def user_input(func_name, x_value):
    """
    Function to get user input for activation function and value, then compute the result.

    Args:
    func_name (str): The name of the activation function.
    x_value (str): The input value for the function.

    Returns:
    None
    """
    if not is_valid_activation_function(func_name):
        return

    if not is_number(x_value):
        print(f"x must be a number")
        return

    x = float(x_value)
    
    if func_name.lower() == 'sigmoid':
        result = sigmoid(x)
    elif func_name.lower() == 'relu':
        result = relu(x)
    elif func_name.lower() == 'elu':
        result = elu(x)

    print(f"{func_name}: f({x}) = {result}")

# Test cases
test_cases = [
    ('sigmoid', '1.5'),  # Valid case
    ('sigmoid', 'abc'),  # x is not a number
    ('belu', '1.5'),      # Invalid activation function
    ('relu', '-2')
]

# Run test cases
for func_name, x_value in test_cases:
    print(f"\nInput activation Function (sigmoid | relu | elu): {func_name}")
    print(f"Input x: {x_value}")
    user_input(func_name, x_value)


# assert round ( sigmoid (3) , 2) ==0.95
# print ( round ( sigmoid (2) , 2) )

# assert round ( elu (1) ) ==1
# print ( round ( elu ( -1) , 2) )
# assert is_number (3) == 1.0
# assert is_number (’ -2a’) == 0.0
# print ( is_number (1) )
# print ( is_number (’n’) )
# assert calc_activation_func(1, 'relu') == 1
# print(round(calc_activation_func(3, 'sigmoid'), 2))