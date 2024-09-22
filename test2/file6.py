def calculate_embeddings(input):
    try:
        model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
        input_embedding = model.encode(input)
        return input_embedding
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None 