#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

# Run the qq acquire command
qq run /home/users/elisa.stabilini/cal_qw11q/runcard_cal/rabi_amplitude.yaml -o /home/users/elisa.stabilini/cal_qw11q/runcard_cal/rabi_pihalf/rabi_pi02