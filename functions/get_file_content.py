# functions/get_file_content.py

import os

def get_file_content(working_directory, file_path):
    """
    Safely read file contents, enforcing working directory boundaries and truncation for large files.

    Parameters:
    - working_directory (str): The base directory to operate in.
    - file_path (str): The relative or absolute path to the file.

    Returns:
    - str: File contents (possibly truncated), or an error string.
    """
    try:
        working_directory = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not full_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        if len(content) > 10000:
            return content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        return f'Error: {str(e)}'