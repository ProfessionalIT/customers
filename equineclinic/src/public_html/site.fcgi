#! /usr/bin/env python2.5
import sys
altpath=sys.path
sys.path = ['/home/equine/webapps']
sys.path += altpath

import code
code.webapp.run()
