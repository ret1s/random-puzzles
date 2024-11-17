from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def create_cassandra_connection():
    try:
        # connecting to the cassandra cluster
        cluster = Cluster(['172.17.0.1'], 9042)

        cas_session = cluster.connect('my_keyspace')

        return cas_session
    except Exception as e:
        print(f"Could not create cassandra connection due to {e}")
        return None
    
if __name__ == "__main__":
    create_cassandra_connection()