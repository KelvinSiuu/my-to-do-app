FILEPATH = "to-do.txt"


def get_todo(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    with open(filepath, "r") as doc:
        todos = doc.readlines()
    return todos


def write_todo(todos, filepath=FILEPATH):
    """ Opens a text file and writes the list of to-do items into the file"""
    with open(filepath, "w") as doc:
        doc.writelines(todos)
