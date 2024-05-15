#!/usr/bin/env python3
import os

from aws_cdk import App
from infrastructure_stack import InfrastructureStack

app = App()
InfrastructureStack(app, "InfrastructureStack")

app.synth()
