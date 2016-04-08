#!/usr/bin/env python
""" Help message in file
"""
import click
import requests
from utils import get


@click.command()
@click.option('--url', help='url', required=True)
def main(url):
    """ check if a url is up!"""
    r = get.health_check(url)
    print "{url} -- {r}".format(**locals())
