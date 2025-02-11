import yaml
import csv

# Load YAML file
def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Convert YAML to CSV
def yaml_to_csv(yaml_data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=yaml_data.keys())
        writer.writeheader()
        writer.writerow(yaml_data)

# File paths
yaml_file = '/Users/tarun/Documents/Projects/GitHub/Formula-1/data/seasons/2024/races/01-bahrain/race.yml'  # Change this to your YAML file path
csv_file = '/Users/tarun/Documents/Projects/GitHub/Formula-1/data/csv-files/race.csv'  # Output CSV file

data = load_yaml(yaml_file)
yaml_to_csv(data, csv_file)

print(f"CSV file '{csv_file}' has been created successfully.")
