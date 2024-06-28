if __name__ == "__main__":
    scores = list(map(int, input().strip().split()))  # Read the scores and convert to list of integers
    
    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Find the runner-up score
    runner_up_score = sorted_scores[1]  # Index 1 because sorted in descending order
    
    # Print the runner-up score
    print(runner_up_score)
