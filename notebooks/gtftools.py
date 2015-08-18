#!/usr/bin/env python

import pandas as pd

def read_gtf(filename):

    # Converter func for the nonstandard attributes column
    def attr_col_func(col):
        d = {}
        for item in col.strip(';').split(';'):
            pair = item.strip().split(' ')
            d[pair[0]] = pair[1].strip('"')
        return d

    def strand_func(col):
        if col =='+':
            return 1
        else:
            return -1

    names=['contig_id', 'source', 'feature', 'start', 'end',
           'score', 'strand', 'frame', 'attributes']

    # Read everything into a DataFrame
    gtf_df = pd.read_table(filename, delimiter='\t', comment='#',
                           header=False, names=names,
                           converters={'attributes': attr_col_func, 'strand': strand_func})
    
    # Generate a new DataFrame from the attributes dicts, and merge it in
    gtf_df = pd.merge(gtf_df,
                      pd.DataFrame(list(gtf_df.attributes)),
                      left_index=True, right_index=True)
    del gtf_df['attributes']
    
    # Switch from [start, end] to [start, end)
    gtf_df.end = gtf_df.end + 1

    return gtf_df
