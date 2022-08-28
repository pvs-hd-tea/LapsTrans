### Terminal arguments
Use `--help` with either of two core scripts to get detailed information about cli arguments.
This will also clarify `config.ini` properties, as they completely mimic command line.

### config.ini
For different purposes, translation, evaluations, and different approaches to all of the above, different config files can be written and called on execution with ```<script> <args> config <config path>```. Any extra arguments will override values in config.

Section `[GLOBAL]` will be used by both scripts.
Section `[TRAINING DATA]` will be imported by `generate_training_data.py`.
Section `[TRANSLATE]` will be imported by `translate.py`.
Values in the latter two section will try to override anything stated in `[GLOBAL]`.

**Example file:**
```ini
[GLOBAL]
seed = 1984
min_list_length = 2
max_list_length = 10
examples_per_task = 30
tab_length = 4

[TRAINING DATA]
input_path = lapstrans_extensions/functions.py
output_path = ./data/list
output_name = list_500
data_size = 500

[TRANSLATE]
input_path = lapstrans_extensions/f_file.py
checkpoint_path = smart2.pickle
```