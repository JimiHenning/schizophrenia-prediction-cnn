#!/bin/bash

# Set the input and output directories (example paths)
INPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm"
OUTPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm_flirt_only"
TEMPLATE="$FSLDIR/data/standard/MNI152_T1_1mm_brain"  # Skull-stripped MNI template for FLIRT

# Make sure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Define the FLIRT function for parallel execution
flirt_process() {
    file="$1"
    
    # Get the relative path of the file from the INPUT_DIR (including subfolders)
    relative_path="${file#$INPUT_DIR/}"
    subdirectory=$(dirname "$relative_path")
    
    # Create output directory for FLIRT results
    flirt_output_dir="$OUTPUT_DIR/$subdirectory/FLIRT"
    mkdir -p "$flirt_output_dir"
    
    # Get the filename without the directory and extension
    filename=$(basename "$file" .nii.gz)
    
    # Perform linear registration with FLIRT
    flirt_output="${flirt_output_dir}/${filename}_flirt.nii.gz"
    flirt_matrix="${flirt_output_dir}/${filename}_affine.mat"
    
    flirt -in "$file" \
          -ref "${TEMPLATE}.nii.gz" \
          -out "$flirt_output" \
          -omat "$flirt_matrix"
    
    echo "FLIRT applied on $file -> $flirt_output"
}

export -f flirt_process  # Export the function so parallel can access it
export INPUT_DIR OUTPUT_DIR TEMPLATE  # Export variables for use in parallel

# Find all .nii.gz files and process them in parallel
find "$INPUT_DIR" -type f -name "*.nii.gz" | parallel flirt_process

