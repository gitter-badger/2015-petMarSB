#!/usr/bin/env python

import csv
import sys
import pandas as pd

outfmt6 = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
           'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

def blast_to_df(fn, names=outfmt6, delimiter='\t', index_col=0):
    return pd.read_table(fn, header=None, index_col=index_col, names=names,
                             delimiter=delimiter, skipinitialspace=True,
                             dtype={'qstart': int, 'qend': int, 'sstart': int, 'send': int})

def best_hits(df, comp_col='evalue'):
    assert type(df) is pd.DataFrame
    df['ind'] = df.index
    df.sort(columns=['ind', comp_col], inplace=True)
    df.drop_duplicates(subset='ind', inplace=True)
    del df['ind']

def get_orthologies(A, B, idx, comp_col='evalue'):

    assert type(A) is pd.DataFrame
    assert type(B) is pd.DataFrame
    assert type(idx) is pd.Index

    best_hits(A)
    best_hits(B)

    X = pd.merge(A, B, how='inner', left_on='sseqid', right_index=True)
    X = pd.merge(pd.DataFrame(index=idx),
                      X[(X.index == X.sseqid_y)], left_index=True, right_index=True, how='left')
    del X['sseqid_x']
    del X['sseqid_y']

    return X
