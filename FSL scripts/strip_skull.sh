#!/bin/bash

# Set the input and output directories (example paths)
INPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/skull_strip/non_stripped"
OUTPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/skull_strip/stripped"

# Make sure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Loop through all .nii.gz files in the input directory
for file in "$INPUT_DIR"/*.nii.gz; do
    # Get the filename without the directory
    filename=$(basename "$file")
    
    # Construct the output file path
    output_file="$OUTPUT_DIR/${filename%.nii.gz}_stripped.nii.gz"

    # Run the BET command
    bet2 "$file" "$output_file" -f 0.3 -g 0

    # Print the status
    echo "Processed $file -> $output_file"
done

