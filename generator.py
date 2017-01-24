"""
CSV data generator
"""

import os
import sys
import numpy as np
import argparse

arguments = argparse.ArgumentParser()
arguments.add_argument('--dim', type=int, default=3)
arguments.add_argument('--num', type=int, default=100)
arguments.add_argument('--cluster', type=int, default=3)
args = vars(arguments.parse_args(sys.argv[1:]))

def generate(out_path):

  nclusters = args['cluster']
  dim = args['dim']

  # Generate centroids
  centroids = [np.random.normal(0,5,dim) for i in range(nclusters)]

  with open(out_path, 'w+') as f:
    for i in range(args['num']):
      c = np.random.choice(range(nclusters))
      v = centroids[c] + np.random.normal(0,0.25,dim)
      f.write(','.join(map(str,v.tolist())))
      f.write('\n')


if __name__ == '__main__':
  out_path = 'data.csv'
  generate(out_path)
