#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=resonator_high_s21  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

# Run the qq acquire command
qq auto /home/users/elisa.stabilini/cal_qw11q/classification.yaml -o /home/users/elisa.stabilini/cal_qw11q/manual_cal/D2_mask/classification_1
