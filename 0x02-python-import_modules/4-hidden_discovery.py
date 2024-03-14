#!/usr/bin/python3

if __name__ == "__main__":
    """ prints all the names defined by the complied module hidden_4.pyc """

    import hidden_4

    names = [name for name in dir(hidden_4) if not name.startswith("__")]
    print("\n".join(names))
