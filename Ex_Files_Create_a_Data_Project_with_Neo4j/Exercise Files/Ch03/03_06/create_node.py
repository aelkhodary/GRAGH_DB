from py2neo import Graph , Node , NodeMatcher , Relationship 
from sqlalchemy import false , null

g = Graph("neo4j+s://c5fd76d0.databases.neo4j.io" , auth=("neo4j" , "VJmPcjo9G1SBxIvlDN5B2rDEej4PJd2QdDa7h_v7z50"))
matcher = NodeMatcher(g)
try:
   pass
   # 1- begin the transaction 
   tx = g.begin()
   # 2- check if the node exist 
   a = matcher.match("Person" , deviceID = "00000000001").first()
   if(a==None):
      a = Node ("Person" , deviceID = "00000000001" , user_name = "Tamer Khodary")
      tx.create(a)
      print(f'**Node had been created  : {a}')
   # 4- check if transaction successed 
   if(tx.exists(a)==False):
         raise Exception 
   
   # 5- create relationship
   b = matcher.match("Business" , business_id = '0322120-04-001').first()
   properties = {"scan_timestamp":"2022-01-01 17:57:42"}
   r= Relationship(a,"VISITED", b , **properties)
   #r.identity(None)
   tx.create(r)
   # 6- check if relationship created 
   if(tx.exists(r)== False):
        raise Exception
   
   # 7- commit 
   g.commit(tx)

# 8-ctach any exception 
except Exception as e :
    # 9-rollBack  
    g.rollback(tx)
    print(e)




   
    


   







