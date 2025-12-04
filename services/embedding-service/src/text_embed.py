from embedder import embed_text

sample =  "auth-service error token expired"

vec = embed_text(sample)
print("vector dims", len(vec))
print("Preview: ", vec[:5])