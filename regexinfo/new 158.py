a= ("abc1234cde678")			

sql:			
regex_substr((input),lit("([0-9]+),1,2")) ---1,2 1 is where to start and 2 is second combination


regex_replace


abc1234cde678
regexp_extract(col(input),lit("([0-9]+)"),1) here in pyspark 1 is groupindex
you get answser as 1234, if alphabet comes continutity breaks

ifyou remove + answers is 1 only


			
df.select(regexp_substr(col("value"),lit("([0-9]+)"))).show()
1234

df.select(regexp_substr(col("value"),lit("([0-9])"))).show()
1

df.select(regexp_extract(col("value"),lit("([0-9]+)"), 1)).show()
1234


extract alphabets [a-z]+

abc1234cde678
df.select(regexp_extract(col("value"),lit("([a-z]+)"), 1)).show() #case sensitive
abc

c)
   ^power ^[0-9]+ extract numnericals present at the starting
   $dollar [0-9]$+ extract numnericals from the end
 
 
 d) sis@gmail.com 
 
    @[A-Za-z]+  , after @ if you find alphabet extract items  --gmail
    
    @[A-Za-z.]+  gmail.com  
    
    
    df.select(regexp_extract(col("value"),lit("(@[A-Za-z]+)"), 1))
    
    try both
    df.select(regexp_extract(col("value"),lit("\\.([A-Za-z]+)"), 1))
    df.select(regexp_extract(col("value"),lit("//.([A-Za-z]+)"), 1))
    
 e) 


 "([a-z]+)([0-9]+)"
 ^^^^^^^^ ^^^^^^^^
 Group 1  Group 2



df.select(regexp_extract(col("value"),"([0-9])([a-z]+)", 2)).show() #case sensitive
answer is cde

if groupindex is 1 then answer is 1

df.select(regexp_extract(col("value"),"([0-9]+)([a-z]+)", 1)).show() #case sensitive
1234



.DOT operator:
    match any single character except newline
    
    
    input:  output 
    cat     c  
    cot     c
    cot     c
    cpt     c
    mat     m
    
    
    1) ([c.t]) -----> regex_extract(col("input"))."([c.t])"  try with +  also try with c*t
    
    
    
    *:start:
    
    + one or more character --- atleast
    
    [0-9]+ 
    
    * : zero or more matches
    
   2)  regex_extract(col("input"))."([c*t])" 
    
    
    c*t c  can be zero or  more
    
    
    List(("color","oxygen"),("colour","neo"),("colorrrrrr","ceat"))
    
    3)   colou?r   ----->  regex_extract(col("input"), "(colou?r",1)
    
    
    4)  regex_extract(col("input"), "([A-Za-z]{2,5}",1)
    
                min max characters matching try with List
                
    5)   List(("mith ssss ","oxygen"),("colour","neo"),("colorrrrrr","ceat"))
    
            regex_extract(col("input"), "((\\s+)+",1)
            
     
     word Boundary:
     
        summer is so cat so we 
        
        regex_extract(col("input"), "(\\cat\\b)+",1)
        
        regex_extract(col("input"), "(\\bcat\\b)+",1) --word boundary
        
        
   grouping 
   ------------
   
   arc@gmail.com 
   
   arc.1@gmail.com
   
   arc1.sm@gmail.com
   
   arc1.st@ai
   
   [A-Za-z0-9._-]+ @[A-Za-z0-9]+\\.[A-za-z]{2,3}
                                     
   thisaccepts everyusername then @ and then have after . this fashion min 2 character and  max 3 charcters
			
a= ("abc1234cde678")			

sql:			
regex_substr((input),lit("([0-9]+),1,2")) ---1,2 1 is where to start and 2 is second combination


regex_replace


abc1234cde678
regexp_extract(col(input),lit("([0-9]+)"),1) here in pyspark 1 is groupindex
you get answser as 1234, if alphabet comes continutity breaks

