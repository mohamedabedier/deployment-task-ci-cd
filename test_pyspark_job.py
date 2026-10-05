import pytest
from pyspark.sql import SparkSession
from pyspark_job import clean_data

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder \
        .master("local[1]") \
        .appName("pytest-pyspark") \
        .getOrCreate()

def test_clean_data(spark):
    mock_data = [
        ("Alice", 100.0),  # good data
        ("Bob", -50.0),    # bad data (-ve value)
        ("Charlie", 0.0),  # bad data (0 value)
        (None, 200.0)      # bad data (no name)
    ]
    columns = ["name", "amount"]
    df = spark.createDataFrame(mock_data, columns)

    result_df = clean_data(df)
    results = result_df.collect()

    # 3. check by Assert
    
    # only one row are good data
    assert len(results) == 1
    
    valid_row = results[0]
    
    assert valid_row["name"] == "Alice"
    assert valid_row["amount"] == 100.0
    
    assert valid_row["amount_with_tax"] == 120.0