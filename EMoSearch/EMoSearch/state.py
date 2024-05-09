import reflex as rx
from typing import List, Tuple

class State(rx.State):
    words: str

    results:  List[Tuple[str, str, float]] = [("😿",":crying cat:",0.843),("🙀",":weary cat:", 0.802),("😼",":cat with wry smile:",0.779)]
	
    def get_results(self):
        answer = self.results
        self.words = ""    