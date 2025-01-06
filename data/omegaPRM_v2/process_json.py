import json
import os
import math

def split_questions_uniformly(input_filepath: str, output_directory: str, num_files: int):
    """
    Split a JSON file containing questions into a specified number of files with approximately equal questions.

    Parameters:
    - input_filepath (str): Path to the JSON file containing the list of questions.
    - output_directory (str): Directory to save the split JSON files.
    - num_files (int): Number of files to split the questions into.

    Each output file will contain approximately len(questions) / num_files questions.
    """
    # Load questions from the input file
    with open(input_filepath, 'r') as f:
        questions = json.load(f)

    # Calculate the number of questions per file
    total_questions = len(questions)
    questions_per_file = math.ceil(total_questions / num_files)

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Split the questions and write to output files
    for i in range(num_files):
        start_idx = i * questions_per_file
        end_idx = min(start_idx + questions_per_file, total_questions)
        questions_subset = questions[start_idx:end_idx]

        output_filepath = os.path.join(output_directory, f"questions_part_{i + 1}.json")
        with open(output_filepath, 'w') as f_out:
            json.dump(questions_subset, f_out, indent=4)

        print(f"Saved {len(questions_subset)} questions to {output_filepath}")


# Example usage
if __name__ == "__main__":
    split_questions_uniformly("extracted_problems_and_answers.json", "output_directory", 8)