from itertools import izip
from functools import partial
from collections import defaultdict

class Place(object):
    def __init__(self, index, direction, xcoord, ycoord, length):
        self._index = index
        self._direction = direction
        self._xcoord = xcoord
        self._ycoord = ycoord
        self._length = length

    @property
    def index(self):
        return self._index

    def __len__(self):
        return self._length

    def itercoords(self):
        if self._direction == "right":
            for i in xrange(self._length):
                yield self._xcoord + i, self._ycoord
        elif self._direction == "down":
            for i in xrange(self._length):
                yield self._xcoord, self._ycoord + i


class Board(object):
    def __init__(self, places):
        self._places = {}
        self._free_places = set()
        self._field = {}

        for place in places:
            self._places[place.index] = place
            self._free_places.add(place.index)
            for x, y in place.itercoords():
                self._field[x, y] = None

        self._sorted_places = sorted(
            self._places.values(), 
            key=lambda place: -len(place)
        )

    def __len__(self):
        return len(self._places)

    def clone(self):
        cloned = type(self)([])
        cloned._places = self._places
        cloned._sorted_places = self._sorted_places
        cloned._field = dict(self._field)
        cloned._free_places = set(self._free_places)
        return cloned

    def iterplaces(self):
        for place in self._sorted_places:
            if place.index in self._free_places:
                yield place.index

    def get_place(self, index):
        return self._places[index]

    def put_word(self, index, word):
        place = self.get_place(index)
        for (x, y), word_letter in izip(place.itercoords(), word):
            self._field[x, y] = word_letter
        self._free_places.discard(index)

    def put_words(self, layout):
        for index, word in layout.iteritems():
            self.put_word(index, word)

    def can_fit_word(self, index, word):
        place = self.get_place(index)
        if index not in self._free_places:
            return False
        if len(word) != len(place):
            return False
        for (x, y), word_letter in izip(place.itercoords(), word):
            letter_on_field = self._field[x, y]
            if letter_on_field is not None and letter_on_field != word_letter:
                return False
        return True

    def print_field(self):
        max_x = 0
        max_y = 0
        for x, y in self._field:
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        for y in xrange(max_y + 1):
            for x in xrange(max_x + 1):
                if (x, y) not in self._field:
                    print ' ',
                else:
                    if self._field[x, y] is None:
                        print '*',
                    else:
                        print self._field[x, y],
            print


class CrosswordsSolver(object):
    def __init__(self, board, words):
        self._places = [Place(**place_data) for place_data in board]
        self._board = Board(self._places)
        self._intersections = self.calc_intersections()
        self._letters_by_position = defaultdict(partial(defaultdict, set))
        self._words = words

        for word in words:
            for position, letter in enumerate(word):
                self._letters_by_position[len(word)][position].add(letter)

    def calc_intersections(self):
        intersections_field = defaultdict(set)
        for place in self._places:
            for position, (x, y) in enumerate(place.itercoords()):
                intersections_field[x, y].add(
                    (place.index, len(place), position)
                )

        intersections = defaultdict(set)
        for place in self._places:
            for position, (x, y) in enumerate(place.itercoords()):
                for index, length, inter_position in intersections_field[x, y]:
                    if index != place.index:
                        intersections[place.index].add(
                            (position, length, inter_position)
                        )
        return intersections

    def is_word_possible(self, index, word):
        for position, length, inter_position in self._intersections[index]:
            word_letter = word[position] 
            possibilities = self._letters_by_position[length][inter_position]
            if word_letter not in possibilities:
                return False
        return True

    def solve(self):
        def _solve(board, words, layout):
            if not words:
                # in case of debugging uncomment this to see solved board
                # board.print_field()
                return layout

            sorted_words = sorted(words, key=lambda word: -len(word))
            for index in board.iterplaces():
                for word in sorted_words:
                    if not board.can_fit_word(index, word):
                        continue

                    if not self.is_word_possible(index, word):
                        continue

                    new_layout = dict(layout)
                    new_layout[index] = word

                    new_board = board.clone()
                    new_board.put_word(index, word)

                    new_words = set(words)
                    new_words.discard(word)

                    result = _solve(new_board, new_words, new_layout)
                    if result:
                        return result
        return _solve(self._board, self._words, {})


def solve(board, words):
    solver = CrosswordsSolver(board, words)
    return solver.solve()


if __name__ == '__main__':
    board = [{
        'index': 0,
        'direction': 'down',
        'xcoord': 0,
        'ycoord': 0,
        'length': 2,
    }, {
        'index': 1,
        'direction': 'right',
        'xcoord': 0,
        'ycoord': 0,
        'length': 2,
    }]
    words = {'ab', 'at'}

    from time import time
    start = time()
    solution = solve(board, words)
    print 'Solution: %s' % solution
    print 'Time: %.03f' % (time() - start)
