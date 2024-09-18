#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=resonator_high_power  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

# Run the qq acquire command
qq auto /home/users/elisa.stabilini/cal_qw11q/qubit_flux_dependence.yaml -o /home/users/elisa.stabilini/cal_qw11q/output_D1/qubit_flux_dependence
