# import os
import string
import numpy as np
# from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
# from app.services.summarize.sumarize import func

# dependencies = [
        #"nlp":nlp,
        # "label_embeddings":label_embeddings,
        # "all_labels":all_labels, 
        # "product_tree":product_tree,
        # "model":model,
        # "hi_en_product_tree":hi_en_product_tree,
        # "hi_en_all_labels":hi_en_all_labels,
        # "hi_en_label_embeddings":hi_en_label_embeddings
# ]


def generate_response(query: str, dependencies: dict, lang: str) -> str:
    ## Unpacking Dependencies
    nlp = dependencies["nlp"]
    label_embeddings = dependencies["label_embeddings"]
    all_labels = dependencies["all_labels"]
    product_tree = dependencies["product_tree"]
    model = dependencies["model"]
    hi_en_product_tree = dependencies["hi_en_product_tree"]
    hi_en_all_labels = dependencies["hi_en_all_labels"]
    hi_en_label_embeddings = dependencies["hi_en_label_embeddings"]

    ## Query Preprocessing
    # Query filtering
    query = query.lower()
    query = query.translate(str.maketrans('', '', string.punctuation))
    query = nlp(query)
    query = [token.text for token in query if not token.is_stop]
    query = " ".join(query)
    # getting Query Embeddings
    query_embedding = model.encode([query])[0]
    if lang == 'en':
        ## Getting most similar labels to our user query
        similarity = cosine_similarity([query_embedding], label_embeddings)[0]
        most_similar_label_index = np.argmax(similarity)
        # most_similar_label_index = similarity.argmax()
        most_similar_label = all_labels[most_similar_label_index]
        similarity_score = similarity[most_similar_label_index]
        ## Returning the response
        if similarity_score>0.55:
            return f"{product_tree[most_similar_label]['Desc']} Please visit: {product_tree[most_similar_label]['Link']}"
        else:
            return "Apologies, I do not have the info. Please contact here."
    else:
        ## Getting most similar labels to our user query
        similarity = cosine_similarity([query_embedding], hi_en_label_embeddings)[0]
        most_similar_label_index = np.argmax(similarity)
        most_similar_label = hi_en_all_labels[most_similar_label_index]
        similarity_score = similarity[most_similar_label_index]
        ## Returning the response
        if similarity_score>0.55:
            return f"{hi_en_product_tree[most_similar_label]['Desc']} Please visit: {hi_en_product_tree[most_similar_label]['Link']}"
        else:
            return "Apologies, I do not have the info. Please contact here."