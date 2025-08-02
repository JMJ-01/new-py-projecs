import csv

# Replace 'your_file.txt' with the actual path to your file
file_path = r"C:\Users\HP\OneDrive\Desktop\JMJ\RESEARCH\ML learning\Swayam course\AI ML\week 4\Week - 4_Datasets_for_Data_Preparation\acDetails.txt"

with open(file_path, 'r') as file:
    # Read a sample of the file (e.g., the first 1024 bytes)
    sample = file.read(1024)
    
    # Use the Sniffer to detect the dialect (which includes the delimiter)
    sniffer = csv.Sniffer()
    try:
        dialect = sniffer.sniff(sample)
        print(f"The detected delimiter is: '{dialect.delimiter}'")
    except csv.Error:
        print("Could not determine the delimiter.")