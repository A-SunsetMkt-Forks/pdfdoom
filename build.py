#!/bin/python

import sys

template_file = open(sys.argv[1], "r")
template_data = template_file.read()
template_file.close()

js_file = open(sys.argv[2], "r")
js_data = js_file.read()
js_file.close()

out_data = template_data.replace("###JS###", js_data)

out_file = open(sys.argv[3], "w")
out_file.write(out_data)
out_file.close()