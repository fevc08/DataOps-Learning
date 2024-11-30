# 21 Days to Learn DataOps with ChatGPT

## Day 1: Introduction to DataOps and Version Control

### Theory
DataOps (Data Operations) combines agile, DevOps, and lean manufacturing practices to improve the speed, quality, and reliability of data workflows. Key principles include:

- Automation: Minimize manual steps in data workflows.
- Collaboration: Foster teamwork between data engineers, analysts, and operations.
- Continuous Integration/Continuous Deployment (CI/CD): Apply software engineering best practices to data workflows.

Version control with Git is essential in DataOps to track changes, collaborate effectively, and maintain workflow transparency. Tools like GitHub or GitLab provide a platform to manage repositories and CI/CD pipelines.

### Exercise
Set up a GitHub Repository

Create a free GitHub account if you don’t have one.
Create a new repository (name it DataOps-Learning).
Commit a Python Script

Open Visual Studio Code.
Create a Python file (e.g., hello_dataops.py) with the following code:

```python
print("Hello, DataOps!")
```

Initialize Git in your local folder:

```bash
git init
git add .
git commit -m "Initial commit: Hello DataOps script"
```

Push your changes to the GitHub repository:

```bash
git branch -M main
git remote add origin <your-repo-URL>
git push -u origin main
```
## Day 2: Python Basics for DataOps
### Theory
Python is a cornerstone for DataOps due to its simplicity and rich ecosystem. Today, we’ll focus on:

1. File Handling: Reading and writing files are common tasks in data workflows.
2. Exception Handling: Ensures scripts can handle errors gracefully.

#### Key Concepts:

**Reading Files:**

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

**Exception Handling:**

```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

### Exercise

1. **Create a .txt File:**
- Create a file named sample_data.txt in the same directory as your Python script. Add the following content:

    ```txt
    Name, Age, City
    John, 30, New York
    Jane, 25, Los Angeles
    Mike, 35, Chicago
    ```

2. Write a Python Script:

- Create a new Python file (e.g., read_file.py).

    Your script should:
    1. Read the contents of sample_data.txt and print them line by line.
    2. Handle the case where the file is missing and print a user-friendly error message.

**Bonus Task:**
If you have time, count the number of lines in the file and print the total.

## Day 3: Working with Config Files
### Theory
In DataOps, configuration files help manage dynamic parameters like database credentials, API keys, or file paths without hardcoding them into scripts. Popular formats include:

1. YAML (Yet Another Markup Language): Readable, widely used in DevOps.
2. JSON (JavaScript Object Notation): Lightweight, ideal for structured data.

**YAML Example (config.yaml):**

```yaml
database:
  host: localhost
  port: 5432
  username: admin
  password: secret
```
**JSON Example (config.json):**

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "username": "admin",
    "password": "secret"
  }
}
```
**Python Libraries for Parsing Config Files:**

- yaml: For YAML files. Install using pip install pyyaml.
- json: Built-in library for JSON.
### Exercise
1. Create a YAML File:

    Name it config.yaml. Include the following:
    ```yaml
    database:
    host: localhost
    port: 5432
    username: admin
    password: secret```
2. Write a Python Script:

    Name the file read_config.py.

    Your script should:
    1. Load and parse the config.yaml file.
    2. Print each parameter in the database section (e.g., host, port).

**Example Output:**

```yaml
Database Host: localhost  
Database Port: 5432  
Database Username: admin  
Database Password: secret
```  
**Bonus Task:**

Modify the script to check if the configuration file exists before reading. Print an error message if it’s missing.

*Hints*

To load YAML in Python:
```python
import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    print(config['database']['host'])  # Access individual keys
```
## Day 4: Environment Setup and Virtual Environments
### Theory
A virtual environment is an isolated environment for Python projects, allowing you to:

1. Avoid version conflicts between dependencies of different projects.
2. Maintain a clean global Python installation.

**Key Tools:**

`venv` (built-in): Simple and effective for creating virtual environments.

`pip:` Python’s package installer for managing dependencies.

**Basic Commands:**

1. Create a virtual environment:
```bash
python -m venv venv_name
```
2. Activate the virtual environment:

    1. Windows:
    ```bash
    venv_name\Scripts\activate
    ```
    2. Mac/Linux:
    ```bash
    source venv_name/bin/activate
    ```
3. Install packages:
```bash
pip install package_name
```
4. Deactivate the environment:
```bash
deactivate
```
### Exercise
1. Set Up a Virtual Environment:

Create a virtual environment named dataops_env in your project folder.

2. Activate the Environment:

Use the appropriate command for your operating system.

3. Install Dependencies:

- Install `PyYAML` and `requests` libraries in the virtual environment using pip.
- Freeze the installed dependencies into a requirements.txt file:
```bash
pip freeze > requirements.txt
```
4. Write a Script:

- Create a Python script (test_env.py) to verify the environment setup.
    
    - The script should import yaml and requests and print a success message:
```python
import yaml
import requests

print("Virtual environment and dependencies are set up successfully!")
```
## Day 5: Scripting with File I/O and Automation
### Theory
File I/O (Input/Output) and automation are essential for DataOps. Automating repetitive tasks like file reading, data parsing, or log generation increases efficiency and reduces human error.

**Key Concepts:**

1. File Handling in Python:

- Reading: Read data from files (open, read, readlines).
- Writing: Write or append data to files (write, writelines).
Automating Tasks:

2. Combine logic to perform recurring tasks (e.g., log backups).
3. Use scheduling tools like `cron` (Linux) or `Task Scheduler` (Windows) for time-based automation.

Working with Directories:

