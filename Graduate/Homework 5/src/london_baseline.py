# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    # Create a list of "London" predictions for every example in the dev set
    with open("birth_dev.tsv", encoding='utf-8') as f:
        num_examples = len(f.readlines())
    
    # Generate a list of "London" predictions
    predictions = ["London"] * num_examples
    
    # Calculate the accuracy using the utils.evaluate_places function
    total, correct = utils.evaluate_places("birth_dev.tsv", predictions)
    
    # Convert to percentage
    accuracy = 100.0 * correct / total if total > 0 else 0.0
    ### END YOUR CODE ###

    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
