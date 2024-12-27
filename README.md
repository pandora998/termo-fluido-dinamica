# termo-fluido-dinamica

1. Create virtual environment 

```
sudo apt-get install -y python3-venv

mkdir directory_env
cd directory_env

python -m venv

source <directory_env>/bin/activate


facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ python3 -m venv env
facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ cd env/
facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica/env$ cd ..
facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ source env/bin/activate
(env) facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ 

```

2. Download pyturb source code:

[pyTurb library code](https://github.com/MRod5/pyturb/tree/master)

3. Install it by pip install -e <path/to/pyturb/setup.py file>

```
(env) facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ pip install -e ../pyturb/
Obtaining file:///home/facu/termofluidodinamica/pyturb
  Preparing metadata (setup.py) ... done
Collecting numpy
  Using cached numpy-2.2.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.4 MB)
Collecting scipy
  Using cached scipy-1.14.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (41.2 MB)
Installing collected packages: numpy, scipy, pyTurb
  Running setup.py develop for pyTurb
Successfully installed numpy-2.2.1 pyTurb-0.4.0 scipy-1.14.1

```

4. Install other dependencies
```

pip install pandas

pip install matplotlib

pip install jupyter

pip install ipykernel

```

5. Downgrade numpy library to work with matplotlib

```
pip install numpy==1.23.5

```

6. Open VSCode with Jupyte extension enabled

(env) facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ code .


7. Alternative, execute notebook by command line 
```
(env) facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ python -m ipykernel install --user --name=env

(env) facu@facu-dell:~/termofluidodinamica/termo-fluido-dinamica$ jupyter nbconvert --to notebook --execute mynotebook.ipynb

```