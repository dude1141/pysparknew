dataframe is runtime...

explicit schema

inferm schema

explicit schema---ddl schema, programtic schema

ddl schema

progrmatic schema




----inferschema if sees corrupte


ddl schema = "id int, name string, salary int, city string"

OR

schema= StructType([StructFiled("id", IntegerType(), true  ),
StructFiled("name", StringType(), true  ),
StructFiled("salary", IntegerType(), true  ),
StructFiled("city", StringType(), true  )])


readmode:
by default permissive, if there is issue with values all rwos will be null with explicait schema

 with infermschema read mode will not work

thats why we need explicit schema

1) .schema(explicit schema).option("mode",dropmalformed)
2) .schema(explicait schema).option("mode",Failfast)---if courupted records are there then it will FAIl 
3) 



1) apple is a good girl, apple is a bad girl 

Split converts (Array(Array())
	Array(Array(apple ,is, a, good, girl), Array(apple ,is ,a ,bad, girl ))
2) Flatmap converts complext to simple data STRUCTURE

	Array (apple ,is, a, good, girl,apple ,is ,a ,bad, girl)
	


but if you want to count use map:

3) 	map(lmabda x:(x,1)----> converst to keyvalue pairs
	
	apple 1,	apple ,1
	is ,1 ,is 1
	
4) reduceBykey----converst to apple,2  and is 2
	works only with values keeping Key as constant...
	Summation function.
	brings all keys to similar machine
	Each machine performs local aggregation within its partitions.
    Shuffling brings together values with the same key on the same machine.

5)  each machien perform slocal GROUPING
	shuffle brings togather values with samekey  on same machine
	final grouping is done on each machine
	


collect vs take vs saveastextile


(1,"Raaj",3)
SortBykey:
	(x==>x._3,false)


Repartition and COALESCE"

def funct(df):
	return df.select(
		col("id"),
		col("name"),
		col("salary"),
		col("city"),
		when(col("salary")> 1000 ,"RICH")
		.Otherwise("poor"))

funct(df)


/*	
scala
def status(df:Dataframe):Dataframe={
*/
	

}





class readingfilesinpyspark :

    def __init__(self):
        self.spark = SparkSession.builder \
        .appName("test") \
        .master("local[*]") \
        .getOrCreate()
# data = r"C:\Users\mouni\Downloads\details-2026-04-05.csv"
        self.schema1 = StructType ([StructField ("id", IntegerType()),
                        StructField ("name", StringType()),
                      StructField("Salary", IntegerType()),
                StructField("city", StringType())
                      ])
        # self.df = None

    def main(self):
        data = r"C:\Users\mouni\Downloads\details-2026-04-05.csv"
        # reader = readingfilesinpyspark("test")
        df = self.spark.read.format("csv").option("header","True") \
                .option("mode","DROPMALFORMED") \
                .schema(self.schema1).load(data)
        df.printSchema()
        df.show(100)

if __name__ == "__main__":
    app = readingfilesinpyspark()
    app.main()

# }


df =spark.createDataFrame([("abc.def.ghi",)],["col1"])
df.select(substring_index(col("col1"),".",1).as("sub_index")
you get abc
	      
2.345  ---> round 2.35

2.344  ---->  2.34

concat(col(col1),lit(" "),col2,lit(""))

concat_ws(" ",col1,col2) 





data = [
    (1, "  karthik  ", " hyderabad ", " india "),
    (2, " ravi ", " mumbai ", " india "),
    (3, " anitha ", " bangalore ", " india "),
    (4, " john ", " new york ", " usa ")
]

columns = ["id", "name", "city", "country"]

from pyspark.sql.functions import upper, col
df2= spark.createDataFrame(data,columns)
df2.show()
columnlist =["name","city","country"]

def uppers(df):
    for i in columnlist:
        df = df.withColumn(i, upper(col(i)))
        return df

df3=uppers(df2).show()




df2= spark.createDataFrame(data,columns)
# df2.show()
columnlist =["name","city","country"]

# id then append to other column apply function 
def uppers(df):
    cols = [col("id")]
    for i in columnlist:
        cols.append(upper(trim(col(i))).alias(i))
    
    df = df.select(*cols)
    return df


Dynamic nature: using config and for old,new in mapping


#config is dictionary, how to access using keys
config ={

    "source_path":"/landing/data/customer/",
    "file_name":"info.csv",
    "file_format":"csv"

}
spark.read.format(config["file_format"]).option("header","true").option("path",config["source_path"])
.load()

#use dictionary column mapping for columnmapping:

 ColumnNameChangesMapping = {
 
			"cust_id":"customer_id",
			"cust_name":"customer_name"
			
 }
	for old,new in mapping.items():
		df1=df.withcolumn(old,new)
			
	
3. 	customers.csv
	orders.csv 
	cric.csv 
	
	
	data folder--->customer folder 
				--->customer folder
	customers folder -- customers.csv similary for ordeers folder etc 
	
	filemapping={
	
		"customer":"/data/customer*"
		"orders":"/data/orders/*"
		"payments":"/data/payments/*"		
	
	}

	for file,path in filemapping.items():
			df =spark.read.format("csv").option("path",filemapping["customer"]).load()
			
			
	4 lookup logics:
	===============================
	
	
	detp= {
	1024:"hr",
	345:"IT",
	3567:"Sales"	
	}
	
	5: METADRIVEN ETL pipelines
	===========================
	PIPELINE ={
	
		"SOURCE":"S3://LANDINGZONE",
		"TARGET":"REDSHIFT",
		"MODE":"APPEND",
		"PARTITION":"DATE"
	
	}
			
   -- THESE 5 points we discussed is for dictionary in  python

	below are for Scala using MAP:
	
	
	val config =Map{

    "source_path"->"/landing/data/customer/",
    "file_name"->"info.csv",
    "file_format"->"csv"

}



PURE FUNCTION:

	


members_df = (
spark.table("dev.spark_db.members") .filter(col("last_name")=="GUEST")
)

bookings_df = (
    spark.table("dev.spark_db.bookings") 

)

facilities_df = spark.table("dev.spark_db.facilities").alias("f")

..


Grouop by and window:

multicolumn Aggreagations:
	1) groupBy aggregations  foreg: max salary department both...
	2)  window by aggreagations 
	
	select aggregated , non-aggregated cols from tables group by non-aggregated columns ; combination needs groupBy
	
	select aggregated cols from tables; dont need groupby
	
	select non-aggregated cols from table ; dont need groupby
	

