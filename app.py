#!/usr/bin/env python3

import os
from aws_cdk import core

from compute_notifier.compute_notifier_stack import ComputeNotifierStack

deploy_env = os.getenv('DEPLOY_ENVIRONMENT', 'dev')

app = core.App()

ComputeNotifierStack(app, "computeNotifier", deploy_env=deploy_env)

app.synth()
