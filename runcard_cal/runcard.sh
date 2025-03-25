#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=qq  # Job name
#SBATCH --time=022:00:00            # Time limit
#SBATCH --partition=qw11q          # Partition name

# Run the qq acquire command

export QIBOLAB_PLATFORMS=~/qibolab_platforms_qrc
source /home/users/elisa.stabilini/calibration/bin/activate

routine="readout_optimization"
current_time=$(date +"%Y-%m-%d_%H-%M-%S")
folder="readout_optimization"

qq run /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${routine}.yaml -o /home/users/elisa.stabilini/cal_qw11q/runcard_cal/${folder}/${routine}_${current_time}_mask_1
