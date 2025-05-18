@echo off 
import unittest 
from src.main import print 
class TestMain(unittest.TestCase): 
    def test_print(self): 
        self.assertTrue(True) 
if __name__ == "__main__": 
    unittest.main() 
