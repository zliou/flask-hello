

# Learning notes

* `url_for('dir', filename='my_file')` searches for a directory named `dir` and a file named 'my_file' relative to 'dir'.
    * This returns a string that can then be used e.g. in HTML tag parameters like `href`.
* `url_for('route')` will match in the main Flask routing `.py` file by function name, not route name.

