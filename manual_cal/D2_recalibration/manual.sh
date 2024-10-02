#!/bin/bash

#SBATCH --job-name=manual_res  # Job name
#SBATCH --time=00:30:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

#run the script
python qubit_spectroscopy.py
