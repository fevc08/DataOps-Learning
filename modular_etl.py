import pandas as pd
import logging
import yaml

# Load configuration
def load_config(config_path="config.yaml"):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

# Logging setup
def configure_logging(log_file):
    logging.basicConfig(
        filename = log_file,
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )

# Modular ETL functions
def extract_data(input_data):
    try:
        data = pd.read_csv(input_data)
        logging.info("Data extraction successful.")
        return data
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

def transform_data(data, config):
    try:
        # Drop duplicates
        original_rows = len(data)
        data = data.drop_duplicates(subset='employee_id')
        duplicates_removed = original_rows - len(data)
        logging.info(f"Dropped {duplicates_removed} duplicate rows")
        
        if config['transformations']['text_to_uppercase']:
            categorical_columns = data.select_dtypes(include=['object']).columns
            for column in categorical_columns:
                data.loc[:, column] = data[column].str.upper()
                logging.info(f"Converted column {column} to uppercase.")
        
        if config['transformations']['fill_missing_dates']:
            # Identify date columns
            date_columns = []
            for column in data.columns:
                if data[column].dtype == 'object':
                    sample_values = data[column].dropna().head()
                    date_patterns = [
                        r'\d{4}[-/]\d{2}[-/]\d{2}',  # YYYY-MM-DD or YYYY/MM/DD
                        r'\d{2}[-/]\d{2}[-/]\d{4}',  # MM-DD-YYYY or MM/DD/YYYY
                        r'\d{2}[-/]\d{2}[-/]\d{2}'   # YY-MM-DD or YY/MM/DD
                    ]
                    for pattern in date_patterns:
                        if sample_values.str.match(pattern).any():
                            date_columns.append(column)
                            break
            
            logging.info(f"Identified date columns: {date_columns}")
            
            for column in date_columns:
                data.loc[:, column] = pd.to_datetime(data[column], format='%Y-%m-%d', errors='coerce')
                missing_dates_count = data[column].isna().sum()
                data.loc[:, column] = data[column].fillna(pd.Timestamp('today'))
                logging.info(f"Filled {missing_dates_count} missing dates in column {column}.")
        
        if config['transformations']['fill_missing_numeric_with_mean']:
            numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
            logging.info("Columns with numeric values categorized successfully")
            for column in numeric_columns:
                data.loc[:, column] = pd.to_numeric(data[column], errors='coerce')
                data.loc[:, column] = data[column].fillna(data[column].mean())
                logging.info(f"Filled missing values in column {column} with mean.")
        
        return data
    
    except Exception as e:
        logging.error(f"Error during transformation: {e}", exc_info=True)
        return None

def load_data(data, output_path):
    try:
        data.to_csv(output_path, index=False, encoding='utf-8')
        logging.info("Data loading successful.")
    except Exception as e:
        logging.error(f"Error during loading: {e}", exc_info=True)

# Pipeline execution
def etl_pipeline(config_path="config.yaml"):
    config = load_config(config_path)
    configure_logging(config['log_file'])
    
    raw_data = extract_data(config['input_path'])
    if raw_data is not None:
        transformed_data = transform_data(raw_data, config)
        if transformed_data is not None:
            load_data(transformed_data, config['output_path'])

# Example usage
if __name__ == "__main__":
    etl_pipeline()
