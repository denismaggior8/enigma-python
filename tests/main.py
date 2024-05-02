import unittest


if __name__ == "__main__":   
    suite = unittest.TestLoader().discover(start_dir="tests",pattern="*_test*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)