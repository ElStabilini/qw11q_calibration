#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=resonator_punchout  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

#load qibo
#module load qibo

# Run the qq acquire command
qq auto /home/users/elisa.stabilini/cal_qw11q/resonator_punchout.yaml -o /home/users/elisa.stabilini/cal_qw11q/output_D3/resonator_punchout_test
