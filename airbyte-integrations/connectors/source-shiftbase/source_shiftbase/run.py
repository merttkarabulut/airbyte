import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceShiftbase

def run():
    source = SourceShiftbase()
    launch(source, sys.argv[1:])
