#!/bin/bash

# SBATCH directives (optional)
#SBATCH --job-name=classification  # Job name
#SBATCH --time=01:00:00            # Time limit
#SBATCH --partition=qw11q            # Partition name

# Run the qq acquire command
qq auto /home/elisa/Desktop/Qibo/Qibocal/cal_qw11q/ramsey_test/resonator_spectroscopy_high.yaml -o /home/elisa/Desktop/Qibo/Qibocal/cal_qw11q/ramsey_test/reportD1/resonator_spectroscopy_high
