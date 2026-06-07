from utils import load_config
from reader import read_data
# from transformer import transformed  # fixed typo: transfomer -> transformer
from writer import write_data
from pyspark.sql import SparkSession



column_mapping = { "cust_id": "customer_id", "cust_name": "customer_name", "cust_age": "customer_age" }


