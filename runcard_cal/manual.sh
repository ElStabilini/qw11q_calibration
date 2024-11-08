#!/bin/bash

#SBATCH --job-name=ramsey # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

#run the script
python ramsey.py
