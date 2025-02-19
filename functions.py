FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the text file and return the list of
    to-do items.
    """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """ Write the todo item list in a text file. """
    with open('todos.txt','w') as file:
        file.writelines(todos_arg)