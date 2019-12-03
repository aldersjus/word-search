from flask import *
import search.word_diagonal as d
import search.word_horizontal as h
import search.word_vertical as v
import random as r
import re as regex

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/create/')
def create():
    return render_template('create.html')


@app.route('/table/', methods=['GET', 'POST'])
def table():
    # TODO REFACTOR CODE INTO SEPARATE FUNCTIONS, THIS IS TOO MUCH CODE FOR ONE...
    al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

    all_points = []
    grid = []

    word_string = request.args.get('words')
    if len(word_string) > 1:  # use request to get list of words split add to word search

        word_list = regex.split(',|, |\n| ', word_string)
        word_list_checked = []
        for check in word_list:
            if not check.isspace() and len(check) > 2:
                word_list_checked.append(check.strip())

        quarter_point = len(word_list_checked) // 4
        half_point = len(word_list_checked) // 2
        three_quarter_point = quarter_point * 3
        full_point = len(word_list_checked)
        words_horizontal = word_list_checked[0:half_point]
        # TODO THINK ABOUT CHANGING DIAGONAL TO ONLY USE SHORT WORDS AS SOMETIMES A LOT OF RECURSION...
        words_diagonal = word_list_checked[half_point:three_quarter_point]
        words_vertical = word_list_checked[three_quarter_point:full_point]

        length_grid = 0
        for word_size in word_list:
            if len(word_size) > length_grid:
                length_grid = len(word_size)

        length_grid = length_grid + len(word_list)  # make it big enough for words

        # simulate create grid size
        for i in range(length_grid):
            grid.append([])

        # create grid
        for hi in range(len(grid)):
            for i in range(len(grid)):
                grid[hi].append(al[r.randrange(0, 26)])

        ho = h.Horizontal(grid, all_points)
        vo = v.Vertical(grid, all_points)
        do = d.Diagonal(grid, all_points)

        for horizontal in words_horizontal:
            ho.create_word_horizontal(horizontal)

        for vertical in words_vertical:
            vo.create_word_vertical(vertical)

        for diagonal in words_diagonal:
            do.create_word_diagonal(diagonal)

        return render_template('table.html', grid=grid)

    elif len(request.args.get('w')) < 1:
        # TODO deal with errors correctly.
        print("ERROR")


if __name__ == '__main__':
    app.run(debug=True)

