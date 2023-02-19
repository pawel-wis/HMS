import os
import unittest

def main(test_path, test_pattern):
	print(f"Searich for tests in: {test_path}")
	suite = unittest.TestLoader().discover(test_path, test_pattern)
	unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
	root_path = os.path.abspath('.')
	test_path = os.path.join(root_path, 'tests/')
	test_pattern = '*test.py'
	main(test_path, test_pattern)
