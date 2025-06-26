# functions/get_files_info.py

import os

def get_files_info(working_directory, directory=None):
    """
    Get a formatted string listing files and directories in the specified path.
    
    Always returns a string: either formatted directory contents or an error message.

    Parameters:
    - working_directory (str): The base directory to operate in.
    - directory (str, optional): A subdirectory within the working directory to inspect.

    Returns:
    - str: A formatted list of contents or an error message.
    """
    # Resolve absolute paths
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.join(working_directory, directory) if directory else working_directory
    target_directory = os.path.abspath(target_directory)

    # Ensure the target_directory is within working_directory
    if not target_directory.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Ensure target_directory is an actual directory
    if not os.path.isdir(target_directory):
        return f'Error: "{directory}" is not a directory'

    # Build result string
    lines = []
    try:
        with os.scandir(target_directory) as entries:
            for entry in entries:
                try:
                    size = entry.stat().st_size
                    is_dir = entry.is_dir()
                    lines.append(f'- {entry.name}: file_size={size} bytes, is_dir={is_dir}')
                except OSError as e:
                    lines.append(f'- {entry.name}: error reading info: {e}')
    except OSError as e:
        return f'Error: Failed to read directory "{directory}": {e}'

    return '\n'.join(sorted(lines))
