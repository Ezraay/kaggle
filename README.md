# Kaggle

## Running a game
Use the following command to see more options.
```
python source/main.py --help
```

The following command runs a game between two agents.
```
python source/main.py RandomAgent RandomAgent
```

## Choosing a seed
By default, the simulation will run with a random seed, but if you want to observe the same random seed, 
use the following argument.
```
python source/main.py --seed 123312 RandomAgent RandomAgent
```