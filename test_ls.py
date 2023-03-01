# list directory contents ( ls ) testing
import os
import shutil
import pytest
import subprocess
from pathlib import Path


class TestClass(object):
    @staticmethod
    def test_list_empty_folder():
        try:
            os.mkdir("/tmp/testfolder")
            result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
            assert not result.stdout, "Listing an empty folder did not return expected result"
        finally:
            shutil.rmtree("/tmp/testfolder")

    @staticmethod
    def test_simple_ls():
        try:
            os.mkdir("/tmp/testfolder")
            Path("/tmp/testfolder/first.txt").touch()
            result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
            print(f"this is the result [{result}]")
            assert "first.txt" in str(result.stdout), "Listing a folder with one file did not return expected result"
        finally:
            shutil.rmtree("/tmp/testfolder")

    @staticmethod
    def test_list_mutiple_files():
        try:
            os.mkdir("/tmp/testfolder")
            Path("/tmp/testfolder/first.txt").touch()
            Path("/tmp/testfolder/second.doc").touch()
            result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
            print(f"this is the result [{result}]")
            assert "first.txt" in str(result.stdout), "Listing a folder with multiple files did not return expected result"
            assert "second.doc" in str(result.stdout), "Listing a folder with multiple files did not return expected result"
        finally:
            shutil.rmtree("/tmp/testfolder")

    @staticmethod
    def test_hidden_files():
        try:
            os.mkdir("/tmp/testfolder")
            Path("/tmp/testfolder/first.txt").touch()
            Path("/tmp/testfolder/second.doc").touch()
            Path("/tmp/testfolder/.hidden_file").touch()
            result = subprocess.run(["ls", "/tmp/testfolder"], stdout=subprocess.PIPE)
            print(f"this is the result [{result}]")
            assert "first.txt" in str(result.stdout), "Listing a folder with a hidden file did not return expected result"
            assert ".hidden_file" not in str(result.stdout), "ls listed hidden file when it shouldn't have"
        finally:
            shutil.rmtree("/tmp/testfolder")

    @staticmethod
    def test_list_hidden_files():
        try:
            os.mkdir("/tmp/testfolder")
            Path("/tmp/testfolder/first.txt").touch()
            Path("/tmp/testfolder/second.doc").touch()
            Path("/tmp/testfolder/.hidden_file").touch()
            result = subprocess.run(["ls", "-a", "/tmp/testfolder"], stdout=subprocess.PIPE)
            print(f"this is the result [{result}]")
            assert "first.txt" in str(result.stdout), "Listing a folder with a hidden file did not return expected result"
            assert ".hidden_file" in str(result.stdout), "ls listed hidden file when it shouldn't have"
        finally:
            shutil.rmtree("/tmp/testfolder")