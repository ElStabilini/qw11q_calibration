#!/bin/bash

#SBATCH --job-name=rb_test # Job name
#SBATCH --time=03:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

#run the script
python rb.py
