from typing import Union
import numpy as np
import sapien
from mani_skill.utils import sapien_utils, common
from mani_skill.envs.sapien_env import BaseEnv
from mani_skill.utils.registration import register_env
from mani_skill.agents.robots import PandaWristCam
from mani_skill.envs.tasks.tabletop.peg_insertion_side import PegInsertionSideEnv
from mani_skill.utils.building import actors
import torch
from typing import Dict

@register_env("insert-residual", max_episode_steps=50)
class InsertResidualEnv(PegInsertionSideEnv):
    SUPPORTED_ROBOTS = ["panda_wristcam"]
    agent: Union[PandaWristCam]

    def __init__(self, *args, robot_uids="panda_wristcam", **kwargs):
        super().__init__(*args, robot_uids=robot_uids, **kwargs)

    def _load_agent(self, options: dict):
        super()._load_agent(options)
    
    def _load_scene(self, options):
        return super()._load_scene(options)