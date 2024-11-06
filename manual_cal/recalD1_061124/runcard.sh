#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qubit_spec  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

# Run the qq acquire command
qq auto /home/users/elisa.stabilini/cal_qw11q/manual_cal/recalD1_061124/qubit_spectroscopy.yaml -o /home/users/elisa.stabilini/cal_qw11q/manual_cal/recalD1_061124/qubit_spectroscopy
