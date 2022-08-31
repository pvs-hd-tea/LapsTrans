## Evaluation
We did not design a proper evaluation strategy, but here is some tests that demonstrate general trends.

Here we demonstrate translation results with our best model.
**Model training parameters:**
- enumerationTimeout 180
- 18 iterations
- taskBatchSize 40
- recognitionTimeout 180
- Helmholtz 0.5

Task dataset generated from the latest lapstrans_extensions/functions.py

-----------------

#### Functions present in training dataset

Each translation attempt is given 30 seconds
**Set**
```
def delete_first(inp):
    return inp[1:]

def replace_all_with_sum(inp):
    s = sum(inp)
    return [s for _ in inp]

def s(inp):
    return sorted(inp)

def contains_2(inp):
    return 2 in inp
```
**Results**

```
HIT contains_200 w/ (lambda (#(lambda (#(lambda (gt? (#(lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) (map (lambda (is-prime (- $0 (if (is-prime $0) 1 $0)))) $0))) $0) 0)) (#(lambda (map (lambda (+ $0 $1)))) 1 $0))) $0)) ; log prior = -4.680944 ; log likelihood = 0.000000
HIT contains_201 w/ (lambda #(is-prime 1)) ; log prior = -2.427001 ; log likelihood = 0.000000
HIT delete_first00 w/ (lambda (cdr $0)) ; log prior = -5.769636 ; log likelihood = 0.000000
HIT delete_first01 w/ (lambda (cdr $0)) ; log prior = -4.193634 ; log likelihood = 0.000000
HIT replace_all_with_sum00 w/ (lambda (#(lambda (map (lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 $1))))) $1)) $0)) $0)) ; log prior = -5.498956 ; log likelihood = 0.000000
HIT replace_all_with_sum01 w/ (lambda (#(lambda (map (lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) $1)) $0)) $0)) ; log prior = -4.484340 ; log likelihood = 0.000000
MISS s00
MISS s01
Hits 6/8 tasks
```

First of all, complex tasks, such as sort, already prove problematic for our model. This must be underperformance on our part, since originally dreamcoder should learn sort - and quickly - at that.

#### Functions merged from two in the training dataset

**Set**
```
def replace_max_with_sum(inp):
    s = sum(inp)
    return [s if x == max(inp) else x for x in inp]

def if_contains_2_floor(inp):
    if 2 in inp:
        return [min(inp) for _ in inp]
    return inp

def n_ns(inp):
    return [inp for _ in range(inp)]

def if_min_is_0(inp):
    return min(inp) == 0
```
**Results**
```
MISS if_contains_2_floor00
HIT if_min_is_000 w/ (lambda #(is-prime 1)) ; log prior = -2.427001 ; log likelihood = 0.000000
HIT if_min_is_001 w/ (lambda (#(lambda (gt? 1 (#(lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) (cons (eq? (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) $0) (length $0)) empty))) $0))) $0)) ; log prior = -3.810497 ; log likelihood = 0.000000
HIT n_ns00 w/ (lambda (map (lambda $1) (range $0))) ; log prior = -12.339244 ; log likelihood = 0.000000
HIT n_ns01 w/ (lambda (cdr (map (lambda $1) (#(lambda (cdr (range (+ 1 (#(lambda (lambda (+ (length (range (- $0 $1))) $1))) 1 (#(lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) (cons $0 (cons $0 empty)))) $0)))))) $0)))) ; log prior = -13.799737 ; log likelihood = 0.000000
MISS replace_max_with_sum00
MISS replace_max_with_sum01
Hits 4/7 tasks
```
We know for a fact, that all of the functions used in this set were originally solved. Evidentally our model struggles to quickly enough find solution when presented with something slightly different from something it has not seen.

#### Functions merged from three in the training dataset

**Set**
```
def delete_first_append_max_zero_min(inp):
    q = inp[1:]
    q = q + [max(q)]
    q = [0 if x == min(q) else x for x in q]
    return q

def range_max_if_first_is_min(inp):
    if inp[0] == min(inp):
        return list(range(max(inp)))
    return inp

def floor_if_contains_2_else_ceil(inp):
    if 2 in inp:
        return [min(inp) for _ in inp]
    else:
        return [max(inp) for _ in inp]

def reverse_negative_range(inp):
    return [-i for i in range(inp-1, -1, -1)]

```
**Results**
```
MISS delete_first_append_max_zero_min00
MISS delete_first_append_max_zero_min01
MISS floor_if_contains_2_else_ceil00
HIT floor_if_contains_2_else_ceil01 w/ (lambda (#(lambda (map (lambda (#(lambda (gt? (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) $0) 0)) $1)) $0)) $0)) ; log prior = -3.496621 ; log likelihood = 0.000000
MISS range_max_if_first_is_min00
MISS range_max_if_first_is_min01
HIT reverse_negative_range00 w/ (lambda (#(lambda (lambda (map (lambda (- $0 ($1 $2))) $1))) (#(lambda (#(lambda (map (lambda (+ $0 $1)))) (#(lambda (#(lambda (fold $0 0 (lambda (lambda (+ $0 (if $1 1 0)))))) (map (lambda (eq? $0 0)) $0))) $0) $0)) (range $0)) (lambda $1))) ; log prior = -14.897331 ; log likelihood = 0.000000
HIT reverse_negative_range01 w/ (lambda (range (#(lambda (lambda (if $1 (+ $0 1) $0))) $0 0))) ; log prior = -11.735437 ; log likelihood = 0.000000
Hits 3/8 tasks
```

And again, more complexity introduces more struggles.
Notice that functions with names ending in `1` are generally `bool` or `List[bool]` operations, and naturally our model performs better due to smaller domain.