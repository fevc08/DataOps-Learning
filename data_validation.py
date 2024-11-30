from pydantic import BaseModel, EmailStr, ValidationError, field_validator
import csv

# Define the function to clean email addresses
def clean_email(email):
    """Replace '[at]' with '@' in email addresses."""
    return email.replace('[at]', '@')

# Define the Pydantic model
class UserData(BaseModel):
    name: str
    email: EmailStr
    age: int

    # Custom validators
    @field_validator('name')
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError('name must not be empty')
        return value

    @field_validator('age')
    def age_must_be_between_18_and_60(cls, value):
        if not 18 <= value <= 60:
            raise ValueError('age must be between 18 and 60')
        return value
    

    @classmethod
    def validate_row(cls, row):
        """Custom method to validate a row."""
        try:
            if not row['email'].strip():
                raise ValueError("Email address cannot be empty.")
            cleaned_email = clean_email(row['email'].strip())
            validated_data = cls(
                name=row['name'].strip(),
                email=cleaned_email,
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
                valid_rows.append(validated_row.model_dump())
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
