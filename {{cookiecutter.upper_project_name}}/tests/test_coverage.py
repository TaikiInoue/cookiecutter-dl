from omegaconf import OmegaConf

from {{cookiecutter.lower_project_name}}.runner import Runner


def test_coverage() -> None:

    cfg = OmegaConf.load("./config.yaml")
    runner = Runner(cfg)
    runner.run()
