from qdrant_client import QdrantClient

# Connexion à Qdrant
client = QdrantClient(host="localhost", port=6333)

# Vérifie combien de points il y a dans ta collection
collection_name = "1"  # Remplace par le vrai nom de ta collection
count = client.count(collection_name=collection_name)

print(f"Nombre de points dans la collection '{collection_name}': {count['count']}")