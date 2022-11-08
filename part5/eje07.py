# -*- coding: utf-8 -*-
# Realiza la cata: (https://www.codurance.com/katalyst/simple-mars-rover/)


cols = 10

def get(movs):
    # your code here
    return None


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