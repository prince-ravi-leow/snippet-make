# `snippet_make.py`

Easily create VS Code Snippet by copy-pasting into the command line, or loading the desired text from a text file.

See [official docs](https://code.visualstudio.com/docs/editor/userdefinedsnippets), to make your snippet executable.

# Usage
```text
$ python3 snippet_make.py --help
usage: snippet_make.py [-h] [--text_file BODY] [--paste PASTE] --title TITLE --prefix PREFIX [--desc DESC]


options:
  -h, --help        show this help message and exit
  --text_file BODY  Load code stored in text file
  --paste PASTE     Paste code directly into console
  --title TITLE     Name of snippet in JSON
  --prefix PREFIX   Shortcut to call snippet
  --desc DESC       Descriptive description of your snippet (Optional)
```

# Example
**Example snippet:**
```python
#!/usr/bin/env python3
```
**Input:**
```shell
$ python3 snippet_make.py --text_file "test/test_py_shebang.txt" --title "Python shebang" --prefix "pyshebang" 
```
**Output:**
```json
"Python shebang": {
    "prefix": "pyshebang",
    "body": [
        "#!/usr/bin/env python3"
    ],
    "description": ""
}
```
# Acknowledgements
Credit to **[@xiaket](https://stackoverflow.com/users/411662/xiaket) et al.** on this [StackOverflow post](https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-the-user), for implementation of multi-line text input in Python. 🙏
