from functools import wraps
from crossword import solve

def run_solver_test(func):
    @wraps(func)
    def wrapped(): 
        board, words, result = func()
        assert solve(board, words) == result
    return wrapped


@run_solver_test
def test_simple_1():
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
    result = {0: 'ab', 1: 'at'}

    return board, words, result


@run_solver_test
def test_simple_2():
    board = [{
        'index': 0,
        'direction': 'down',
        'xcoord': 0,
        'ycoord': 0,
        'length': 4,
    }, {
        'index': 1,
        'direction': 'down',
        'xcoord': 2,
        'ycoord': 0,
        'length': 4,
    }, {
        'index': 2,
        'direction': 'right',
        'xcoord': 0,
        'ycoord': 1,
        'length': 4,
    }, {
        'index': 3,
        'direction': 'right',
        'xcoord': 0,
        'ycoord': 3,
        'length': 4,
    }]
    words = {'ccaa', 'baca', 'baaa', 'bbbb'}
    result = {0: 'bbbb', 1: 'ccaa', 2: 'baca', 3: 'baaa'}

    return board, words, result
