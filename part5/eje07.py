# -*- coding: utf-8 -*-
# Realiza la cata: (https://www.codurance.com/katalyst/simple-mars-rover/)


cols = 10

def get(movs): 
    pos=['N','E','S','W'] 
    dir = 'N' 
    x = 0 
    y = 0 
    for m in movs: 
        if m == 'M' and dir == 'N': y = (y + 1) % cols 
        if m == 'M' and dir == 'S': y = (y - 1) % cols 
        if m == 'M' and dir == 'E': x = (x + 1) % cols 
        if m == 'M' and dir == 'W': x = (x - 1) % cols 
        elif m == 'R': 
            dir = pos[(pos.index(dir) + 1) % 4] 
            # if dir == 'N': dir = 'E' 
            # elif dir == 'S': dir = 'W' 
            # elif dir == 'E': dir = 'S'
            # elif dir == 'W': dir = 'N'
        elif m == 'L': 
            dir = pos[(pos.index(dir) - 1) % 4] 
            # if dir == 'N':dir = 'W' 
            # elif dir == 'S':dir = 'E' 
            # elif dir == 'E':dir = 'N' 
            # elif dir == 'W':dir = 'S' 
    return (x, y, dir)

def test():
    assert get("M") == (0, 1, 'N'), "M"
    assert get("MMMMMMMMMM") == (0, 0, 'N'), "MMMMMMMMMM"
    assert get("RMM") == (2, 0, 'E'), "RMM"
    assert get("RMMMMMMMMMM") == (0, 0, 'E'), "RMMM"
    assert get("MMRMMLM") == (2, 3, 'N'), "MMRMMLM"
    assert get("LM") == (9, 0, 'W'), "MMRMMLM"
    assert get("LLM") == (0, 9, 'S'), "MMRMMLM"
    pass

if __name__ == "__main__":
    test()
    print("Everything passed")