ifyou remove + answers is 1 only


			
df.select(regexp_substr(col("value"),lit("([0-9]+)"))).show()
1234

df.select(regexp_substr(col("value"),lit("([0-9])"))).show()
1

df.select(regexp_extract(col("value"),lit("([0-9]+)"), 1)).show()
1234


extract alphabets [a-z]+

abc1234cde678
df.select(regexp_extract(col("value"),lit("([a-z]+)"), 1)).show() #case sensitive
abc

c)
   ^power ^[0-9]+ extract numnericals present at the starting
   $dollar [0-9]$+ extract numnericals from the end
 
 
 d) sis@gmail.com 
 
    @[A-Za-z]+  , after @ if you find alphabet extract items  --gmail
    
    @[A-Za-z.]+  gmail.com  
    
    
    df.select(regexp_extract(col("value"),lit("(@[A-Za-z]+)"), 1))
    
    try both
    df.select(regexp_extract(col("value"),lit("\\.([A-Za-z]+)"), 1))
    df.select(regexp_extract(col("value"),lit("//.([A-Za-z]+)"), 1))
    
 e) 


 "([a-z]+)([0-9]+)"
 ^^^^^^^^ ^^^^^^^^
 Group 1  Group 2



df.select(regexp_extract(col("value"),"([0-9])([a-z]+)", 2)).show() #case sensitive
answer is cde

if groupindex is 1 then answer is 1

df.select(regexp_extract(col("value"),"([0-9]+)([a-z]+)", 1)).show() #case sensitive
1234



.DOT operator:
    match any single character except newline
    
    
    input:  output 
    cat     c  
    cot     c
    cot     c
    cpt     c
    mat     m
    
    
    1) ([c.t]) -----> regex_extract(col("input"))."([c.t])"  try with +  also try with c*t
    
    
    
    *:start:
    
    + one or more character --- atleast
    
    [0-9]+ 
    
    * : zero or more matches
    
   2)  regex_extract(col("input"))."([c*t])" 
    
    
    c*t c  can be zero or  more
    
    
    List(("color","oxygen"),("colour","neo"),("colorrrrrr","ceat"))
    
    3)   colou?r   ----->  regex_extract(col("input"), "(colou?r",1)
    
    
    4)  regex_extract(col("input"), "([A-Za-z]{2,5}",1)
    
                min max characters matching try with List
                
    5)   List(("mith ssss ","oxygen"),("colour","neo"),("colorrrrrr","ceat"))
    
            regex_extract(col("input"), "((\\s+)+",1)
            
     
     word Boundary:
     
        summer is so cat so we 
        
        regex_extract(col("input"), "(\\cat\\b)+",1)
        
        regex_extract(col("input"), "(\\bcat\\b)+",1) --word boundary
        
        
   grouping 
   ------------
   
   arc@gmail.com 
   
   arc.1@gmail.com
   
   arc1.sm@gmail.com
   
   arc1.st@ai
   
   [A-Za-z0-9._-]+ @[A-Za-z0-9]+\\.[A-za-z]{2,3}
                                     
   thisaccepts everyusername then @ and then have after . this fashion min 2 character and  max 3 charcters
  
  			
			
			
a= ("abc1234cde678")			

sql:			
regex_substr((input),lit("([0-9]+),1,2")) ---1,2 1 is where to start and 2 is second combination


regex_replace


abc1234cde678
regexp_extract(col(input),lit("([0-9]+)"),1) here in pyspark 1 is groupindex
you get answser as 1234, if alphabet comes continutity breaks






Consider only regular memebrs (not guest) and direct members(not recomended by any other member)
Consider only bookings for more than 8 hours
Ensure all regular and direct members are listed even if they have no 8 hour bookings
Ensure all 8 hour bookings are listed even if they are not made by regular and direct members
Sort the report by slots and first name in ascending order



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
	
	   