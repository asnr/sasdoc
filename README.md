SAS Documentation Tool
======================

The goal is to start with a folder containing SAS macros (potentially within subfolders) and create a web site from which you can view and search for macros by the macro title or keywords in comments just above the macro definition in the `*.sas` source files.

There are 3 steps to go from a folder of source files to a web site:

1.  `sas2rst.py`, a program written in Python (specifically version 3.4, but can be modified to be valid Python 2.6, 2.7 or 3.3) reads all of the `*.sas` files, extracts the comments and other useful information (like macro names and file paths) and stores it in corresponding `*.rst` files in another folder. For example, if the original SAS source code folder looks like this:

        SASLibrary/
        ├── inner_SASLibrary/
        │   └── inner_macro.sas
        └── outer_macro.sas

    and the output folder is specified as `~/sas_documentation/reST_files` then after running `sas2rst.py`, the `reST_files` folder will look like this:

        reST_files/
        ├── inner_SASLibrary/
        │   └── inner_macro.rst
        ├── index.rst
        └── outer_macro.rst

    In particular, if `out_macro.sas` looks like this:

        /* 
          Calculates the standard deviation of the variable varname in dataset.
        */
        %macro calculate_sd(dataset, varname);
            ...
        %mend;
   
    then `out_macro.rst` will look like this:
   
        calculate_sd
        =======
    
        The SAS source file for this library is here:
    
        ``~/sas_files/SASLibrary/out_macro.sas``
    
        To include this library in your code, use::
    
            %include "~/sas_files/SASLibrary/out_macro.sas";
    
        calculate_sd
        -------
        ::
    
            Calculates the standard deviation of the variable varname in  dataset.

2.  [Sphinx](http://sphinx-doc.org/), a Python library, is then called on the
    folder of `.rst` files, producing a collection of HTML, CSS and JavaScript files that form the website.

3.  A web server serves the website. There are no restrictions on the web
    server that can be used. In particular, because Sphinx produces a
    static site, the web server can be very simple; there is no need for a database or application server. The SimpleHTTPServer which is part of the
    Python standard library is sufficient---on any computer with Python (2 or 3) installed, simply call
    ```shell
    $ python -m SimpleHTTPServer 8000
    ```
    to start serving files relative to the current directory.


Implementation notes
--------------------

*   Ideally, when any `.sas` file changes within the SAS source folder the
    `sas2rst.py` script should be called and the website pages should be updated. Included in the Python files is a Bash script which does that.

*   To run `sas2rst.py` do
    ```shell
    $ ./sas2rst.py SAS_SOURCE_FOLDER RST_OUTPUT_FOLDER
    ```
    Once Sphinx is initialised on `RST_OUTPUT_FOLDER`, just call
    ```shell
    [RST_OUTPUT_FOLDER] $ make html
    ```
    There are equivalent commands for Windows Command Prompt/PowerShell.
