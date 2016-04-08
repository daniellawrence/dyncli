#!/usr/bin/env python
import os
import click
import yaml
from commands import merge

plugin_dir = os.path.join(os.path.dirname(__file__), 'commands')




class MyCLI(click.MultiCommand):

    def __init__(self, name, *args, **kwargs):
        super(MyCLI, self).__init__(*args, **kwargs)
        self.cli_name = name

    def list_commands(self, ctx):
        rv = []
        allowed_commands = self.get_config().get('commands', [])
        for filename in os.listdir(plugin_dir):
            if '__' in filename:
                continue
            if not filename.endswith('.py'):
                continue
            if '_' in filename and not filename.startswith('{0}_'.format(self.cli_name)):
                continue
            if '_' in filename:
                filename = filename.split('_')[-1]
            if filename.startswith('test_'):
                continue
            if filename.startswith('config_'):
                continue
            command = filename[:-3]
            if command not in allowed_commands:
                continue
            rv.append(command)

        rv.sort()
        return set(rv)

    def get_config(self):

        global_yaml = 'configs/global.yaml'
        overrides_yaml = 'configs/{0}.yaml'.format(self.cli_name)

        global_config = {}
        overrides = {}

        if os.path.exists(global_yaml):
            global_config = yaml.load(open(global_yaml))

        if os.path.exists(overrides_yaml):
            overrides = yaml.load(open(overrides_yaml))

        return merge(global_config, overrides)


    def get_command(self, ctx, name, with_cli_name=True):


        if name == '__init__':
            return None

        if with_cli_name:
            name = "{0}_{1}".format(self.cli_name, name)
        module_name = "commands.{1}".format(self.cli_name, name)

        try:
            mod = __import__(module_name, None, None, name)
        except ImportError as error:
            if with_cli_name:
                # If we tried with the name or namespace, and we failed.
                # Try again without the namespace
                name = name.split('_')[-1]
                return self.get_command(ctx, name, with_cli_name=False)

            return None

        ctx._meta = self.get_config()
        command = mod.main
        return command


if __name__ == '__main__':
    import sys
    namespace = sys.argv[0].split('/')[-1]
    cli = MyCLI(namespace)
    cli()
