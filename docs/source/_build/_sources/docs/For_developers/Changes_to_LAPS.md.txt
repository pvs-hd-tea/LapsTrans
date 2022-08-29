## For Developers
### Changes to LAPS

[ec/dreamcoder/enumeration.py](https://github.com/pvs-hd-tea/LapsTrans/commit/5fde314cc56a11534ac0b7adb542351bfbd96e6e#diff-97475ba5780c9a0810ad3cf4f8799b023dda3e206773cb269c7cd85a50a56156 "ec/dreamcoder/enumeration.py")
psutils.Process.rlimit() call would crash on university HPC

[ec/solvers/geomLib/Renderer.ml](https://github.com/pvs-hd-tea/LapsTrans/commit/5fde314cc56a11534ac0b7adb542351bfbd96e6e#diff-67959a56309aca2ec2eac430fe82a9173d1d72140520f8f56b83f7e80c660eb1 "ec/solvers/geomLib/Renderer.ml")
[ec/solvers/logoLib/VGWrapper.ml](https://github.com/pvs-hd-tea/LapsTrans/commit/5fde314cc56a11534ac0b7adb542351bfbd96e6e#diff-ea68a172928018bafc129ef4679f009b66ce256b77457f1bffc90883f19c1b8d "ec/solvers/logoLib/VGWrapper.ml")
The ocaml solver compilation did not complete without this fix. Ultimately it does not matter -- Cairo is a vector graphics library, and we are not working with those, but this fix was easier than unbundling ocaml make files, and removing components we don't need.

https://github.com/pvs-hd-tea/LapsTrans/commit/242cf14c1ae3d46376018153332d65198970fabe
https://github.com/pvs-hd-tea/LapsTrans/commit/170dc5ec4c2282fba1d357dae16e4d73f2f0b373
https://github.com/pvs-hd-tea/LapsTrans/commit/7a820c57747e493ac08999dc215cf5d89ab3f387
https://github.com/pvs-hd-tea/LapsTrans/commit/f3e07612f5b5ed78e28a39d69acf284edc059cff
[ec/dreamcoder/dreamcoder.py](https://github.com/pvs-hd-tea/LapsTrans/commit/511e0518d3a45aa6568f858202b779674fb4e457#diff-86fa485299dbddcde76b3b4e30cd5e65ff9a5a234c92f0311d021763359a1adc "ec/dreamcoder/dreamcoder.py")
Complete rework of core of list domain processing. We are working with LAPS, and since the list processing was not studied as a part of LAPS paper, scripts for it were not updated since dreamcoder paper.

[ec/dreamcoder/dreamcoder.py](https://github.com/pvs-hd-tea/LapsTrans/commit/bd5b394161b1a45bd4d146a7bb69ca266f890f5c#diff-86fa485299dbddcde76b3b4e30cd5e65ff9a5a234c92f0311d021763359a1adc "ec/dreamcoder/dreamcoder.py")
Custom code tokenizer injected into dreamcoder. The NLTK naturally did not quite cut it for the code processing. A lot of changes have to be made to work with code, e.g. `\n` and `\t` with literals, deconstructing code into tiniest semantic pieces:
`foo[:,3] -> ['[]', 'foo', ':', ',', '3', ']']

[ec/dreamcoder/dreamcoder.py](https://github.com/pvs-hd-tea/LapsTrans/commit/ddb0b6e6771b2f097fdd4537886eb4fbc09ae292#diff-86fa485299dbddcde76b3b4e30cd5e65ff9a5a234c92f0311d021763359a1adc "ec/dreamcoder/dreamcoder.py")
Translation callback. This was needed to extract the LISP results from the live executing dreamcoder, and kill the program after one pass.

### Extra arguments
We added two extra arguments to the list domain of dreamcoder:
- --useCodeTokenizer: Makes LAPS use tokenizer for python source code instead of NLTK for natural languages.
- --translate: Halts LAPS after one pass, and calls translation callback to save the results externally into json, instead of default .pickle file where all of the progress and logs is bundled together.