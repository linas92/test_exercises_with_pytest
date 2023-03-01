# list directory contents ( ls ) testing & dir 
import os
import sys
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
            

    @staticmethod
    @pytest.mark.skipif(sys.platform.startswith("win"), reason="Skipping non-windows test")
    def test_list_hidden_files_test_with_mark():
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

   
    @staticmethod
    def test_dir_windows_only():
        if not sys.platform.startswith("win"):
            pytest.skip("Skipping windows-only test")
        try:
            os.mkdir("c\testfolder")
            Path("c\testfolder\first.txt").touch()
            result = subprocess.run(["dir", "c\testfolder"], stdout=subprocess.PIPE)
            print("Result: [{}]".format(result))
            assert "first.txt" in str(result.stdout), "Listing a folder ON WINDOWS with one file did not return as expected"
        finally:
            shutil.rmtree("c\testfolder")


    @staticmethod
    @pytest.mark.skipif(not sys.platform.startswith("win"), reason="Skipping windows-only test")# same test with "pytest.mark."
    def test_dir_windows_only_test_with_mark():
        try:
            os.mkdir("c\testfolder")
            Path("c\testfolder\first.txt").touch()
            result = subprocess.run(["dir", "c\testfolder"], stdout=subprocess.PIPE)
            print("Result: [{}]".format(result))
            assert "first.txt" in str(result.stdout), "Listing a folder ON WINDOWS with one file did not return as expected"
        finally:
            shutil.rmtree("c\testfolder")


    @staticmethod
    @pytest.mark.xfail(reason="-y parameter does not yet work")
    def test_uninplemented_feature_should_fail():
        try:
            os.mkdir("/tmp/testfolder")
            Path("/tmp/testfolder/first.txt").touch()
            result = subprocess.run(["ls", "-y", "/tmp/testfolder"], stdout=subprocess.PIPE)
            print(f"this is the result [{result}]")
            assert "first.txt" in str(result.stdout), "Listing a foilder with -y did not return an expected result"
        finally:
            shutil.rmtree("/tmp/testfolder")