Use the os and shutil libraries for directory management.
```python
import os
os.mkdir('new_folder')  # Create a directory
os.listdir()            # List directory contents
```
### Exercise
1. Scenario:
You’re tasked with automating log processing for a system. Your goal is to:

    - Create a script to generate a sample log file.
    - Read and process the log file.
    - Save processed results into a new file.

2. Step-by-Step Tasks:

    Generate Logs:
    Write a script to create a sample log file (system.log) with 10 lines of dummy data.
    Example log line:

    ```arduino
    2024-11-22 14:30:45 INFO: Task completed successfully
    ```
    Process Logs:
    - Read the log file and filter lines containing a specific keyword, e.g., `ERROR`. Save the filtered results to `error_logs.txt`.

    Script Structure:
    - Create a Python script (log_processor.py) that includes:

        -Log generation.
        -Reading and filtering.
        -Writing filtered logs.

**Bonus Task:**

- Add a timestamp to the error_logs.txt filename, e.g., error_logs_20241122.txt. Use the datetime library for this.

**Hints**

To write logs to a file:

```python
with open('system.log', 'w') as file:
    for i in range(10):
        file.write(f"2024-11-22 14:30:45 INFO: Line {i+1}\n")
```
To filter logs:

```python
with open('system.log', 'r') as file:
    lines = file.readlines()
filtered = [line for line in lines if 'ERROR' in line]
```
To add a timestamp:

```python
from datetime import datetime
timestamp = datetime.now().strftime('%Y%m%d')
filename = f"error_logs_{timestamp}.txt"
```
Day 6: Basic Data Processing and Validation
Topic Explanation: Basic Data Processing and Validation
Data processing is a key part of DataOps. It involves cleaning, transforming, and validating raw data to make it usable. Validation ensures data integrity by checking that data adheres to defined rules or schema.

Today, we will:

- Process structured data (CSV format).
- Clean and validate data:
    - Remove empty rows.
    - Validate specific fields (e.g., email format, numeric ranges).
- Save cleaned data back to a file.

**Step-by-Step Guide**

Understand the Input File

We'll use a sample CSV file with the following structure:

```graphql
name,email,age
Alice,alice@example.com,30
Bob,bob[at]example.com,25
Charlie,,22
,jane@example.com,28
```
Tasks:

Load the CSV file.
Remove rows with missing data.
Ensure email format is valid (contains @).
Ensure age is within a specific range (e.g., 18–60).
Output:
A cleaned CSV file:

```graphql
name,email,age
Alice,alice@example.com,30
Bob,bob@example.com,25
```
Exercise
1. Create a sample CSV file named data.csv with the above data.
2. Write a Python script to:
    - Load the file and display its content.
    - Clean the data based on the rules.
    - Save the cleaned data into a new file named cleaned_data.csv.

**Starter Code**

Here’s a hint to get you started:

```python
import csv

# Load and process the CSV file
try:
    with open('data.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        print("Original Data:")
        for row in rows:
            print(row)
    
    # Cleaning and validation logic here
    
    with open('cleaned_data.csv', 'w', newline='') as outfile:
        fieldnames = ['name', 'email', 'age']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        # Write cleaned rows here

except FileNotFoundError:
    print("Input file 'data.csv' not found.")
```
**Deliverables**
- data.csv: The input file.
- Python script: Implements data processing and validation.
- cleaned_data.csv: The cleaned output file.
Once you're done, share your updated repository link, and I'll review your work!

## Day 7: Data Validation
### **Topic Explanation:**
#### *Pydantic for Schema Validation*
Pydantic is a Python library used for data validation and parsing. It enforces type checks and ensures that data matches a defined schema. This is particularly useful when working with data pipelines to prevent invalid data from propagating through the system.

**Key Features:**

- *Schema Definition:* Define a data model with constraints (e.g., types, value ranges).
- *Validation:* Automatically checks if the data conforms to the model.
- *Error Handling:* Provides detailed error messages for invalid data.

**Example Use Case:**

Imagine validating rows of a CSV file to ensure:

- The name is a string.
- The email is properly formatted.
- The age is an integer within a specific range.

### Exercise: Data Validation with Pydantic

**Step-by-Step Instructions**
1. Install Pydantic:

```bash
pip install pydantic
```
2. Define a schema for the data:

- `name`: Non-empty string.
- `email`: Valid email format.
- `age`: Integer between 18 and 60.

**Write a Python script to:**

- Read a CSV file (`data.csv`).
- Validate each row against the schema using Pydantic.
- Save valid rows to `validated_data.csv`.

**Starter Code**
```python
from pydantic import BaseModel, EmailStr, ValidationError
import csv

# Define the Pydantic model
class UserData(BaseModel):
    name: str
    email: EmailStr
    age: int

    @classmethod
    def validate_row(cls, row):
        """Custom method to validate a row."""
        try:
            validated_data = cls(
                name=row['name'].strip(),
                email=row['email'].strip(),
                age=int(row['age'].strip())
            )
            return validated_data
        except (ValidationError, ValueError) as e:
            print(f"Validation error for row {row}: {e}")
            return None

# File paths
input_file = 'data.csv'
output_file = 'validated_data.csv'

# Read and validate data
valid_rows = []
try:
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            validated_row = UserData.validate_row(row)
            if validated_row:
                valid_rows.append(validated_row.dict())
except FileNotFoundError:
    print(f"Input file '{input_file}' not found.")

# Write validated data to a new file
if valid_rows:
    with open(output_file, 'w', newline='') as outfile:
        fieldnames = ['name', 'email', 'age']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid_rows)
    print(f"Validated data saved to {output_file}")
else:
    print("No valid data to save.")
```
**Deliverables**
- Input file: data.csv with test data to validate.
- Python script: Implements schema validation with Pydantic.
- Output file: validated_data.csv containing valid rows.