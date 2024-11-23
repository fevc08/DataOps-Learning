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

