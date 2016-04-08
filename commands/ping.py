import click
from utils import get
from . import apply_configs

@click.command()
@click.option('-u', '--url', required=False)
@apply_configs
def main(ctx, url):
    """ ping the remote url """
    r = get.health_check(url)
    print "{url} {r}".format(**locals())


if __name__ == '__main__':
    main()
