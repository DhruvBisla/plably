import os
import csv
import subprocess
import utils

class TestCLI():    
    def test_help(self):
        process = subprocess.Popen(['python3', '-m', 'plably', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        matches = ["help", "arguments", "positional", "-h", "--help"]
        assert(all(x in stdout.decode("utf-8") for x in matches))
        assert((stderr == b''))
    def test_graphing(self):
        utils.create_fake_data()
        os.system('python3 -m plably "Test vs. Test" tests/data.csv tests/output.png')
        assert(os.path.isfile("tests/output.png"))
