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


@run_solver_test
def test_complex_1():
    board = []
    index = 0
    for x, y, length in [
        (0, 0, 8),
        (9, 0, 6),
        (0, 2, 15),
        (0, 4, 10),
        (11, 4, 4),
        (0, 6, 6),
        (7, 6, 8),
        (0, 8, 8,),
        (9, 8, 6),
        (0, 10, 4),
        (5, 10, 10),
        (0, 12, 15),
        (0, 14, 6),
        (7, 14, 8)]:
        board.append({
            'index': index,
            'direction': 'right',
            'xcoord': x,
            'ycoord': y,
            'length': length,
        })
        index += 1

    for x, y, length in [
        (0, 0, 7),
        (0, 8, 7),
        (2, 0, 5),
        (2, 6, 9),
        (4, 0, 10),
        (4, 11, 4),
        (6, 0, 6),
        (6, 7, 6),
        (8, 2, 6),
        (8, 9, 6),
        (10, 0, 4),
        (10, 5, 10),
        (12, 0, 9),
        (12, 10, 5),
        (14, 0, 7),
        (14, 8, 7)]:
        board.append({
            'index': index,
            'direction': 'down',
            'xcoord': x,
            'ycoord': y,
            'length': length,
        })
        index += 1

    words = {
        'AMEN',
        'APPEAL',
        'BANTAM',
        'BLUSTERY',
        'CASTIGATE',
        'CONJUROR', 
        'CREASED',
        'CRUCIVERBALISTS',
        'DEMAND',
        'DISPLEASES',
        'DOMAIN',
        'EYES',
        'LARGELY',
        'MANNERISM',
        'MIST',
        'NAVIGATE',
        'NEEDLE',
        'NOMADS',
        'PACESETTER', 
        'PENCIL', 
        'PICKSON', 
        'POINTEDOUT', 
        'POSTPONE', 
        'PRICER', 
        'ROSETTE', 
        'RULE', 
        'SAUCE', 
        'SWEATGLAND', 
        'SWIMMINGCOSTUME', 
        'TRUCE'
    }
    result = {
        0: 'POSTPONE', 
        1: 'PRICER', 
        2: 'CRUCIVERBALISTS', 
        3: 'SWEATGLAND', 
        4: 'MIST', 
        5: 'NOMADS', 
        6: 'NAVIGATE', 
        7: 'CONJUROR', 
        8: 'APPEAL', 
        9: 'EYES', 
        10: 'PACESETTER', 
        11: 'SWIMMINGCOSTUME', 
        12: 'DEMAND', 
        13: 'BLUSTERY', 
        14: 'PICKSON', 
        15: 'CREASED', 
        16: 'SAUCE', 
        17: 'MANNERISM', 
        18: 'POINTEDOUT', 
        19: 'AMEN', 
        20: 'NEEDLE', 
        21: 'DOMAIN', 
        22: 'BANTAM', 
        23: 'PENCIL', 
        24: 'RULE', 
        25: 'DISPLEASES', 
        26: 'CASTIGATE', 
        27: 'TRUCE', 
        28: 'ROSETTE', 
        29: 'LARGELY'
    }

    return board, words, result