from qdrant_client import QdrantClient

# 1. Connecte-toi à Qdrant
client = QdrantClient(host="localhost", port=6333)

# 2. Vérifie la collection
print(client.get_collections())

# 3. Vérifie le nombre de points
print("Nombre de points:", client.count("collection_1"))

# 4. Crée un vecteur factice pour tester
vector = [0.01] * 768  # 768 = taille embedding

# 5. Test de recherche
results = client.search(
    collection_name="collection_1",
    query_vector=vector,
    limit=5
)

print("Résultats:", results)