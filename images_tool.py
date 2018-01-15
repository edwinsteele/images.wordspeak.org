#!/usr/bin/env python3
"""build helper"""

from pathlib import Path
import os
import subprocess
import click

MAX_NUMERIC_STR_LEN = 3
SITE_BASE = os.path.dirname(__file__)


@click.group()
def cli():
    click.echo("Starting wordspeak tool")


@cli.command()
def fix_image_naming():
    """pad image names with leading zeros to allow sigal sorting"""
    pictures_dir = Path(os.path.join(SITE_BASE, "pictures"))
    images = \
        list(pictures_dir.glob("*/*.JPG")) + \
        list(pictures_dir.glob("*/*.jpg"))
    for image in images:
        filename_no_suffix, _, suffix = os.path.basename(image).rpartition(".")
        try:
            if len(filename_no_suffix) <= MAX_NUMERIC_STR_LEN:
                # might need to pad
                fns_as_int = int(filename_no_suffix)
                new_path = "%s/%03d.%s" % (os.path.dirname(image),
                                           fns_as_int,
                                           suffix)
                image.rename(new_path)
        except ValueError:
            print("Unable to parse %s as an int" % (filename_no_suffix,))


@cli.command()
def build():
    """Build the site using nikola"""
    subprocess.check_call(["nikola", "build"], cwd=SITE_BASE)


@cli.command()
def sync():
    """Deploy the site"""
    args = [
        "rsync",
        "--ignore-times",
        "--delete",
        "-av",
        "./_build/",
        "gemini.wordspeak.org:Sites/images.wordspeak.org",
    ]
    subprocess.check_call(args, cwd=SITE_BASE)


if __name__ == "__main__":
    cli()
