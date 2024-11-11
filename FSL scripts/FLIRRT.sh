/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm/40013_mprage_stripped_znorm.nii.gz

TEST_OUTPUT_DIR="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm_flirtfnirt/test"
mkdir -p "$TEST_OUTPUT_DIR/flirt_intermediates"

flirt -in "/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm/sample_scan.nii.gz" \
      -ref "$FSLDIR/data/standard/MNI152_T1_1mm_brain.nii.gz" \
      -out "$TEST_OUTPUT_DIR/flirt_intermediates/sample_scan_flirt.nii.gz" \
      -omat "$TEST_OUTPUT_DIR/flirt_intermediates/sample_scan_affine.mat"

echo "FLIRT test complete. Output saved to $TEST_OUTPUT_DIR/flirt_intermediates/"

fnirt --in="/mnt/c/Users/JimiH/IRON HACK/WEEK 8/FINAL PROJECT/IRON HACK PROJECT MRI/TRAINING DATA/skull_strip/stripped/znorm/sample_scan.nii.gz" \
      --aff="$TEST_OUTPUT_DIR/flirt_intermediates/sample_scan_affine.mat" \
      --ref="$FSLDIR/data/standard/MNI152_T1_1mm.nii.gz" \
      --iout="$TEST_OUTPUT_DIR/sample_scan_fnirt.nii.gz" \
      --cout="$TEST_OUTPUT_DIR/flirt_intermediates/sample_scan_warp_coefficients.nii.gz"

echo "FNIRT test complete. Output saved to $TEST_OUTPUT_DIR/"

fsleyes "$FSLDIR/data/standard/MNI152_T1_1mm.nii.gz" "$TEST_OUTPUT_DIR/sample_scan_fnirt.nii.gz"

