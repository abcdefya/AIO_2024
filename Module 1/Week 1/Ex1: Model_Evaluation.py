def evaluate_classification_model(tp, fp, fn):
    """
    Function to calculate precision, recall, and F1-score for a classification model.

    Args:
    tp (int): Number of true positives.
    fp (int): Number of false positives.
    fn (int): Number of false negatives.

    Returns:
    None
    """
    # Check if type is int for tp, fp, and fn
    for arg_name, arg_value in zip(["tp", "fp", "fn"], [tp, fp, fn]):
        if not isinstance(arg_value, int):
            print(f"{arg_name} must be an integer")
            return
    
    # Check if greater than zero for tp, fp, and fn
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp, and fn must be greater than zero")
        return
    
    # Calculate metrics
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    
    # Print metrics
    print("Precision is", precision)
    print("Recall is", recall)
    print("F1-score is", f1_score)


# Test cases
test_cases = [
    (3, 4, 1),    # Valid case
    ('a', 4, 1),  # tp is not an integer
    (3, 'b', 1),  # fp is not an integer
    (3, 4, 'c'),  # fn is not an integer
    (0, 4, 1),    # tp is not greater than zero
    (3, 0, 1),    # fp is not greater than zero
    (3, 4, 0),    # fn is not greater than zero
]

# Iterate through test cases
for i, test_case in enumerate(test_cases, start=1):
    print(f"\nTest Case {i}: evaluate_classification_model(tp={test_case[0]}, fp={test_case[1]}, fn={test_case[2]})")
    evaluate_classification_model(*test_case)