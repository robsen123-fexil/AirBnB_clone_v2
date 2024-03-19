#!/usr/bin/python3
"""Test modules.
"""
import os
from typing import TextIO


from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears the c

    Args:
        stream (TextIO): The strr.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)





def delete_file(file_path: str):
    """Removes a file if it exists.
    Args:
        file_path file to remove.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)





def reset_store(store: FileStorage, file_path='file.json'):
    """Resets leStorage to reset.
        file_path (str): The path to the store's file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')
    if store is not None:
        store.reload()





def read_text_file(file_name):
    """Re
    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)






def write_text_file(file_name, text):
    """Wri the file to write to.
        text (str): The content of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
