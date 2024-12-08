import csv

def is_valid_email(email):
    """Validate email format."""
    return '@' in email and '.' in email

try:
    # load and process the CVS file
    with open('data.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
        print('Original Data:')
        for row in rows:
            print(row)
    
    # Cleaning and validation
    cleaned_rows = []
    for row in rows:
        is_valid_row = True
        
        # Check for missing values
        if not (row['name'] and row['email'] and row['age']):
            is_valid_row = False
        
        # Email validation
        email = row['email'].replace('[at]', '@').strip()
        if not is_valid_email(email):
            is_valid_row = False
        
        # Age validation
        try:
            age = int(row['age'].strip())
            if age < 18 or age > 60:
                is_valid_row = False
        except ValueError:
            is_valid_row = False
        
        # Add valid rows to cleaned list
        if is_valid_row:
            cleaned_row = {
                'name': row['name'].strip(),
                'email': email,
                'age': str(age)
            }
            cleaned_rows.append(cleaned_row)
    
    # Save cleaned data to a new file
    with open('cleaned_data.csv', 'w', newline='') as outfile:
        fieldnames = ['name', 'email', 'age']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_rows)
    
    print("\nCleaned Data:")
    for row in cleaned_rows:
        print(row)

except FileNotFoundError:
    print("Input file 'data.csv' not found.")