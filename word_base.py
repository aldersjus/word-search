import random as r


class WordBase:

    def __init__(self, grid, all_points):
        self.grid = grid
        self.all_points = all_points
        self.start_points = []
        self.start_x = 0
        self.start_y = 0

    def create_start_points(self):
        self.start_x = r.randrange(0, len(self.grid))
        self.start_y = r.randrange(0, len(self.grid))
        start = (self.start_x, self.start_y)
        return start

    def check_start_points(self, start):
        ok = True
        for st in self.start_points:
            if st == start:
                ok = False

        if ok:
            self.start_points.append(start)
        return ok

    def check_all_points(self, word_points):
        ok = True
        for ap in self.all_points:
            for wap in word_points:
                if wap == ap:
                    ok = False

        if ok:
            for aok in word_points:
                self.all_points.append(aok)
        return ok
