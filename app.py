#!/usr/bin/env python3

import os
import json
from aws_cdk import core

from compute_notifier.compute_notifier_stack import ComputeNotifierStack


def load_aux_config(environment: str):
    aux_config_file = os.path.expanduser(f'./aux_config/{environment}.json')

    if not os.path.isfile(aux_config_file):
        return None
    with open(aux_config_file) as f:
        try:
            config = json.load(f)
        except Exception as e:
            print('Not able to load aux config file {} : {}'.format(aux_config_file, e))
            return None
    return config


deploy_env = os.getenv('DEPLOY_ENVIRONMENT', 'dev')
aux_config = load_aux_config(deploy_env)

app = core.App()

ComputeNotifierStack(app,
                     "computeNotifier",
                     deploy_env=deploy_env,
                     aux_config=aux_config)

app.synth()
