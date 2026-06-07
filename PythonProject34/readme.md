read config.yaml

and using .items to do column mapping

transformations:
  dropDuplicates: true
  column_mapping:
    cust_id : customer_id
    cust_name : customer_name
    cust_age : customer_age
	
for old, new in config["transformations"]["column_mapping"].items(): using mapping