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
        ("Alice1", 100.0),  # good data (low)
        ("Alice2", 500.0),  # good data (mid)
        ("Alice3", 9000.0), # good data (hige)
        ("Bob", -50.0),     # bad data (-ve value)
        ("Charlie", 0.0),   # bad data (0 value)
        (None, 200.0)       # bad data (no name)
        ("Ali", 12000.0)    # bad data (amont is more than 10000)
    ]
    columns = ["name", "amount"]
    df = spark.createDataFrame(mock_data, columns)

    result_df = clean_data(df)
    results = result_df.collect()

    # 3. check by Assert
    
    # now become three rows are good data
    assert len(results) == 3
    

    # try all the 3 categories
    # Alice1
    assert results[0]["name"] == "Alice"
    assert results[0]["amount"] == 100.0
    
    assert results[0]["amount_with_tax"] == 120.0

    assert results[0]["amount_category"] == "low"

    # Alice2
    assert results[1]["name"] == "Alice"
    assert results[1]["amount"] == 500.0
    
    assert results[1]["amount_with_tax"] == 600.0

    assert results[1]["amount_category"] == "mid"

    # Alice3
    assert results[2]["name"] == "Alice"
    assert results[2]["amount"] == 900.0
    
    assert results[2]["amount_with_tax"] == 1080.0

    assert results[2]["amount_category"] == "high"