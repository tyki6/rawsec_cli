"""Test file for search File"""
import csv
import io
import json
import os
import unittest
from unittest import TestCase
import unittest.mock

from rawsec_cli.output import json_output, csv_output, table_output, print_output
from rawsec_cli.search import searchProject
from rawsec_cli.search import searchProjectCTF
from rawsec_cli.search import searchProjectOperating
from rawsec_cli.search import searchProjectResources
from rawsec_cli.search import searchProjectTools

from unittest.mock import patch


def test_json_output(capsys):
    json_output(projects=[], file=None)
    captured = capsys.readouterr()
    assert "{'projects': [], 'total': 0}" in captured.out

    json_output(projects=[], file="test.json")
    assert os.path.exists("test.json")
    with open("test.json", "r") as json_file:
        data = json.load(json_file)
        assert "projects" in data
        assert "total" in data
    os.remove("test.json")


def test_csv_output(capsys):
    csv_output(projects=[], file=None, wanted_keys=["name", "source"])
    captured = capsys.readouterr()
    assert '"name","source"' in captured.out
    csv_output(projects=[{"name": "test", "source": "test"}], file="test.csv", wanted_keys=["name", "source"])
    assert os.path.exists("test.csv")
    with open("test.csv", "r") as csv_file:
        spamreader = csv.reader(csv_file, quoting=csv.QUOTE_ALL)
        headers = next(spamreader, None)
        assert "name" in headers
        assert "source" in headers
    os.remove("test.csv")


def test_table_output(capsys):
    table_output(projects=[], file=None, wanted_keys=["name", "source"])
    captured = capsys.readouterr()
    assert "Project not found!" in captured.out

    table_output(projects=[{"name": "test", "source": "test"}], file="test.txt", wanted_keys=["name", "source"])
    assert os.path.exists("test.txt")
    with open("test.txt", "r") as txt_file:
        text = txt_file.read()
        assert "name" in text
        assert "source" in text
    os.remove("test.txt")

    table_output(projects=[{"name": "test", "source": "test"}], file=None, wanted_keys=["name", "source"])
    captured = capsys.readouterr()
    assert "Total projects found: 1" in captured.out


def test_print_output(capsys):
    print_output(projects=[{"name": "test", "source": "test"}], output="table", wanted_keys=["name", "source"])
    captured = capsys.readouterr()
    assert "Total projects found: 1" in captured.out

    print_output(projects=[], output="json")
    captured = capsys.readouterr()
    assert "{'projects': [], 'total': 0}" in captured.out

    print_output(projects=[], output="csv", wanted_keys=["name", "source"])
    captured = capsys.readouterr()
    assert '"name","source"' in captured.out

    print_output(file="test.txt", projects=[{"name": "test", "source": "test"}], wanted_keys=["name", "source"])
    assert os.path.exists("test.txt")
    with open("test.txt", "r") as txt_file:
        text = txt_file.read()
        assert "name" in text
        assert "source" in text
    os.remove("test.txt")
