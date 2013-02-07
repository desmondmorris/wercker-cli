import os
import shutil

from clint.textui import puts, colored

from werckercli import prompt
from werckercli.paths import get_global_wercker_path

import json


def validate():
    try:
        with open('wercker.json') as f:
            try:
                json.load(f)
                puts(colored.green("Found a valid wercker.json file"))
            except ValueError:
                puts(colored.red("Not a valid wercker.json file"))
            f.close()
    except IOError as e:
        puts(colored.yellow("Could not find a wercker.json file"))
