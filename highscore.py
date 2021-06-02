class HighScore:
    def __init__(self):
        self.high_score = 0
    
    def set_high_score(self, new_score: int):
        if new_score > self.high_score:
           self.high_score = new_score