import os

def rename_spaces_in_paths(root_dir):
    # First rename directories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            if ' ' in dirname:
                new_dirname = dirname.replace(' ', '')
                old_path = os.path.join(dirpath, dirname)
                new_path = os.path.join(dirpath, new_dirname)
                os.rename(old_path, new_path)
                print(f"Renamed directory: {old_path} -> {new_path}")
    
    # Then rename files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if ' ' in filename:
                new_filename = filename.replace(' ', '')
                old_path = os.path.join(dirpath, filename)
                new_path = os.path.join(dirpath, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed file: {old_path} -> {new_path}")

if __name__ == "__main__":
    current_dir = "/Users/mauricio.drada/code_and_repos/python_and_ableton_resources"
    rename_spaces_in_paths(current_dir)