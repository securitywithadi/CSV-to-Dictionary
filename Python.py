import csv

def csv_to_dict(file_path):
    """
    Reads a CSV file with two columns: 'keys' and 'values', 
    and converts it into a dictionary.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        dict: A dictionary with keys from the first column and values from the second column.
    """
    result_dict = {}
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 2:
                    print(f"Skipping invalid row: {row}")
                    continue
                key, value = row[0], row[1]
                result_dict[key] = value
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return result_dict

# Example usage
file_path = 'data.csv'  # Replace with your CSV file path
data_dict = csv_to_dict(file_path)
print(data_dict)
