flirt -in /mnt/c/Users/JimiH/IRON\ HACK/WEEK\ 8/FINAL\ PROJECT/IRON\ HACK\ PROJECT\ MRI/TRAINING\ DATA/skull_strip/stripped/znorm_flirt_only/on_ds004837/control/sub-2387A_ses-0001_T1w_stripped_znorm.nii.gz \
      -ref $FSLDIR/data/standard/MNI152_T1_1mm_brain.nii.gz \
      -out /mnt/c/Users/JimiH/IRON\ HACK/WEEK\ 8/FINAL\ PROJECT/IRON\ HACK\ PROJECT\ MRI/TRAINING\ DATA/skull_strip/stripped/znorm_flirt_only/on_ds004837/control/sub-2387A_ses-0001_T1w_stripped_znorm_realigned.nii.gz \
      -omat /mnt/c/Users/JimiH/IRON\ HACK/WEEK\ 8/FINAL\ PROJECT/IRON\ HACK\ PROJECT\ MRI/TRAINING\ DATA/skull_strip/stripped/znorm_flirt_only/on_ds004837/control/sub-2387A_ses-0001_T1w_stripped_znorm_realigned_affine.mat \
      -dof 12 \
      -cost mutualinfo \
      -searchrx -30 30 -searchry -30 30 -searchrz -30 30 \
      -v

