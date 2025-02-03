#!/bin/bash

# SBATCH directives (optional)

#SBATCH --job-name=runcard_test0  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q # Partition name

# Run the qq acquire command
qq acquire /home/users/elisa.stabilini/cal_qw11q/runcard_cal/resonator_spectroscopy_high.yaml -o /home/users/elisa.stabilini
