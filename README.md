# PyData Geneva: RecBole Tutorial
Repository containing a simple tutorial on how to use RecBole to
build a recommendation system. This tutorial is part of the [PyData Geneva Session](https://www.meetup.com/pydata-geneve/events/292560839/) 
held on April 5 2023. You can find the slides [here](slides.pdf).

## Requirements

`Poetry` 1.3.0 or above installed to manage the project dependencies. Then 
install the dependencies with `poetry`:

```bash
poetry install
```

### Install the Git hooks

Install the git hooks with:

```bash
poetry run pre-commit install
```

after which the git hooks will run automatically on `git commit`.


## Train a RecSys

Run the following command to train a recommendation system

```bash
poetry run inv run-recbole -c <path_to_config_file> -m <recbole_model_name> -f <dataset_name> -n <num_processes>
```

where:
- `path_to_config_file`: is a path to configuration file. This can be any RecBole
compatible configuration file. There are some configuration files ready to use
in `src/recboletutorial/configs`. By default set to `src/recboletutorial/configs/basic.yaml`
- `recbole_model_name`: is the name of the model to use. Here is a [list of all
models supported by RecBole](https://recbole.io/model_list.html). By default set
to `NeuMF`
- `dataset_name`: is the name of the dataset to use. Custom datasets are stored
in `recbole_artifacts/dataset`. By default set to `ml-100k`.
- `num_processes`: is the number of processes running in parallel to train the
model. This corresponds to the number of available GPUs. By default set to 1.

During the training process the model checkpoints are stored in `recbole_artifacts/saved`.
The `TensorBoard` logs are stored in the `log_tensorboard` directory, while the
log messages are stored in the `log` directory.