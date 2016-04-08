#!/usr/bin/env python
""" Help message in file
"""
import click
from utils import get


@click.command()
@click.option('--name', metavar="name", help='The person to greet.', required=True)
@click.pass_context
def main(ctx, name):
    """ Check if the url is up"""
    url = ctx._meta.get('url')
    r = get.health_check(url)
    print "Hello {name} from {url}, {r}".format(**locals())


if __name__ == '__main__':
    main()
