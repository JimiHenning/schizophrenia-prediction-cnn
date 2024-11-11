#!/bin/bash

# Define input and output directories
INPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm/on_ds004873"
OUTPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm/on_ds004873/realigned"
TEMPLATE="$FSLDIR/data/standard/MNI152_T1_1mm_brain.nii.gz"

# Make sure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Define a function for FLIRT processing
flirt_process() {
    local file="$1"
    local filename=$(basename "$file" .nii.gz)
    local flirt_output="${OUTPUT_DIR}/${filename}_flirt.nii.gz"
    local flirt_matrix="${OUTPUT_DIR}/${filename}_affine.mat"

    flirt -in "$file" \
          -ref "$TEMPLATE" \
          -out "$flirt_output" \
          -omat "$flirt_matrix" \
          -dof 12 \
          -cost mutualinfo \
          -searchrx -30 30 -searchry -30 30 -searchrz -30 30 \
          -v

    echo "FLIRT applied on $file -> $flirt_output"
}

# Export the function and variables so that they can be used by parallel
export -f flirt_process
export OUTPUT_DIR TEMPLATE

# Find all .nii.gz files and process them in parallel
find "$INPUT_DIR" -type f -name "*.nii.gz" | parallel flirt_process {}

