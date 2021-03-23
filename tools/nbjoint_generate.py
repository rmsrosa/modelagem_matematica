# Generate the navigable book-like structure"

import os
import nbjoint as nbj

os.chdir(os.path.dirname(os.path.abspath(__file__)))

nbj.joint('nbjoint_config.yml')
