#!/usr/bin/env python3
"""
Generates an install.bat script for running on a target to install the simulator.
"""
import logging
import os
import subprocess
import sys
import re
from pathlib import Path


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
project_root = Path(__file__).parents[1]


try:
    version = subprocess.check_output(
        ['git', 'describe', '--tags', '--always'],
        cwd=str(project_root),
    ).decode().strip()
except subprocess.CalledProcessError:
    logger.exception("Failed to get version from git")
    exit(1)

(project_root / "dist-gh-release").mkdir(exist_ok=True)
os.chdir(str(project_root / "dist-gh-release"))

logger.info("Loading template")
with open((project_root / "assets" / "install.bat"), "r") as f:
    source = f.read()

script = re.sub("__RELEASE__", version, source)

logger.info("Writing script")
with open((project_root / "dist-gh-release" / "install.bat"), "w") as f:
    f.write(script)

logger.info("Success")