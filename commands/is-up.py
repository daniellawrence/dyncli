#!/usr/bin/env python
""" Help message in file
"""
import click
import requests
from utils import get
from . import apply_configs


@click.command()
@click.option('--url', help='url', required=False)
@apply_configs
def main(context, url):
    """ check if any url is up, you must"""
    print "is-up.py: Checking if {url} is up...".format(**locals())
    r = get.health_check(url)
    print "is-up.py: {url} -- {r}".format(**locals())
