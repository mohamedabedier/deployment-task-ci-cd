from pyspark.sql import functions as F

def clean_data(df):
    # 1. Remove rows where amount <= 0
    df_filtered = df.filter(F.col("amount") > 0)
    
    # 2. Remove rows where name is NULL
    df_filtered = df_filtered.filter(F.col("name").isNotNull())

    # 4. Remove amount more than 10000 
    df_filtered = df_filtered.filter(F.col("amount") <= 10000)
    
    # 3. Add amount_with_tax column (amount * 1.20)
    df_final = df_filtered.withColumn("amount_with_tax", F.col("amount") * 1.20)
    
    # 5. Add amount_category
    # ≤400 → low 
    # ≤700 → mid
    # ≤1000 → high
    df_final = df_final.withColumn("amount_category", 
                                      F.when(F.col("amount") <= 400 , "low")
                                      .when(F.col("amount") <= 700 , "mid")
                                      .otherwise("high")
                                      )
    return df_final