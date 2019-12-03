from search.word_base import WordBase
from search import word_class as wc


class Diagonal(WordBase):

    def __init__(self, grid, all_points):
        super().__init__(grid, all_points)

    def add_to_grid(self, word_class):
        if self.check_all_points(word_class.all_points):
            for l in range(len(word_class.word)):
                self.grid[word_class.all_points[l][0]][word_class.all_points[l][1]] = word_class.word[l]
        else:
            self.create_word_diagonal(word_class.word)

    def create_word_diagonal(self, word):
        start = self.create_start_points()
        not_in_list = self.check_start_points(start)

        if not_in_list:
            word_class = wc.Word(word, start[0], start[1])

            if word_class.y + len(word) <= 10 and word_class.x + len(
                    word) <= 10:  # TODO replace ten with length of grid lists

                for l in range(len(word)):
                    word_class.add_positions((word_class.y + l, word_class.x + l))

                self.add_to_grid(word_class)

            elif word_class.y - len(word) >= 0 and word_class.x - len(word) >= 0:
                word_class.backwards = True
                for l in range(len(word)):
                    word_class.add_positions((word_class.y - l, word_class.x - l))

                self.add_to_grid(word_class)

            else:
                self.create_word_diagonal(word)

        else:
            self.create_word_diagonal(word)
