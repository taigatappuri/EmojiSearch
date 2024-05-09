import reflex as rx
from typing import List, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
import sentencepiece as spm
import tqdm as notebook_tqdm
import pandas as pd
import os
#日本語のテキスト埋込モデル(GLuCoSE)をロード
#https://huggingface.co/pkshatech/GLuCoSE-base-ja
model = SentenceTransformer('pkshatech/GLuCoSE-base-ja')
emojis_data = pd.read_csv('Data/emojis_data.csv')
#絵文字の名前を埋め込み
emoji_embeddings = model.encode([ed for ed in emojis_data["name_ja"]])


class State(rx.State):
    words: str

    results: List[Tuple[str, str, float]]
    
    def get_results(self):
        answer = self.results
    
        input_embedding = model.encode([self.words])
        
        emoji_embeddings_norm = emoji_embeddings / np.linalg.norm(emoji_embeddings, axis=1, keepdims=True)
        input_embedding_norm = input_embedding / np.linalg.norm(input_embedding)
        cosine_similarities = np.dot(emoji_embeddings_norm, input_embedding_norm.T)
        closest_emoji_indices = np.argsort(-cosine_similarities, axis=0)[:5].flatten()
        closest_emojis = emojis_data.iloc[closest_emoji_indices]
        
        for index, row in closest_emojis.iterrows():
            emoji_row = emojis_data.iloc[index]
            emoji = row['emoji']
            emoji_name = emoji_row['name']
            similarity = cosine_similarities[index][0]
            print(emoji, emoji_name, similarity)
            self.results.append((emoji, ":"+emoji_name+":", float(similarity)))
        self.words = ""    
