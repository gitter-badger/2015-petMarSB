#!/usr/bin/env python

from joshua.intervaltree import Interval, IntervalTree
from joshua.intervalforest import IntervalForest
import pandas as pd

import intervaltools as ivt

def test_calc_bases_overlapped():
    iv = Interval(50, 150)
    iv_roverlap = [Interval(100, 200)]
    assert ivt.calc_bases_overlapped(iv, iv_roverlap) == 50

    iv_loverlap = [Interval(0, 100)]
    assert ivt.calc_bases_overlapped(iv, iv_loverlap) == 50

    iv_contained = [Interval(75,125)]
    assert ivt.calc_bases_overlapped(iv, iv_contained) == 50

    iv_contains = [Interval(0, 200)]
    assert ivt.calc_bases_overlapped(iv, iv_contains) == 100

def test_calc_based_overlapped_merged():
    iv = Interval(50, 150)
    iv_overlap = [Interval(50, 200), Interval(0, 100)]
    assert ivt.calc_bases_overlapped(iv, iv_overlap) == 100

    
    

if __name__ == '__main__':
    print 'Running tests...'
    test_calc_bases_overlapped()
