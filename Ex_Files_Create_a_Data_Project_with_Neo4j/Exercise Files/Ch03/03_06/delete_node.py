from py2neo import Graph , Node , NodeMatcher , Relationship 
from sqlalchemy import false , null

g = Graph("neo4j+s://c5fd76d0.databases.neo4j.io" , auth=("neo4j" , "VJmPcjo9G1SBxIvlDN5B2rDEej4PJd2QdDa7h_v7z50"))
matcher = NodeMatcher(g)
try:
   pass
   # 1- begin the transaction 
   tx = g.begin()

   # 2- Delete relationship 
   delete_query = """MATCH (a:Person)-[r:VISITED]->(b:Bussiness)
        WHERE a.deviceID = $id_a AND b.business_id = $id_b
        AND r.scan_timestamp = $scan_timestamp
        DELETE r
        """

    # Assuming you have stored the identities of `a` and `b` somewhere
    # and you have the 'scan_timestamp' property value stored as well
   params = {
    "id_a": "00000000001",  # The stored identity of node `a`
    "id_b": "0322120-04-001",  # The stored identity of node `b`
    "scan_timestamp": "2022-01-01 17:57:42"
     }
   # Execute the delete query within the transaction
   tx.run(delete_query, params)


   # Step 1: Attempt to match the node you wish to delete
   a = matcher.match("Person", deviceID="00000000001").first()

   if a is not None:
      # Step 2: Delete the node using a Cypher command
      delete_query = "MATCH (n:Person {deviceID: $deviceID}) DELETE n"
      tx.run(delete_query, deviceID="00000000001")
      print(f"**Node requested for deletion: {a}")
   else:
      print("No matching node found.")

    # 7- commit 
   g.commit(tx)


   # Step 3: Optionally, you can check if the deletion was successful by trying to match the node again
   a_post_delete = matcher.match("Person", deviceID="00000000001").first()
   if a_post_delete is None:
      print("**Node successfully deleted")
   else:
     raise Exception("Node deletion failed or node still exists.")




  




# 8-ctach any exception 
except Exception as e :
    # 9-rollBack  
    g.rollback(tx)
    print(e)




   
    


   







