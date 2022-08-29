
## Code quality
### LoC
| path | files | code | comment | blank | total |
| :--- | ---: | ---: | ---: | ---: | ---: |
| . | 19 | 942 | 158 | 294 | 1,394 |
| laps_augmentations | 2 | 45 | 35 | 13 | 93 |
| pipeline | 1 | 211 | 92 | 39 | 342 |
| tests | 10 | 310 | 1 | 73 | 384 |
| tests/configurations | 4 | 13 | 0 | 2 | 15 |
| tests/helpers | 1 | 2 | 0 | 1 | 3 |
| utils | 1 | 63 | 27 | 13 | 103 |

### Test coverage in ec/lapstrans_extensions
```
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
laps_augmentations/code_tokenizer.py      32      5    84%
pipeline/pipeline.py                     186     29    84%
utils/configuration.py                    46      0   100%
----------------------------------------------------------
TOTAL                                    264     34    87%
```

From this report omitted:
- `laps_augmentations/translation_callback.py`
1 function: 10 LoC
It uses multiple nested dreamcoder classes, and would require unreliable imports to test
- Any and all dreamcoder native code, even modified
- `generate_training_data.py` and `translate.py`, as these are just scripts that bootstrap the functionality implemented in other covered files.
- `functions.py` -- functions written for model training. The errors here will be caught by Pipeline, and if not, will not affect the training, since the code will still correlate to the input-output, even if such behaviour was not expected by the human author.

