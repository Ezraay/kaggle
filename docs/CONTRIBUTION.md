# How to Contribute

## Setting up the repository

First start by cloning the repository either through a desktop app or the commandline

```
git clone https://github.com/Ezraay/kaggle
```

The project is split into separate folders for separate concerns of the project.
For instance, the `docs/` folder contains important documentation. The `source/` folder contains all the scripts and
code for the project.

## Working with branches
In order to create changes in the repository, you should work in a separate branch to `develop` and `master`. To create a new branch
use the following command or use GitHub desktop:
```
git checkout -b feat/your-feature-name
```

The branch name should follow the guidelines below:

#### Creating a feature
`feat/your-feature-name`
#### Fixing a bug
`bugfix/your-bug-name`
#### Documentation (non-code changes)
`docs/short-docs-description`

To publish your new branch, use the following command:
```
git push
```

Then you can continue as usual with commits etc.
When you are finished with your changes, create a pull request into `develop` in order to merge your changes into the branch.
> NOTE: Do not create a pull request into `master` from your feature branch

## Initialising virtual environment

Make sure to work inside the source folder, including your venv and dependencies.

It's recommended to create a virtual environment for the project so that dependency packages are the same version
across all development environments. To create a virtual environment, use the following command or create it
via your IDE.

```
python -m venv ./venv/
```

Then you must activate the virtual environment for your shell. This is platform dependent, but for Windows, the command
is:

```
./venv/Scripts/activate.bat
```

If everything worked correctly, you should see some indication of (venv) in your command line.
Then you can install the project dependencies to your virtual environment.

```
pip install -r ./requirements.txt
```

If these dependencies ever change (i.e. update package version or new package requirement), you can
update the `requirements.txt` file with the following command:
```
pip freeze > requirements.txt
```

## Running the simulation

Make sure you open the `source/` folder in your editor of choice, otherwise Python imports may not
function correctly. The project assumes the root folder is `source/` from the location of execution.

To run the project, use the command line or create launch profiles in your IDE.

```
python ./main.py --help
```

The above command will show more information about specific command line arguments you can pass into the
program. To simulate a game between two agents, use the following command:

```
python ./main.py RandomAgent RandomAgent
```

## Where are the agents?

The simulation locates the agent in the `agents/` folder, and tries to find an agent in the file `random_agent.py`
(note the snake_case_naming) and a class named RandomAgent (note the PascalCaseNaming). If the file or class does not
exist, the script will fail, so make sure you spell the name of the agent correctly both in code and in execution.

Every agent must inherit from the base `Agent` class and override the `get_winning_move` function to create
custom agent behaviour.
[Please see AGENTS.md for more information. ](https://github.com/Ezraay/kaggle/blob/master/docs/AGENTS.md)