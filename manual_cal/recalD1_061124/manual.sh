#!/bin/bash

#SBATCH --job-name=quibt_cal  # Job name
#SBATCH --time=01:00:00            # Time limit:
#SBATCH --partition=qw11q            # Partition name

#run the script
python qubit_cal.py

