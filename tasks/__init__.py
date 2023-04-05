from invoke import Collection, task

from . import utils

ns = Collection()


@task(
    optional=[
        "config_file",
        "model",
        "dataset",
        "nproc",
        "log_level",
    ],
)
def run_recbole(
    ctx,
    config_file="src/recboletutorial/configs/basic.yaml",
    model="NeuMF",
    dataset="ml-100k",
    nproc=1,
    log_level="info",
):
    """Trains a RecSys model using RecBole framework.

    Args:
        config_file (str, optional): path to the config file.
        Defaults to `src/recboletutorial/configs/basic.yaml`.

        model (str, optional): name of the model to use. Defaults to
        `NeuMF`.

        dataset (str, optional): name or path to the dataset to use.
        Defaults to `ml-100k`.

        nproc (int, optional): number of processes to spawn. Defaults to 1.

        log_level (str, optional): the logging level to use. Default to "info"
    """
    import os

    # paths to store all RecBole related files: data, model checkpoints
    artifacts_dir = "recbole_artifacts"
    utils.ensure_dir(artifacts_dir)

    python_script_path = "recboletutorial.run_recbole"
    data_path = os.path.join(artifacts_dir, "dataset/")
    checkpoint_dir = os.path.join(artifacts_dir, "saved/")

    cmd = f"python -m {python_script_path}"
    cmd += f" --config_files={config_file}"
    cmd += f" --model={model}"
    cmd += f" --dataset={dataset}"
    cmd += f" --nproc={nproc}"
    cmd += f" --data_path={data_path}"
    cmd += f" --checkpoint_dir={checkpoint_dir}"
    cmd += f" --state={log_level}"

    ctx.run(cmd)


ns.add_task(run_recbole)
