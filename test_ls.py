# list directory contents ( ls ) testing
import os
import shutil
import pytest
import subprocess
from pathlib import Path


def test_list_empty_folder():# should pass (once)
    os.mkdir("/tmp/testfolder")
    result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
    assert not result.stdout
    shutil.rmtree("/tmp/testfolder")

def test_simple_ls():#s hould fail
    os.mkdir("/tmp/testfolder")
    Path("/tmp/testfolder/first.txt").touch()
    result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
    assert not result.stdout
    shutil.rmtree("/tmp/testfolder")