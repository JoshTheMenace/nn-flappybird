
class Score:
    score = 0

    def reset(self):
        self.score = 0

    def increase(self):
        self.score += 1

    def __str__(self):
        return str(self.score)
    
    def normalize(self):
        return int(self.score / 2)
