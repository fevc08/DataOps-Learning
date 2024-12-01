import pandas as pd

input_file = 'raw_data.csv'
output_file = 'processed_data.csv'

def etl_process(input_file, output_file):
    
    try:
        # Extract: Read the data from raw_data.csv
        df = pd.read_csv(input_file)
        
        # Transform
        ## Replace [at] with @ in the email column.
        df['email'] = df['email'].str.replace('[at]', '@', regex=False)
        
        ## Standardize column names to lowercase
        df.columns = df.columns.str.lower()
        
        ## Remove rows with missing values.
        df = df.dropna()
        
        ## Combine first_name and last_name into a full_name column.
        df['full_name'] = df['first_name'] + ' ' + df['last_name']
        df = df.drop(columns = ['first_name', 'last_name']) # Drop the columns 'first_name'
        df = df[['full_name', 'email', 'date_of_birth']] # Reorder the columns
        
        # Validating proper format for columns with datetime
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
        df = df.dropna(subset=['date_of_birth'])  # Remove rows with invalid dates
        
        # Load: Save the transformed data into processed_data.csv
        df.to_csv(output_file, index = False)
        print(f"ETL process completed. Processed data saved to {output_file}")
        
        # Return some basic information about the transformation
        return {
            'original_rows': len(pd.read_csv(input_file)),
            'processed_rows': len(df),
            'columns': list(df.columns)
        }
    
    except FileNotFoundError:
        print(f"Error: Input file {input_file} not found.")
    except Exception as e:
        print(f"An error occurred during ETL process: {e}")

# Run the ETL process
if __name__ == '__main__':
    result = etl_process(input_file, output_file)
    if result:
        print("\nETL Process Summary:")
        print(f"Original number of rows: {result['original_rows']}")
        print(f"Processed number of rows: {result['processed_rows']}")
        print(f"Columns in processed data: {result['columns']}")