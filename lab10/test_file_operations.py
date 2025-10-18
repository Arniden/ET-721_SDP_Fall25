'''
Arnaud Tadonkeng
Oct 15, 2025
Lab #10: File Operation Test
'''
import unittest
import os
from lab10.file_operations import read_file, write_file, append_file, email_read

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to file
        msg = "Arnaud Tadonkeng"
        with open(self.filename, "w") as f:
            f.write(msg)

        # verify file exits and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        # test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)
        
        with open(self.filename, "r") as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file
        initial_content = "Line one"
        append_content = "\nLine two"

        with open(self.filename, "w") as f:
            f.write(initial_content)
        
        with open(self.filename, "a") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)
    
    # LAB EXERCISE
    def test_email_read(self):
        # create an input file with several emails so email_read can count them
        emails = [
            "nick@yahoo.com",
            "vsingh@gmail.com",
            "aparker@gmail.com",
            "pchen@hotmail.com",
            "fsmith@gmail.com",
            "jcandela@yahoo.com",
            "cpeterson@hotmail.com",
            "kbrook@gmail.com",
            "tng@hotmail.com",
            "jhunter@yahoo.com",
            "pfranco@gmail.com",
            "mmansion@gmail.com",
            "clee@hotmail.com",
        ]

        # write the emails to the test input file (one per line)
        with open(self.filename, "w") as f:
            for i, e in enumerate(emails):
                # include a name part to mimic the real file format
                f.write(f"User{i}, {e}\n")

        # call email_read which should create a report file named 'reportemail.txt'
        report_name = "reportemail.txt"
        # ensure no leftover report exists
        if os.path.exists(report_name):
            os.remove(report_name)

        # call the function under test
        email_read(self.filename, report_name)

        # read the generated report and verify contents
        with open(report_name, "r") as f:
            report = f.read()

        expected = "yahoo = 3\ngmail = 6\nhotmail = 4\n"
        self.assertEqual(report, expected)
        # cleanup report file
        if os.path.exists(report_name):
            os.remove(report_name)
            

# run the unittest automatically when the file is run 
if __name__ == "__main__":
    unittest.main()