df.groupBy(dept).agg(max("salary"))

id dept salary
1  chem  45
2  chem  60
3  pharm  30

df21 = df13.groupBy(col("city")).agg(min(col("Temperature")),max(col("Temperature")), avg(col("Temperature")))


window aggreagations:

	productid productname sales date 
	123        maggi        300  26thmay
	123		   maggi		300  26thmay
	123		   maggi		400  27thmay
	
get sales of last week:
	sum--oneweek limitaiont window
	

id dept salary
1  chem  45
2  chem  60
3  pharm  30
4  pharm  66

get max salry each department

		df13.groupBy(col("dept")).agg(min(col("Temperature")),max(col("Temperature")), avg(col("Temperature")))



1) rows between unbounded proceeding and  currentrow

id   dept salary cumulativesal
1	 chem 	
2    chem 
3    pharma
4




1------1 feet  ---unboundepreceeding is first row
2--------1+2=3 feet
3------1+2+3=6 feet
rows between unbounded preceeding and current row 


rows between unboundepreceeding is first row
current row= where 


syntax:
	
	
	Windows=Window.partitionBy("..").orderBy(desc(col("colname"))).rowsBetween(Window.unboundedPreceedding,currentRow)
	
	
	result= df.select(col,col2,col3....sum(col("salary")).over(Windows)
	
	windows get executed row byrow
	
	
	a= window.orderBy("id").rowsbetween(window.UnboundedPreceeding ,Window.currentRow)
	
	
	running sum 
	
	moving sum
	
	cumulative sum 
	
	calcluate the avg rating of each user based on last 3 ratings
	
	
what ever you give it does rowby row and starts from first columns

scoreData1 = [
 (1,"Movie1",  4.5),  -2 where ever you stand you need last 3 ratings  4.5
 (1,"Movie2",  4.0),      4.5+4.0/2 =4.25
 (1,"Movie3",  2.5),      4.5+4.0+2.5/3= 
 (2,"Movie1",  4.0),   4.0 
 (2,"Movie2",  4.1),    4.0+4.1/2=
 (2,"Movie3",  4.6),   4.0+4.1+4.6/3=
(2,"Movie6",  3.0),
(2,"Movie7",  3.8)

rowsbetween(-2,0) ---> 2 previous rows + current row






So for each user:
current rating
previous rating
previous previous rating

That gives the last 3 ratings including the current rating.


you need last 3 ratings ,where ever you are from there last 3 ratings.



rowsbetween(0,2) ---first three ratings


scoreData1 = [
 (1,"Movie1",  4.5   ----0  4.5+4.0+2.5/3=
 (1,"Movie2",  4.0   -----1
 (1,"Movie3",  2.5   ------2 
 (2,"Movie1",  4.0
 (2,"Movie2",  4.1
 (2,"Movie3",  4.6
(2,"Movie6",  3.0)
(2,"Movie7",  3.8)


rowsbetween(-1,0)------>last 2 ratings ---rolling size of window 2

rolling size of window 5 means  rowsbetween(-4,0)





lead and lag:

lead : next ----- lead (colname, offsetvlaue)

lag : previous 


id name 	salary lead(salary,1)
1  mohna     56          45
2   veer     45           31
3   vijay    31           25
4    veena   25            null

members_df = (
spark.table("dev.spark_db.members") .filter(col("last_name")=="GUEST")
)

bookings_df = (
    spark.table("dev.spark_db.bookings") 

)

facilities_df = spark.table("dev.spark_db.facilities").alias("f")

..


Grouop by and window:

multicolumn Aggreagations:
	1) groupBy aggregations  foreg: max salary department both...
	2)  window by aggreagations 
	
	select aggregated , non-aggregated cols from tables group by non-aggregated columns ; combination needs groupBy
	
	select aggregated cols from tables; dont need groupby
	
	select non-aggregated cols from table ; dont need groupby
	

df.groupBy(dept).agg(max("salary"))

id dept salary
1  chem  45
2  chem  60
3  pharm  30

df21 = df13.groupBy(col("city")).agg(min(col("Temperature")),max(col("Temperature")), avg(col("Temperature")))


window aggreagations:

	productid productname sales date 
	123        maggi        300  26thmay
	123		   maggi		300  26thmay
	123		   maggi		400  27thmay
	
get sales of last week:
	sum--oneweek limitaiont window
	

id dept salary
1  chem  45
2  chem  60
3  pharm  30
4  pharm  66

get max salry each department

		df13.groupBy(col("dept")).agg(min(col("Temperature")),max(col("Temperature")), avg(col("Temperature")))



1) rows between unbounded proceeding and  currentrow

id   dept salary cumulativesal
1	 chem 	
2    chem 
3    pharma
4




1------1 feet  ---unboundepreceeding is first row
2--------1+2=3 feet
3------1+2+3=6 feet
rows between unbounded preceeding and current row 


rows between unboundepreceeding is first row
current row= where 


syntax:
	
	
	Windows=Window.partitionBy("..").orderBy(desc(col("colname"))).rowsBetween(Window.unboundedPreceedding,currentRow)
	
	
	result= df.select(col,col2,col3....sum(col("salary")).over(Windows)
	
	windows get executed row byrow
	
	
	a= window.orderBy("id").rowsbetween(window.UnboundedPreceeding ,Window.currentRow)
	
	
	running sum 
	
	moving sum
	
	cumulative sum 
	
	calcluate the avg rating of each user based on last 3 ratings
	
	
what ever you give it does rowby row and starts from first columns

scoreData1 = [
 (1,"Movie1",  4.5),  -2 where ever you stand you need last 3 ratings  4.5
 (1,"Movie2",  4.0),      4.5+4.0/2 =4.25
 (1,"Movie3",  2.5),      4.5+4.0+2.5/3= 
 (2,"Movie1",  4.0),   4.0 
 (2,"Movie2",  4.1),    4.0+4.1/2=
 (2,"Movie3",  4.6),   4.0+4.1+4.6/3=
(2,"Movie6",  3.0),
(2,"Movie7",  3.8)

rowsbetween(-2,0) ---> 2 previous rows + current row






So for each user:
current rating
previous rating
previous previous rating

That gives the last 3 ratings including the current rating.


you need last 3 ratings ,where ever you are from there last 3 ratings.

rowsbetween(0,2) ---first three ratings


space remoives
ltrim
rtrim
trim


renaming columns using withcolumnRename(col,newcolname)

and using toDF to rename multiple columns


df ---id name age

df.toDF("studentid,"studentname",studentage")


CAST:
col("name").cast("string")

looping 

from pyspark.sql.functions import upper, col
df2= spark.createDataFrame(data,columns)
df2.show()
columnlist =["name","city","country"]

def uppers(df):
    for i in columnlist:
        df = df.withColumn(i, upper(col(i)))
        return df

df3=uppers(df2).show()



handling nulls:

	filter 
	
	Na functions for filling nulls:
		
	na.fill
	na.drop
	
	id name age 
	1  mohan null 
	null veer 86
	3 	null 36
	
	df.na.fill("na")
	
	id name age 
	1  mohan na 
	na veer 86
	3 	na 36
	
	df.na.fill(subset=[colname,value="na"])
	df.na.drop
	
	
	
	drop duiplicates
	
	
	using distinct  df.distinct
	
	dropduplicates   df.dropDuplicates(colnamae)
	
	dropping using window at production level
		
	
	Padding:
	
	LPAD, RPAD..
	
	colname karthik
	lpad(colname,15,'*')
	
	*********karthik
	
	
	date:
	string fromat related date col --"2025-01-01"
	
	best way use to_date(col("string fromat related date col"))
	
	then format like yyyy mm dd or dd mm yyyy 
	
	
	to_timestamp(col("15:30:00")) converts string to timestamp
	
	
	withcolumn("daysdiff",date_add())
	
	
	
	df.withColumn("date1",coalesce("date1",lit("2026-03-01")))
	

