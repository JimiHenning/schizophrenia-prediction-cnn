#!/bin/bash

# Set the input and output directories (example paths)
INPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/non_stripped/on_ds004873/control"
OUTPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/on_ds004873/control"

# Make sure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop through all .nii.gz files in the input directory, including all subfolder levels
find "$INPUT_DIR" -type f -name "*.nii.gz" | while read -r file; do
    # Get the relative path of the file from the INPUT_DIR (including subfolders)
    relative_path="${file#$INPUT_DIR/}"
    
    # Extract the directory structure from the relative path
    subdirectory=$(dirname "$relative_path")
    
    # Create the corresponding subdirectory structure in the OUTPUT_DIR
    output_subdir="$OUTPUT_DIR/$subdirectory"
    mkdir -p "$output_subdir"
    
    # Get the filename without the directory
    filename=$(basename "$file")
    
    # Construct the output file path
    output_file="$output_subdir/${filename%.nii.gz}_stripped.nii.gz"
    
    # Run the BET command
    bet2 "$file" "$output_file" -f 0.5 -g 0
    
    # Print the status
    echo "Processed $file -> $output_file"
done
