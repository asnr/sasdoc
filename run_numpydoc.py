from numpydoc import NumpyDocString
from sphinxdoc import SphinxDocString

s = """
Processes a dataset and produces CAs.
1. Runs %findmiss(); to eliminate useless fields
2. Splits fields into numeric and character
3. Double Checks character fields to ensure they aren't numeric formatted as text
4. creates formats for all numerics
5. Replaces autoamtic percentile formats with more appropriate formats for age, time, amount type variables
6. Creates CATools compatible CAs ready for import into CATools. 

Parameters
----------
pds
    Name of the dataset to be processed
gb_flag
    Good Bad Flag name
output_path
    Path and name of CAs
trim : {Y, N}, optional
    Option to run findmiss macro or not (default Y). This macro removes all missing and single value fields from a dataset.
create_dev : {number, N}, optional
    Percentage of sample that should make up the development population. 0.7 would create 70% dev, 30% Holdout (default 0.5). If 'N', then will use already existing flag stored in variable dev_flag (1->dev row, 0->holdout row).
var_list : {space-delimited list of strings, N, empty}, optional
    List of variables you want to get CAs for (default N). If empty/N then all variables are processed
client_team : {Y, N}, optional
    Uses the Client Teams CharAnal Macro (default N).

Returns
-------
dataset_small : dataset
    Trimmed dataset
HTML
    CAs in the speified output path

Warns
-----
Macro doesn't work well with single characteristics variables. 
Add a numeric variable to your list if it doesn't work

Examples
--------
%Data2CA(
pds= input_dataset
,gb_flag = cr_gbf
,output_path = D:\CR\Tomek\CA_Prep_test2.html
,trim = Y
,create_dev = 0.7
,var_list = &my_vars.
);
"""

sdoc = SphinxDocString(s)
print(str(sdoc))