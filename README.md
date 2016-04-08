Dynamic CLI
-----------

Drop small files into the `commands` directory, then be able to execute them without issues.

Example
-------

The simplest example


```
# ./commands/dansysadm_ping.py
@click.command()
def main(name):
    """ Check if the url is up"""
    r = requests.get('http://dansysadm.com').status_code
    print "{url}, {r}".format(**locals())
```

```
$ ./main.py ping
dansysadm.com, 200
```





