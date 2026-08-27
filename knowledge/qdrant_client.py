import os
import json
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from sentence_transformers import SentenceTransformer

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

COLLECTION_NAME = "incident_knowledge_base"

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# Produces 384-dimensional embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_incidents():
    with open("data/incidents.json", "r", encoding="utf-8") as f:
        return json.load(f)


def upload_incidents():
    incidents = load_incidents()
    points = []

    for incident in incidents:
        text = (
            f"Incident: {incident['incident']}. "
            f"Symptoms: {incident['symptoms']}. "
            f"Root cause: {incident['root_cause']}. "
            f"Blast radius: {incident['blast_radius']}. "
            f"Remediation: {incident['remediation']}. "
            f"Outcome: {incident['outcome']}."
        )

        vector = model.encode(text).tolist()

        points.append(
            PointStruct(
                id=incident["id"],
                vector=vector,
                payload=incident
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Uploaded {len(points)} incidents to Qdrant.")


if __name__ == "__main__":
    upload_incidents()
