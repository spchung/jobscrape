from neo4j_database import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "neo4j1234")

driver = GraphDatabase.driver(URI, auth=AUTH)

def get_driver():  
  if not driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
  driver.verify_connectivity()
  return driver
