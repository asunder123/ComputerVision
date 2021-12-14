#!/bin/bash
source  ~/.venvs/chaostk/Scripts/activate
export PYTHONPATH=`pwd`
chaos  --verbose run --dry cvchaos.json
