		
			
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