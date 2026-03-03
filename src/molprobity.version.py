#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# molprobity.version.py - Get MolProbity version
#
# Copyright (C) 2026 Arthur Zalevsky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Get MolProbity version
"""

import argparse
import logging
from pathlib import Path
import subprocess
import re

def molprobity_version(self, tool: str = 'molprobity.clashscore') -> str:
    """
    Get MolProbity version.
    We assume that all tools belong to the same release.
    """
    version = "Not available"
    try:
        # Try to get "internal version" 4.x.x
        version = get_internal_version()
    except subprocess.CalledProcessError:
        logging.error(f'{tool} is missing')
    except FileNotFoundError:
        # Fallback to commit-based version
        version = subprocess.check_output(
            [tool, '--version'],
            text=True,
            stderr=subprocess.STDOUT).strip()

    return version

def get_internal_version(tool: str = 'molprobity.clashscore') -> str:
    """
    Get internal molprobity version.
    We assume that all tools belong to the same release.
    """
    version = None

    mp_tool_path = subprocess.check_output(
        ['which', tool],
        text=True,
        stderr=subprocess.STDOUT).strip()

    mp_core_path = Path(
        Path(mp_tool_path).parent,
        '../../molprobity/lib/core.php'
    )

    if mp_core_path.is_file():
        with open(str(mp_core_path), 'r') as f:
            raw = f.readlines()

        for line in raw:
           q = re.search('^define\\("MP_VERSION", "(?P<version>.*)"\\);', line)

           if q:
               version = q.group('version')
               break

        return version

    else:
        raise FileNotFoundError('Molprobity core.php module is missing')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="MolProbity validation",
        description="Assess quality of atomic models")

    parser.add_argument('-t', '--tool',
                        help='MolProbity tool to identify MolProbity installation path',
                        default='molprobity.clashscore',
                        required=False)

    args = parser.parse_args()

    version = molprobity_version(args.tool)

    print(version)
