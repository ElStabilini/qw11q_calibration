#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=022:00:00            # Time limit
#SBATCH --partition=qw11q          # Partition name

# Run the qq acquire command

routine="chevron"
current_time=$(date +"%Y-%m-%d_%H-%M-%S")
folder="0.2"

qq run /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${routine}.yaml -o /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${folder}/fix_dependencies_${routine}_${current_time}
