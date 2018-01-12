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
# copy_exif_data = False

jpg_options = {'quality': 75,
               'optimize': True,
               'progressive': True}

thumb_size = (280, 210)
# Attribute of Album objects which is used to sort medias (eg 'title'). To sort
# on a metadata key, use 'meta.key'.
# albums_sort_attr = 'name'

# Reverse sort for albums
# albums_sort_reverse = False

# Attribute of Media objects which is used to sort medias. 'date' can be used
# to sort with EXIF dates, and 'meta.key' to sort on a metadata key (which then
# must exist for all images).
# medias_sort_attr = 'filename'

# Reverse sort for medias
# medias_sort_reverse = False

ignore_directories = []
ignore_files = []

use_assets_cdn = False

# A list of links (tuples (title, URL))
# links = [('Example link', 'http://example.org'),
#          ('Another link', 'http://example.org')]

# List of files to copy from the source directory to the destination.
# A symbolic link is used if ``orig_link`` is set to True (see above).
# files_to_copy = (('extra/robots.txt', 'robots.txt'),
#                  ('extra/favicon.ico', 'favicon.ico'),)

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

# Adjust the image after resizing it. A default value of 1.0 leaves the images
# untouched.
# adjust_options = {'color': 1.0,
#                   'brightness': 1.0,
#                   'contrast': 1.0,
#                   'sharpness': 1.0}

