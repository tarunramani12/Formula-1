# import yaml
# import csv

# # Load YAML file
# def load_yaml(file_path):
#     with open(file_path, 'r') as file:
#         data = yaml.safe_load(file)
#     return data

# # Convert YAML to CSV
# def yaml_to_csv(yaml_data, csv_file_path):
#     with open(csv_file_path, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=yaml_data.keys())
#         writer.writeheader()
#         writer.writerow(yaml_data)

# # File paths
# yaml_file = '/Users/tarun/Documents/Projects/GitHub/Formula-1/data/seasons/2024/races/01-bahrain/race.yml'  # Change this to your YAML file path
# csv_file = '/Users/tarun/Documents/Projects/GitHub/Formula-1/data/csv-files/race.csv'  # Output CSV file

# data = load_yaml(yaml_file)
# yaml_to_csv(data, csv_file)

# print(f"CSV file '{csv_file}' has been created successfully.")




import yaml
import csv
import os

# Load YAML file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Convert YAML to CSV
def yaml_to_csv(yaml_data, csv_file_path):
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)  # Create folder if not exists
    
    with open(csv_file_path, 'w', newline='') as file:
        if isinstance(yaml_data, list):  # If YAML is a list, write multiple rows
            keys = set().union(*(d.keys() for d in yaml_data if isinstance(d, dict)))
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(yaml_data)
        elif isinstance(yaml_data, dict):  # If YAML is a dictionary, write a single row
            writer = csv.DictWriter(file, fieldnames=yaml_data.keys())
            writer.writeheader()
            writer.writerow(yaml_data)
        else:
            print(f"Unsupported data format in {csv_file_path}")

# Process all YAML files in a directory recursively
def process_yaml_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".yml"):
                yaml_path = os.path.join(root, file)
                csv_path = os.path.splitext(yaml_path)[0] + ".csv"
                
                try:
                    data = load_yaml(yaml_path)
                    yaml_to_csv(data, csv_path)
                    print(f"Converted: {yaml_path} -> {csv_path}")
                except Exception as e:
                    print(f"Error processing {yaml_path}: {e}")

# Specify the directory to scan
directory_to_scan = '/Users/tarun/Documents/Projects/GitHub/Formula-1/our-data'  # Change this to your target directory
process_yaml_files(directory_to_scan)

print("Processing complete.")