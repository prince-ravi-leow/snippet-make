#!/usr/bin/env python3

import json

def snippet_make(text_file, paste, title, prefix, desc):
	if text_file:
		with open(text_file, "rt") as input_file:
			snippet_body = [line for line in input_file]

	if paste:
		print("Enter/Paste your content, hit RETURN to accept input.\n")
		snippet_body = input()

	snippet_object = {
		"prefix": prefix,
		"body": snippet_body,
		"description": "" if not desc else desc
	}
	
	snippet_json = f'"{title}": ' + json.dumps(snippet_object, indent = 4)

	return snippet_json


if __name__ == "__main__":
	import sys
	from argparse import ArgumentParser

	parser = ArgumentParser(description = "Make VS Code Snippet from text file or clipboard")

	parser.add_argument(
		"--text_file", 
		dest = "text_file", 
		help = "Load code from text file")
	parser.add_argument(
		"--paste", 
		action = "store_true", 
		dest = "paste", 
		help = "Paste code directly into console")
	parser.add_argument(
		"--title", 
		dest = "title", 
		help = "Name of snippet in JSON", 
		required = True)
	parser.add_argument(
		"--prefix", 
		dest = "prefix", 
		help = "Shortcut to call snippet", 
		required = True)
	parser.add_argument(
		"--desc", 
		dest = "desc", 
		type = str, 
		help = "Descriptive description of your snippet (optional)")

	if len(sys.argv) < 2:
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()
	text_file = args.text_file
	paste = args.paste
	title = args.title
	prefix = args.prefix
	desc = args.desc

	if not text_file and not paste:
		print("Please specify text file to load code from (--text_file <path/to/code.txt>), or invoke --paste flag to paste code directly into console")
		sys.exit(1)

	snippet_json = snippet_make(text_file, paste, title, prefix, desc)

	print(f"\n{snippet_json}\n")