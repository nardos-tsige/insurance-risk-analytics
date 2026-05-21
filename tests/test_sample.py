import pytest 
import pandas as pd 
import numpy as np 
 
def test_pandas_version(): 
    assert pd.__version__ is not None 
 
def test_numpy_version(): 
    assert np.__version__ is not None 
 
def test_import_hypothesis_tests(): 
    try: 
        from src import hypothesis_tests 
        assert True 
    except ImportError: 
        assert False, "Failed to import hypothesis_tests" 
 
def test_import_modeling(): 
    try: 
        from src import modeling 
        assert True 
    except ImportError: 
        assert False, "Failed to import modeling" 
