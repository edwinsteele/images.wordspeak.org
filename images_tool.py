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


def fix_image_naming():
    """pad image names with leading zeros to allow sigal sorting"""
    pictures_dir = Path(os.path.join(SITE_BASE, "pictures"))
    images = \
        list(pictures_dir.glob("*/*.JPG")) + \
        list(pictures_dir.glob("*/*.jpg"))
    for image in images:
        filename_no_suffix, _, suffix = os.path.basename(image).rpartition(".")
        try:
            if len(filename_no_suffix) < MAX_NUMERIC_STR_LEN:
                # might need to pad
                fns_as_int = int(filename_no_suffix)
                new_path = "%s/%03d.%s" % (os.path.dirname(image),
                                           fns_as_int,
                                           suffix)
                print("Renaming %s to %s" % (image, new_path))
                image.rename(new_path)
        except ValueError:
            print("Unable to parse %s as an int" % (filename_no_suffix,))


@cli.command()
def build():
    """Build the site using sigal"""
    fix_image_naming()
    subprocess.check_call(["sigal", "build"], cwd=SITE_BASE)
    subprocess.check_call(["find", "_build", "-name", "*.css", "-exec",
                           "csso", "-i", "{}", "-o", "{}", ";"],
                          cwd=SITE_BASE)
    subprocess.check_call(["find", "_build", "-name", "*.js", "-exec",
                           "uglifyjs", "{}", "-o", "{}", ";"],
                          cwd=SITE_BASE)
    proc = subprocess.run(["imageOptim", "-d", "_build"],
                          stdout=subprocess.PIPE, cwd=SITE_BASE)
    print(proc.stdout.decode("utf-8"))
    # Add copyright and licence information with exiftool
    # http://photometadata.org/META-Resources-Field-Guide-to-Metadata#Copyright%20Status
    # Copyright Notice
    # Rights Usage Terms


@cli.command()
def sync():
    """Deploy the site"""
    args = [
        "rsync",
        "--ignore-times",
        "--delete",
        "--filter=protect .well-known",
        "-av",
        "--compress",
        "./_build/",
        "images.wordspeak.org:Sites/images.wordspeak.org",
    ]
    subprocess.check_call(args, cwd=SITE_BASE)


if __name__ == "__main__":
    cli()
