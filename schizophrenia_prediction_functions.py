import os
import shutil
import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt
import seaborn as sns

def recast(df, *column_names):
    for column_name in column_names:
        if column_name in df.columns:

            df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
            df[column_name] = df[column_name].round(0).astype('Int64')
        else:
            raise KeyError(f"Column '{column_name}' not found in the DataFrame")

    return df


###FILE MOVING, DELETING AND RENAMING

def delete_subfolder(directory):
    """
    delete the 'func' subfolder in all subfolders of a given directory
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            func_folder_path = os.path.join(folder_path, "func")

            if os.path.isdir(func_folder_path):
                try:
                    shutil.rmtree(func_folder_path)
                    print (f"Deleted:{func_folder_path}")
                except Exception as e:
                    print(f"Error deleting{func_folder_path}: {e}")



def delete_sub_subfolder(directory):
    """
    delete the 'meg' subfolder in all subfolders of a given directory
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            meg_folder_path = os.path.join(folder_path, r"ses-0001\meg")

            if os.path.isdir(meg_folder_path):
                try:
                    shutil.rmtree(meg_folder_path)
                    print (f"Deleted:{meg_folder_path}")
                except Exception as e:
                    print(f"Error deleting{meg_folder_path}: {e}")


def rename_subfolder(directory):
    """
    renames all subfolders in a given directory
    """
    for folder_name in os.listdir(directory):
        if folder_name.startswith("00"):
            new_name = folder_name[2:]

            old_path = os.path.join(directory, folder_name)
            new_path = os.path.join(directory, new_name)

            os.rename(old_path, new_path)
            print(f"Renamed '{folder_name}' to '{new_name}'")


def delete_sub_subfolder2(directory):
    """
    deletes the 'rest_1' subfolder in all subfolders of a given directory
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            rest_folder_path = os.path.join(folder_path, r"session_1\rest_1")

            if os.path.isdir(rest_folder_path):
                try:
                    shutil.rmtree(rest_folder_path)
                    print (f"Deleted:{rest_folder_path}")
                except Exception as e:
                    print(f"Error deleting{rest_folder_path}: {e}")


def move_file(directory):
    """
    moves files two levels up
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            file_folder_path = os.path.join(folder_path, r"session_1\anat_1")

            if os.path.isdir(file_folder_path):
                current_path = os.path.join(file_folder_path, "mprage.nii.gz")
                new_path = os.path.join(folder_path, "mprage.nii.gz")
                try:
                    shutil.move(current_path, new_path)
                    print (f"Moved:{current_path} to {new_path}")
                except Exception as e:
                    print(f"Error moving{current_path}: {e}")


def delete_subfolder2(directory):
    """
    deletes the 'session_1' subfolder in all subfolders of a given directory
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            ses_folder_path = os.path.join(folder_path, "session_1")

            if os.path.isdir(ses_folder_path):
                try:
                    shutil.rmtree(ses_folder_path)
                    print (f"Deleted:{ses_folder_path}")
                except Exception as e:
                    print(f"Error deleting{ses_folder_path}: {e}")


def rename_files(directory):
    """
    adds the folder name (which corresponds to the patient ID) to the filename of all MRI scans in the given directory
    """
    for folder in os.listdir(directory):
            folder_path = os.path.join(directory, folder)

            if os.path.isdir(folder_path):
                  for file in os.listdir(folder_path):
                        old_path = os.path.join(folder_path, file)

                        if os.path.isfile(old_path):
                              new_name = f"{folder}_{file}"
                              new_path = os.path.join(folder_path, new_name)

                              os.rename(old_path, new_path)
                              print(f"Renamed '{file}' to '{new_name}' in folder '{folder}'")


def move_files_to_parent_directory(directory):
    """
    moves files one level up
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
                for file_name in os.listdir(folder_path):
                    current_path = os.path.join(folder_path, file_name)
                    new_path = os.path.join(directory, file_name)
                try:
                    shutil.move(current_path, new_path)
                    print (f"Moved:{current_path} to {new_path}")
                except Exception as e:
                    print(f"Error moving{current_path}: {e}")


