		
			
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
   
   
   
   
   

    
   
   
   
   
        
        
     