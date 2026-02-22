#!/bin/bash

# Find python3
PYTHON=$(which python3)

if [ -z "$PYTHON" ]; then
    echo "Python 3 is not installed. Please install Python to run NEXA."
    exit 1
fi

# Run NEXA
$PYTHON nexa.py