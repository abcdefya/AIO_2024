def md_nre_single_sample(y, y_hat, n, p):
    # Step 1: Take the nth root of y and y_hat
    y_n_root = y ** (1/n)
    y_hat_n_root = y_hat ** (1/n)
    
    # Step 2: Calculate the difference
    diff = abs(y_n_root - y_hat_n_root)
    
    # Step 3: Raise the difference to the power of p
    diff_p = diff ** p
    
    # Return the final result
    return diff_p

# Test cases
print(md_nre_single_sample(100, 99.5, 2, 1))
print(md_nre_single_sample(50, 49.5, 2, 1))
print(md_nre_single_sample(20, 19.5, 2, 1))
print(md_nre_single_sample(0.6, 0.1, 2, 1))
