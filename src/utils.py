import os
import sys
import click


ERRORS = {
    1: "Syntax error in file {0}: {1}\n",
    2: "Unable to detect unused names, 'from {0} import *' used in file {1}.\n"
}


def error(code, str_args):
    assert isinstance(str_args, list)
    click.secho(ERRORS[code].format(*str_args), fg='red', err=True)
    sys.exit()


def get_dot_relpath(basedir, path):
    cutted_path, _ = os.path.splitext(path)
    relpath = os.path.relpath(cutted_path, basedir)
    return relpath.replace('/', '.')


class ParsedItem(str):

    def __new__(cls, path, name, filepath, node, line, module=None):
        item = str.__new__(cls, path)
        item.name = name
        item.filepath = filepath
        item.node = node
        item.line = line
        item.module = module
        return item
