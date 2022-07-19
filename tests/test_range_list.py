"""
tests.data_structure.range_list

This tests the range_list of data_structure module
"""

from data_structure.range_list import RangeList

def _test_add_range():
    """
    Testing code of adding range to RangeList
    """

    # test add simple range
    rl = RangeList()
    rl.add((1, 5))
    rl.add((10, 17))
    rl.add((17, 18))
    assert str(rl) == "[1, 5) [10, 18)"

    # test adding invalid ranges
    try:
        rl.add((4, 4))
    except Exception as err:
        assert isinstance(err, AssertionError)

    # test adding sub range of any existing range
    rl = RangeList([(1, 5), (10, 18)])
    rl.add((2, 4))
    rl.add((12, 16))
    assert str(rl) == "[1, 5) [10, 18)"

    # test adding range overlapping with any existing range
    rl = RangeList([(1, 5), (10, 18)])
    rl.add((-1, 3))
    rl.add((16, 20))
    assert str(rl) == "[-1, 5) [10, 20)"
    rl.add((4, 8))
    assert str(rl) == "[-1, 8) [10, 20)"

    # test adding range not overlapping with any existing range
    rl = RangeList([(-1, 5), (10, 20)])
    rl.add((-19, -16))
    rl.add((-10, -5))
    rl.add((30, 35))
    rl.add((37, 40))
    assert str(rl) == "[-19, -16) [-10, -5) [-1, 5) [10, 20) [30, 35) [37, 40)"

    # test adding range that fill range gap
    rl = RangeList([(-19, -16), (-10, -5), (-1, 5), (10, 20), (30, 35), (37, 40)])
    rl.add((-16, -10))
    rl.add((18, 32))
    assert str(rl) == "[-19, -5) [-1, 5) [10, 35) [37, 40)"

    # test adding range includes any existing range
    rl = RangeList([(-19, -5), (-1, 5), (10, 35), (37, 40)])
    rl.add((-2, 36))
    assert str(rl) == "[-19, -5) [-2, 36) [37, 40)"
    rl.add((-100, 100))
    assert str(rl) == "[-100, 100)"


def _test_remove_range():
    """
    Testing code of remove range from RangeList
    """

    # test remove invalid range
    rl = RangeList()
    try:
        rl.remove((4, 3))
    except Exception as err:
        assert isinstance(err, AssertionError)

    # test remove range overlapping with any existing range
    rl = RangeList([(-100, 100)])
    rl.remove((-120, -80))
    rl.remove((80, 120))
    assert str(rl) == "[-80, 80)"

    # test remove sub range of any existing range
    rl = RangeList([(-80, 80)])
    rl.remove((-70, -60))
    rl.remove((60, 70))
    assert str(rl) == "[-80, -70) [-60, 60) [70, 80)"

    # test remove range not overlapping with any existing range
    rl = RangeList([(-80, -70), (-60, 60), (70, 80)])
    rl.remove((-70, -65))
    rl.remove((65, 70))
    assert str(rl) == "[-80, -70) [-60, 60) [70, 80)"

    # test remove range includes any existing range
    rl = RangeList([(-80, -70), (-60, 60), (70, 80)])
    rl.remove((-90, 65))
    assert str(rl) == "[70, 80)"


def test():
    """
    testing code of RangeList
    """
    _test_add_range()
    _test_remove_range()
    print("all tests passed!")


if __name__ == "__main__":
    test()
