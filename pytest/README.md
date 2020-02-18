# PYTEST
pytest will run all files of the form test_*.py or *_test.py in the current 
directory and its subdirectories.
# Calling pytest through python
python -m pytest [...]
# Stopping after the first (or N) failures
pytest -x  // stop after first failures
pytest --maxfail=2  // stop after two failures