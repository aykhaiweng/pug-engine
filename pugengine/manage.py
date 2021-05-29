#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def initialize_debugger(debugger="debugpy"):
    """
    Initialize the debugger to use
    """
    debuggers = [
        'debugpy'
    ]
    if debugger in debuggers:
        if debugger == 'debugpy':
            import debugpy
            debugpy.listen(("0.0.0.0", "9999"))
            print("Starting the debugpy for VSCode now, waiting...")
            print("Debugger attached, starting server.Starting the debugpy for VSCode now, waiting...")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # localize the args
    args = sys.argv

    # Pop out the debugger flag if it's available
    for i, arg in enumerate(args):
        if arg.find("--debugger") != -1:
            debugger = args.pop(i)
            initialize_debugger(debugger)

    execute_from_command_line(args)


if __name__ == '__main__':
    main()
