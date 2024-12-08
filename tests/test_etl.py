import pytest
import pandas as pd
from modular_etl import extract_data, transform_data, load_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "employee_id": [1, 2, 2, 3],
        "name": ["Alice", "Bob", "Bob", None],
        "salary": [50000, 60000, 60000, None],
        "date_of_joining": ["2020-01-01", None, None, "2021-03-15"]
    })

@pytest.fixture
def sample_config():
    return {
        "transformations": {
            "fill_missing_numeric_with_mean": True,
            "text_to_uppercase": True,
            "fill_missing_dates": True,
        }
    }

def test_extract_data(tmp_path):
    # Create a temporary CSV file
    test_file = tmp_path / "sample_input.csv"
    pd.DataFrame({"id": [1, 2, 3]}).to_csv(test_file, index=False)

    # Call the extract function
    data = extract_data(test_file)

    # Assert data is not None and contains expected rows
    assert data is not None
    assert not data.empty
    assert len(data) == 3  # Verify the number of rows

def test_transform_data(sample_data, sample_config):
    # Call the transform function
    transformed_data = transform_data(sample_data, sample_config)

    # Assertions
    assert len(transformed_data) == 3  # Duplicates removed
    assert transformed_data["salary"].isnull().sum() == 0  # Missing numeric values filled
    assert transformed_data["name"].str.isupper().all()  # Names converted to uppercase
    assert transformed_data["date_of_joining"].isnull().sum() == 0  # Missing dates filled

def test_load_data(sample_data, tmpdir):
    output_path = tmpdir.join("output.csv")
    load_data(sample_data, str(output_path))

    # Assert the output file exists
    assert output_path.exists()

    # Verify the file contents
    loaded_data = pd.read_csv(output_path)
    pd.testing.assert_frame_equal(loaded_data, sample_data)
