from gensim.models import KeyedVectors
print("loading")
# Load the pre-trained Word2Vec model
model_path = '/Users/stephen/Dev/job_scrapper/GoogleNews-vectors-negative300.bin.gz'
word2vec_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

def generate_word_vector(word2vec_model: KeyedVectors, input_string: str):
    # Split the input string into words
    words = input_string.lower().split()

    # Filter out words that are not in the vocabulary
    words_in_vocab = [word for word in words if word in word2vec_model.key_to_index]

    # Check if there are words in the vocabulary
    if not words_in_vocab:
        print("No words in the vocabulary.")
        return None

    # Calculate the average word vector
    vectors = [word2vec_model[word] for word in words_in_vocab]
    average_vector = sum(vectors) / len(vectors)

    return average_vector.tolist()

# Example usage
print("Start")
while True:
    input_text = input("Enter a sentence: ")
    vector = generate_word_vector(word2vec_model, input_text)

    if vector is not None:
        print("length: ",len(vector), "Word vector:", vector)