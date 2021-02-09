# rock-paper-scissors-assignment

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository] https://github.com/EmilioAngelM/rock-paper-scissors-assignment under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-assignment
```

Use Anaconda to create and activate a new virtual environment, perhaps called "rock-paper-scissors-env":

```sh
conda create -n rock-paper-scissors-env python=3.8
conda activate rock-paper-scissors-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install python-dotenv
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file with the name ".env." The create a "PLAYER_NAME" variable that contains your name:

    PLAYER_NAME="YOUR NAME"

Example: 
    PLAYER_NAME="Emilio Angel"

## Usage

Run the game script:

```py
python game.py
