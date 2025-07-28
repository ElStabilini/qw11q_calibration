#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=20:00:00            # Time limit
#SBATCH --partition=qw11q # Partition name

# Run the qq acquire command

export QIBOLAB_PLATFORMS=~/qibolab_platforms_qrc
source /home/users/elisa.stabilini/new_env/bin/activate

routine="qubit_spectroscopy"
current_time=$(date +"%Y-%m-%d_%H-%M-%S")
folder="post_fridge_cycle"

qq run /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${routine}.yaml -o /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${folder}/${routine}_${current_time}
