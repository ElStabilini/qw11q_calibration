#!/bin/bash

#SBATCH directives (optional)
#SBATCH --job-name=test  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=dummy            # Partition name

#run the script
python manual_t1.py
