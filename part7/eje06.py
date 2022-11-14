# -*- coding: utf-8 -*-
# Documenta la siguiente función usando docstrings

def max(numbers):
    if len(numbers) == 0:
        return None
    else:
        max = numbers[0]
        for i in numbers:
            if i > max:
                max = i
        return max


def test():
    assert max([1, 2, 3, 4, 5]) == 5, "Should be 5"
    assert type(max.__doc__) == str, "Should be docstrings"
    assert len(str(max.__doc__)) > 14, "Your dockstring is too short"

if __name__ == "__main__":
    test()
    print("Everything passed")