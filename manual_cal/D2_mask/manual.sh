#!/bin/bash

#SBATCH --job-name=manual_res  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

#run the script
python rabi_amplitude.py
