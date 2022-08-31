## Preparations:
Get the ec repo, and don't forget to checkout into correct branch:
```
git clone https://github.com/ellisk42/ec
cd ec
git checkout icml_2021_supplement
```

Install all the deps you will need:
```
sudo apt-get update
sudo apt-get install build-essential git-core pkg-config automake libtool libcairo2-dev libzmq3-dev pkg-config wget zlib1g-dev python-dev libbz2-dev graphviz libffi-dev software-properties-common swig ocaml opam
```

## Python
LAPS is written with python 3.7.7
Ubuntu 20 comes preinstalled with python 3.8 as default, and it is aliased as ```python```. Unless you want to reconfigure your python environment, it's advised to use ```python3.7``` explicitly. This also means running ```python3.7 -m pip ...``` instead of ```pip ...```.

```
sudo apt-get update; 
sudo add-apt-repository ppa:deadsnakes/ppa; sudo apt-get update; 
sudo apt-get install python3.7; sudo apt install python3.7-dev; 
sudo apt install python3-pip; python3.7 -m pip install pip;
python3.7 -m pip install --upgrade setuptools;
```

Now the python package requirements. Unfortunately they are scattered across three files. Not sure which ones are tautological, but just to be safe:
```
python3.7 -m pip install -r requirements.txt
python3.7 -m pip install -r language_requirements.txt
python3.7 -m pip install -r language_requirements_3_7_7.txt
```

There are also few they forgot to add:
```
python3.7 -m pip install num2words graphviz
```

NLTK tokenizer:
```
python3.7
import nltk; nltk.download('punkt')
exit()
```

## Moses

### Boost
You have to build Moses yourself, and for that you have to build its dependency - boost - also yourself (there are compiled boost libs in the Ubuntu repos, but Moses refuses to compile with them).
```
wget http://downloads.sourceforge.net/project/boost/boost/1.60.0/boost_1_60_0.tar.gz
tar zxvf boost_1_60_0.tar.gz
cd boost_1_60_0/
./bootstrap.sh
./b2 -j4 --prefix=$PWD --libdir=$PWD/lib64 --layout=system link=static install
```
This puts compiled libraries into the current - ```boost_1_60_0``` - directory.

### Actually Moses
```
git clone https://github.com/moses-smt/mosesdecoder.git
cd mosesdecoder
./bjam --with-boost=<FULL path to the folder boost_1_60_0> -j4
```
Move the ```mosesdecoder``` directoty into ec/ and rename it as ```moses_compiled```.

## Opam environment

It will ask you to add command to initialize opam into bash_profile, agree, but it might not always work, especially for non-orthodox shells, like zsh. You might need to add
```
eval `opam config env`
```
there manually, or just run it every time.
```
opam init
opam update
opam switch create 4.06.1+flambda
```
```
eval `opam config env`
opam depext ppx_jane core re2 yojson vg cairo2 camlimages menhir.20211128 ocaml-protoc zmq
opam install ppx_jane core re2 yojson vg cairo2 camlimages menhir.20211128 ocaml-protoc zmq
```
## Ocaml solvers compilation

Now make sure you are in ```ec``` directory, and build ocaml code.
```make clean; make```

# Running LAPS:

The datasets that come with the repo are not good, you need to get the actual ones from Zenodo from [links they give in readme](https://github.com/ellisk42/ec/tree/icml_2021_supplement#datasets).

Examples commands to run LAPS are in [docs/icml_2021_experiments](https://github.com/ellisk42/ec/blob/icml_2021_supplement/docs/icml_2021_experiments)