def move_files_to_parent_directory_2lvls(directory):
    """
    moves ALL files in a subfolder two levels up
    """
    for folder in os.listdir(directory):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            file_folder_path = os.path.join(folder_path, "anat")
            if os.path.isdir(file_folder_path):
            # List all files in the folder
                files_to_move = os.listdir(file_folder_path)  # Get a list of files first
                for file_name in files_to_move:
                    current_path = os.path.join(file_folder_path, file_name)
                    new_path = os.path.join(directory, file_name)
                    try:
                        shutil.move(current_path, new_path)
                        print(f"Moved: {current_path} to {new_path}")
                    except Exception as e:
                        print(f"Error moving {current_path}: {e}")



def move_files_from_deepest_subdirectories(directory, target_directory=None):
    """
    moves files from the deepest subfolder into the specified directory
    """
    # Set the target directory to move files to if not specified
    if target_directory is None:
        target_directory = directory
    
    # Loop over each item (file or folder) in the current directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # If it's a directory, check if it's a leaf
        if os.path.isdir(item_path):
            # If the directory has no subdirectories, it's a leaf, so we move files
            if not any(os.path.isdir(os.path.join(item_path, sub)) for sub in os.listdir(item_path)):
                # Move files in the leaf directory
                for file_name in os.listdir(item_path):
                    file_path = os.path.join(item_path, file_name)
                    if os.path.isfile(file_path):  # Only move files, not directories
                        new_path = os.path.join(target_directory, file_name)
                        try:
                            shutil.move(file_path, new_path)
                            print(f"Moved: {file_path} to {new_path}")
                        except Exception as e:
                            print(f"Error moving {file_path}: {e}")
            # If it's not a leaf, go deeper
            else:
                move_files_from_deepest_subdirectories(item_path, target_directory)


def add_stripped_to_filenames(directory):
    for filename in os.listdir(directory):
        # Check if the filename matches the pattern we want to modify
        if "T1w_znorm_flirt" in filename:
            # Construct the new filename by replacing the part we want to change
            new_filename = filename.replace("T1w_znorm_flirt", "T1w_stripped_znorm_flirt")
            old_filepath = os.path.join(directory, filename)
            new_filepath = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_filepath, new_filepath)
            print(f"Renamed: {filename} -> {new_filename}")


def add_stripped_to_filenames_in_df(df, column_name="filename"):
    # Create a copy of the DataFrame
    df_copy = df.copy()
    
    # Modify the specified column in the copied DataFrame
    df_copy[column_name] = df_copy[column_name].apply(
        lambda x: x.replace(".nii.gz", "_stripped_znorm_flirt.nii.gz") if x.endswith(".nii.gz") else x
    )
    return df_copy



## MRI SCAN MANIPULATION AND NORMALIZATION


def reorder_and_flip_axes(image_data, current_order, target_order=(0, 1, 2)):
    """
    Reorder and flip specific slices of an MRI image.
    
    Parameters:
    - image_data (numpy array): The MRI scan data.
    - current_order (tuple): Current order of axes as integers, e.g., (1, 2, 0).
    - target_order (tuple): Desired order of axes. Default is (0, 1, 2) for (sagittal, coronal, axial).
    
    Returns:
    - transformed_data (numpy array): The reordered and flipped image data.
    """
    # Reorder the axes
    transpose_axes = [current_order.index(i) for i in target_order]
    transformed_data = np.transpose(image_data, axes=transpose_axes)
    
    # Flip the transformed data to achieve the correct orientation for each slice type
    # Flip the sagittal slice vertically (Y-axis flip) and the axial slice horizontally (X-axis flip)
    transformed_data = np.flip(transformed_data, axis=1)  # Flip Y-axis (vertical) for sagittal
    transformed_data = np.flip(transformed_data, axis=0)  # Flip X-axis (horizontal) for axial

    return transformed_data


