# images.wordspeak.org
Wordspeak images

# Setup

make virtualenv
pip install -r requirements.txt
brew cask install imageoptim
npm install -g csso-cli
npm install uglify-js -g
npm install -g imageoptim-cli

ImageOptim settings:
* General:
  * enable all but pngcrush, guetzli and svgo
  * strip PNG metadata but not JPEG metadata
  * Preserve file perms, attributes and hard links
* Enable lossy minification
* JPEG @66%
* PNG @80%
* GIF @80%
* Optimization level: insane

# Run

./images_tool.py build
./images_tool.py sync
