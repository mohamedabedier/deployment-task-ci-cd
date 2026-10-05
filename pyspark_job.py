from pyspark.sql import functions as F

def clean_data(df):
    # 1. Remove rows where amount <= 0
    df_filtered = df.filter(F.col("amount") > 0)
    
    # 2. Remove rows where name is NULL
    df_filtered = df_filtered.filter(F.col("name").isNotNull())
    
    # 3. Add amount_with_tax column (amount * 1.20)
    df_final = df_filtered.withColumn("amount_with_tax", F.col("amount") * 1.20)
    
    return df_final