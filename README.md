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
   `from pyspark.sql.functions import expr`
    `return expr(f"""cast(concat(left(lpad(cast(hhmm_value AS STRING), 4, '0'),2), ':',`
   `left(lpad(cast(hhmm_value AS STRING), 4, '0'),2) AS INTERVAL HOUR TO MINUTE) """)`
