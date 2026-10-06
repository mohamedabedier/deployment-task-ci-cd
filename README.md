# PySpark DataOps & CI Pipeline 🚀

Welcome to the **deployment-task-ci-cd** repository! This project demonstrates a complete DataOps workflow for a PySpark data processing job. It features a robust Continuous Integration (CI) pipeline using **GitHub Actions** and **Pytest** to automatically validate data transformations and enforce data quality rules before deployment.

## 📌 Project Overview

In modern Data Engineering (like Medallion Architectures), moving data from the **Bronze** (raw) to the **Silver** (cleansed) layer requires strict quality gates. This project implements a PySpark ETL job that cleanses transactions and enriches the data, protected by a CI pipeline that prevents bad logic from reaching production.

## ⚙️ Business Rules Implemented

The core transformation function (`clean_data` in `pyspark_job.py`) applies the following rules:
1. **Data Quality:** Removes records with invalid negative or zero amounts.
2. **Data Integrity:** Filters out records missing a customer name (`NULL`).
3. **Outlier Detection:** Removes transactions exceeding 10,000.
4. **Enrichment (Tax):** Calculates a 20% tax and adds an `amount_with_tax` column.
5. **Categorization:** Classifies transactions into `low` (≤400), `mid` (≤700), or `high` (>700) tiers.

## 🚀 Continuous Integration (CI) Pipeline

This repository is configured with a GitHub Actions workflow (`.github/workflows/ci.yml`). 
Whenever a **Pull Request** is opened or code is pushed to the `main` branch, the pipeline automatically:
1. Provisions an Ubuntu runner.
2. Sets up Python.
3. Installs dependencies (`pyspark` and `pytest`).
4. Executes the unit tests in `test_pyspark_job.py` using a local SparkSession.
5. Blocks the merge if any data quality assertions fail.

## 📁 Repository Structure

- `.github/workflows/`: Contains the GitHub Actions CI pipeline configuration.
- `pyspark_job.py`: The main PySpark transformations written as pure, testable functions.
- `test_pyspark_job.py`: The Pytest suite with mock data and strict assertions.
