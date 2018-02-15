# -*- coding: utf-8 -*-

title = "Edwin's photos"
source = 'pictures'
theme = 'galleria'
author = 'Edwin Steele'

# ----------------
# Image processing (ignored if use_orig = True)
# ----------------

img_size = (1600, 1200)
show_map = True

# If True, EXIF data from the original image is copied to the resized image
copy_exif_data = False

jpg_options = {'quality': 75,
               'optimize': True,
               'progressive': True}

thumb_size = (280, 210)
ignore_directories = []
ignore_files = []

use_assets_cdn = False

links = [('Wordspeak', 'https://www.wordspeak.org'),]
files_to_copy = (('extra/favicon.ico', 'favicon.ico'),
                ('extra/robots.txt', 'robots.txt'))

# --------
# Plugins
# --------

# List of plugins to use. The values must be a path than can be imported.
# Another option is to import the plugin and put the module in the list, but
# this will break with the multiprocessing feature (the settings dict obtained
# from this file must be serializable).
# plugins = ['sigal.plugins.adjust', 'sigal.plugins.copyright',
#            'sigal.plugins.upload_s3', 'sigal.plugins.media_page']

# Add a copyright text on the image (default: '')
# copyright = "© An example copyright message"
