Apple Analysis project reference: \
https://www.youtube.com/watch?v=BlWS4foN9cY


# PySpark Project

A Python project for learning and working with Apache Spark.

## Git Commands

### Initial Setup
```bash
# Add the remote repository
git remote add origin https://github.com/dude1141/pysparknew
```

### Staging Changes
```bash
# Stage all changes and untracked files
git add -A
```

### Committing Changes
```bash
# Create an initial commit with all project files
git commit -m "Initial commit: Add PySpark project files"
```

### Pushing to Remote
```bash
# Push local commits to the remote repository
git push -u origin master
```

### Other Useful Commands
```bash
# Check git status
git status

# View remote configuration
git remote -v
```

## Project Files
- `readingfilesinpyspark.py` - Main PySpark script
- `Pysparknotes_2026.pdf` - PySpark notes and documentation
- [DIAGRAM.md](DIAGRAM.md) - Project diagram (view & download via Excalidraw)



## spark types
- `transformating muliplte columns, we use dictionary:CRS_DEP_TIME:expr(""")`
- 'transform CRS_DEP_TIME to an interval

- `departur time, 1111 ,710 7hours 10 min , 2 digits from left as hr and 2digit from right as min`
- `lpad(CRS_DEP_TIME ,4,'0') 650 becomes 0650`
- `expr("left(lpad(CRS_DEP_TIME,4,'0'), 2)")
step1df = ( flight_time_raw_df.withColumns({
    "CRS_DEP_TIME_HH":expr("left(lpad(CRS_DEP_TIME,4,'0'), 2)"),
    "CRS_DEP_TIME_MM":expr("right(lpad(CRS_DEP_TIME,4,'0'), 2)")
    })
  `
- `def getinterval(hhmm_value): `
  - `from pyspark.sql.functions import expr`
   - `return expr(f"""cast(concat(left(lpad(cast(hhmm_value AS STRING), 4, '0'),2), ':',`
   - `left(lpad(cast(hhmm_value AS STRING), 4, '0'),2) AS INTERVAL HOUR TO MINUTE) """)`

## casting using try cast and handling nil 

    - `transaction_id	customer_name	dop	purchase_amount	discount`
    - '100	Prashant	2020-06-15	12000	18.5`
    - `101	David	2018-08-7	15000	nil`
    - `102	Simran	14-05-2019	3000000000	21`

- `try cast is use for eg 18.5 we can cast to double, for nil it will fail so we use try_cast`
- `here try cast converting nil it will return instead of null and top of that we apply nvl`
- `converting nil and null values to zero`

-` df3 = df3.selectExpr("customer_name",
                     "nvl(try_cast(dop as date), to_date(dop,'dd-MM-yyyy')) as date_of_purchase",
                     "nvl(try_cast(discount as double),0) as applied_discount",
                     "purchase_amount",
                     "transaction_id").filter("purchase_amount is not null") `
## case when

  - ` df3 = df3.selectExpr("increment", expr(" case when salary > 300000 then 3000 else salary* 10/100 end").withCoumn("salary", expr("increment+salary"))`

## withColumn using col and Expr
- ` flight_time_df1 = (flight_time_df.withColumnRenamed("fl_date","dep_date")
.withColumn("arr_date",expr("to_date(dep_date + dep_time + wheels_on + taxi_in) as arr_date"))
.withColumns({"crs_dep_date": expr("dep_date + crs_dep_time"),
"dep_time": expr("dep_date + dep_time"),
"crs_arr_time": expr("arr_date + crs_arr_time"),
"arr_time": expr("arr_date + arr_time"),})
)`

## Use `withColumn`, `expr`, and `selectExpr` to transform DataFrames.r

    - ` flight_time_df12 = (flight_time_df.withColumnRenamed("fl_date","dep_date")
.withColumn("arr_date", to_date(col("dep_date") + col("dep_time") + col("wheels_on") + col("taxi_in")))
.withColumns({"crs_dep_date": col("dep_date") + col("crs_dep_time"),
"dep_time": col("dep_date") + col("dep_time"),
"crs_arr_time": col("arr_date") + col("crs_arr_time"),
"arr_time": col("arr_date") + col("arr_time")})
)`
