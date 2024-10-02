from embeddings import get_embeddings
import numpy as np

def main():
    reference_sentence = "What is your age range?"
    print(f"Reference sentence: {reference_sentence}")
    reference_embedding, _ = get_embeddings(reference_sentence);
    file_path = "sentences.txt"
    
    try:
        with open(file_path, 'r') as file:
            sentences = file.readlines()
        
        for sentence in sentences:
            sentence = sentence.strip()  # Remove any leading/trailing whitespace
            if sentence:  # Ensure the sentence is not empty
                embeddings_vector, tokens = get_embeddings(sentence)
                similarity = np.dot(reference_embedding, embeddings_vector) / (np.linalg.norm(reference_embedding) * np.linalg.norm(embeddings_vector))
                print(f"similary for '{sentence}': {similarity}, tokens used: {tokens}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()