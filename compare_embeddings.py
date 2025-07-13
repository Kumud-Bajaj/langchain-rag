from langchain.embeddings import HuggingFaceEmbeddings
from langchain.evaluation import load_evaluator

def main():
    # Use HuggingFaceEmbeddings instead of OpenAIEmbeddings
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words using pairwise distance
    evaluator = load_evaluator("pairwise_embedding_distance", embeddings=embedding_function)
    words = ("apple", "iphone")
    result = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {result}")

if __name__ == "__main__":
    main()
