#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=sim          # Partition name

#Run the qq acquire command
test.py
