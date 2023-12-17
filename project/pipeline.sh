#!/bin/bash

# Set up the virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r ./requirements.txt

python3 project/pipeline.py