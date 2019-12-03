class Word:

    def __init__(self, word, x, y):
        self.x = x
        self.y = y
        self.word = word
        self.all_points = []
        self.backwards = False

    def add_positions(self, positions):
        self.all_points.append(positions)

    def get_word(self):
        return self.word

    def get_positions(self):
        return self.all_points

    def get_facing(self):
        return self.backwards


