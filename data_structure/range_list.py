"""
data_structure.range_list
This file implements the range list data structure.

"""

from typing import List
from typing import Tuple

Range = Tuple[int, int]  # an alias for readability


class RangeList:
    """
    A pair of integers define a range, for example: [1, 5). This range includes integers: 1, 2, 3, and 4.
    A range list is an aggregate of these ranges: [1, 5), [10, 11), [100, 201)
    """

    def __init__(self, ranges: List[Range] = None):
        """
        @param ranges List[Tuple[int, int]], the initial range pairs of this range list
        """
        ranges = ranges or []
        for range_ in ranges:
            assert (len(range_) == 2) and (range_[1] - range_[0] >= 1)
        self._ranges: List[Range] = ranges  # all range pairs of this range list

    def add(self, range_: Range):
        """
        Adds a range to the list
        @param range_ Tuple[int, int], tuple of two integers that specify beginning and end of a range.
        """
        assert (len(range_) == 2) and (range_[1] - range_[0] >= 1)

        # 1. the range list is empty, just add the first range pairs and return
        if not self._ranges:
            self._ranges = [range_]
            return

        # 2. the range list is not empty, iterate all range pairs to extend old range or insert new range
        new_ranges = []
        add_beg, add_end = range_  # the range to add

        for (beg, end) in self._ranges:
            # 2.1 the adding range is already handled
            if add_beg is None and add_end is None:
                # save current range directly
                new_ranges.append((beg, end))
                continue

            # 2.2 the adding range includes current range
            if add_beg <= beg and add_end >= end:
                # ignore current range
                continue

            # 2.3 the adding range is on the left side of current range
            if add_end <= beg:
                if add_end < beg:  # any gap between two ranges
                    # save the adding range first, then save current range
                    new_ranges.append((add_beg, add_end))
                    new_ranges.append((beg, end))
                else:  # no gap between two ranges
                    # save the merged two ranges
                    new_ranges.append((add_beg, end))

                # mark adding range as handled
                add_beg, add_end = None, None
                continue

            # 2.4 the adding range is on the right side of current range
            if add_beg >= end:
                if add_beg > end:  # any gap between two ranges
                    # save current range pair directly
                    new_ranges.append((beg, end))
                else:  # no gap between two ranges
                    # extend the adding beg
                    add_beg = beg
                continue

            # 2.5 the adding range is within current range
            if add_beg >= beg and add_end <= end:
                # save current range, ignore the adding range
                new_ranges.append((beg, end))

                # mark the adding range as handled
                add_beg, add_end = None, None
                continue

            # 2.6 the adding range is overlapping the left side of current range pair
            if add_beg < beg and add_end < end:
                # extend the end of the adding range
                add_end = end
                continue

            # 2.7 the adding range is overlapping the right side of current range pair
            if add_beg > beg and add_end > end:
                # extend the beginning of the adding range
                add_beg = beg
                continue

        if add_beg is not None and add_end is not None:
            new_ranges.append((add_beg, add_end))

        self._ranges = new_ranges

    def remove(self, range_: Range):
        """
        Removes a range from the list
        @param range_ Tuple[int, int], tuple of two integers that specify beginning and end of a range.
        """
        assert (len(range_) == 2) and (range_[1] - range_[0] >= 1)

        # 1. the range list is empty, return immediately
        if not self._ranges:
            return

        # 2. the range list is not empty, iterate all range pairs to shrink old range
        new_ranges = []
        rm_beg, rm_end = range_  # the range to remove

        for (beg, end) in self._ranges:
            # 2.1 the removing range is already handled
            if rm_beg is None and rm_end is None:
                # save current range directly
                new_ranges.append((beg, end))
                continue

            # 2.2 current range is within removing range
            if beg >= rm_beg and end <= rm_end:
                # skip current range, it is removed
                continue

            # 2.3 current range is on the left side of removing range
            if end <= rm_beg:
                # save current range
                new_ranges.append((beg, end))
                continue

            # 2.4 current range is on the right side of removing range
            if beg >= rm_end:
                # save current range and mark removing range as handled
                new_ranges.append((beg, end))
                rm_beg, rm_end = None, None
                continue

            # 2.5 current range includes removing range, the removing range divide current range into two parts
            if beg <= rm_beg and end >= rm_end:
                # save the left part
                left_beg = beg + 1 if beg == rm_beg else beg
                left_end = rm_beg
                if left_end - left_beg >= 1:
                    new_ranges.append((left_beg, left_end))

                # save the right part
                right_beg = rm_end
                right_end = end
                if right_end - right_beg >= 1:
                    new_ranges.append((right_beg, right_end))

                continue

            # 2.6 current range is overlapping the left side of removing range
            if beg < rm_beg and end < rm_end:
                # current end is moved to rm_beg
                new_ranges.append((beg, rm_beg))
                continue

            # 2.7 current range is overlapping the right side if removing range
            if beg > rm_beg and end > rm_end:
                # current beg is moved to rm_end
                new_ranges.append((rm_end, end))
                continue

        self._ranges = new_ranges

    def print(self):
        """
        Prints out the list of ranges in the range list
        """
        print(self)

    def __str__(self):
        """
        Return the string representation of this range list
        """

        out = ""
        for range_ in self._ranges:
            pair = f"[{range_[0]}, {range_[1]}) "
            out += pair
        return out.strip()


