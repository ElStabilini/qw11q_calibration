#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q          # Partition name

# Run the qq acquire command

current_time=$(date +"%Y-%m-%d_%H-%M-%S")

qq run /home/users/elisa.stabilini/cal_qw11q/runcard_cal/cryoscope.yaml -o /home/users/elisa.stabilini/cal_qw11q/runcard_cal/cryoscope_tests/B2/cryoscope_${current_time}
