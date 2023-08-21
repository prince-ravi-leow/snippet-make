#!/usr/bin/env python3

import sys
import json
from argparse import ArgumentParser

### PARSE ARGUMENTS
parser = ArgumentParser(description="Convert text into VS Code Snippet")

parser.add_argument("--text_file", 
                    action="store", 
                    dest="body", 
                    type=str, 
                    help="Load code stored in text file")
parser.add_argument("--paste", 
                    action="store", 
                    dest="paste", 
                    type=bool, 
                    default=False,
                    help="Paste code directly into console (default: False)")
parser.add_argument("--title", 
                    action="store", 
                    dest="title", 
                    type=str, 
                    help="Name of snippet in JSON", 
                    required=True)
parser.add_argument("--prefix", 
                    action="store", 
                    dest="prefix", 
                    type=str, 
                    help="Shortcut to call snippet", 
                    required=True)
parser.add_argument("--desc", 
                    action="store", 
                    dest="desc", 
                    type=str, 
                    help="Descriptive description of your snippet (optional)")

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
paste = args.paste
body = args.body
title = args.title
prefix = args.prefix
desc = args.desc

### MAIN BODY
# Load snippet body from text file
if body:
    snippet_body = []
    with open(body, "rt") as input_file:
    		for line in input_file:
    			snippet_body.append(line)
                    
# Load snippet body from clipboard 
if paste:
    print("Enter/Paste your content, hit RETURN, followed by Ctrl-D (Ctrl-Z on Windows) to accept input.\n")
    snippet_body = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        snippet_body.append(line)

# Construct VS Code Snippet JSON object
if not desc:
    desc = ""

snippet_object = {
    "prefix": prefix,
    "body": snippet_body,
    "description": desc
}
snippet_json = f'"{title}": ' + json.dumps(snippet_object, indent=4)

# Print output to console
print(f"\n{snippet_json}\n")