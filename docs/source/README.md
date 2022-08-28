## Getting started

### How to - Start

#### Option 1
First you will have to solve non-trivial task of deploying LAPS on your machine. For instructions refer to [Deploying LapsTrans to Ubuntu 20](Deploying_LapsTrans_to_Ubuntu_20.md)

#### Option 2
Alternatively, if you have access to the Uni Heidelberg HPC, you can find deployed instance at `/home/container/lapstrans_home/LapsTrans`
Clone it, or use it as is. To source the correct python and opam environments, necessary for running laps execute
```sh
source /home/container/lapstrans_home/env.sourcefile
```

### How to - Translate

To execute the translation script, navigate to the `ec/` directory, type in the terminal
```
python3.7 lapstrans_extensions/translate.py -i <Path to the file containing the function to translate> config lapstrans_extensions/config.ini
```
or 
```
python3.7 lapstrans_extensions/translate.py --cli config lapstrans_extensions/config.ini
```

For interactive input of functions.

The results will be written to `lapstrans_extensions/working_dir/translation.json`, but you could modify that path and more through command line options and/or config.ini file.
For more instructions go to [Configuration](/ec/lapstrans_extensions/docs/Configuration.md)

### How to - Data generation

To execute the training data generation script, navigate to the `ec/` directory, type in the terminal
```
python3.7 lapstrans_extensions/generate_training_data.py -i <Path to the file containing the training functions> config lapstrans_extensions/config.ini
```

This generates both language data for LAPS, as well as solved task examples for the dreamcoder portion of it.

The results will be written to `ec/data/list/<Output name>`, but you could modify that path and more through command line options and/or config.ini file.
For more instructions go to [Configuration](/ec/lapstrans_extensions/docs/Configuration.md)

### Notes

We have built a mechanism to infer the possible input-output types for the given function, differentiating between `List[int]`, `List[bool]`, `bool`, `int`.
Since python is dynamically typed, this might cause unexpected consequences. An obvious illustration is that `+` operand can be used for both list concatenation, addition, and even
```
>>> True+True
2
```
So the function that you have written with a specific purpose in mind, might very well take and return other types flawlessly.

Our code does not differentiate, except **it detects identity mappings**. Moreover in research we discovered that if the function returns `bool` or `List[bool]`, and was detected to be an identity mapping very often this is unexpected behaviour, and thus we treat it as such. Such `bool` interpretation will be ignored.

In other cases, however, all legal type combinations will be processed into training data/ translation examples, and passed onto dreamcoder.

Operations such as sum(l: List) will work both with conventional integer list, and boolean list (effectively counting `True` elements).
