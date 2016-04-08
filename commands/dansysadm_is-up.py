#!/usr/bin/env python
""" Help message in file
"""
import click
from utils import get
from . import apply_configs


@click.command()
@apply_configs
def main(url):
    """ Check if dansysadm.com is up"""
    print "dansysadm_is-up.py: Checking if DANSYSADM.COM is UP!"
    r = get.health_check(url)
    print "dansysadm_is-up.py: DANSYSADM.COM, {r}".format(**locals())


if __name__ == '__main__':
    main()