def z_score_normalize(directory):
    """
    use z-score normalization to homogenize brightness intensities for all scans
    """
    print(f"Starting normalization for directory: {directory}")
        
    # Walk through each subdirectory and file in the specified directory
    for root, _, files in os.walk(directory):
        print(f"Processing folder: {root}")
        
        # Create the "znorm" subfolder in the current directory if it doesn't exist
        output_dir = os.path.join(root, "znorm")
        os.makedirs(output_dir, exist_ok=True)
        
        for item in files:
            if item.endswith('.nii') or item.endswith('.nii.gz'):
                item_path = os.path.join(root, item)
                
                # Load and process the image
                try:
                    img = nib.load(item_path)
                    data = img.get_fdata()

                    # Perform Z-score normalization on brain region only
                    brain_data = data[data > 0]  # Assuming non-brain regions are zero
                    mean_intensity = np.mean(brain_data)
                    std_intensity = np.std(brain_data)
                    
                    if std_intensity != 0:  # Avoid division by zero
                        normalized_data = (data - mean_intensity) / std_intensity
                        
                        # Construct output path in the "znorm" folder with "_znorm" suffix
                        filename, ext = os.path.splitext(item)
                        if ext == '.gz':  # Handle .nii.gz extension
                            filename, _ = os.path.splitext(filename)
                            ext = '.nii.gz'
                        else:
                            ext = '.nii'
                        
                        output_path = os.path.join(output_dir, f"{filename}_znorm{ext}")
                        
                        # Save the normalized image in the new location
                        normalized_img = nib.Nifti1Image(normalized_data, img.affine, img.header)
                        nib.save(normalized_img, output_path)
                        print(f"Normalized and saved: {output_path}")
                    else:
                        print(f"Warning: Standard deviation is zero for {item_path}, skipping normalization.")

                except Exception as e:
                    print(f"Error processing file {item_path}: {e}")


def calculate_global_mean_std(directories):
    """Calculate mean and std for the entire dataset across multiple directories."""
    all_values = []
    for directory in directories:
        for file in os.listdir(directory):
            if file.endswith('.nii') or file.endswith('.nii.gz'):
                filepath = os.path.join(directory, file)
                img = nib.load(filepath)
                data = img.get_fdata()
                brain_data = data[data > 0]  # Only non-background values
                all_values.extend(brain_data)  # Accumulate brain voxel intensities

    # Calculate global mean and std
    global_mean = np.mean(all_values)
    global_std = np.std(all_values)
    return global_mean, global_std

def z_score_normalize_global(data, target_mean, target_std):
    """Apply z-score normalization to match target mean and std."""
    brain_data = data[data > 0]  # Only non-background values
    mean = brain_data.mean()
    std = brain_data.std()
    if std != 0:  # Avoid division by zero
        normalized_data = (data - mean) / std * target_std + target_mean
    else:
        normalized_data = data
    return normalized_data

def apply_normalization(directories, target_mean, target_std, output_dir_suffix='_brightness_normalized'):
    """Normalize brightness for all files in the given directories and save to new directories."""
    for directory in directories:
        output_dir = f"{directory}{output_dir_suffix}"
        os.makedirs(output_dir, exist_ok=True)
        
        for file in os.listdir(directory):
            if file.endswith('.nii') or file.endswith('.nii.gz'):
                filepath = os.path.join(directory, file)
                img = nib.load(filepath)
                data = img.get_fdata()

                # Normalize to the target mean and std
                normalized_data = z_score_normalize_global(data, target_mean, target_std)

                # Save the normalized image in the new directory
                output_path = os.path.join(output_dir, file)
                normalized_img = nib.Nifti1Image(normalized_data, img.affine, img.header)
                nib.save(normalized_img, output_path)
                print(f"Saved normalized image to {output_path}")

