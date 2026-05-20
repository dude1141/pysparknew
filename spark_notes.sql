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

	

