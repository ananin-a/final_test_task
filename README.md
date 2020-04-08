# Final_Test_Task

## How to execute the tests (Linux_OS_Settings):

1. Install python 3.8:

	```bash
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python3.8
	```

2. Install pip:

	```bash
	python3 -m pip install pip
	```

3. Create a virtual environment:

	```bash
	sudo apt-get install -y python3.8-venv
	mkdir ~/venv
	cd ~/venv
	python3 -m venv selenium
	```

4. Activate a virtual environment:

	```bash
	cd ~/venv
	source venv/bin/activate
	```

5. Install the necessary environment requirements (libraries, modules, packages etc.):

	```bash
	pip install -r requirements.txt
	```
	
6. Execute the tests from the terminal via the command:

	```bash
	pytest -v --tb=line <test_name.py>
	```
	
	The parameter `--tb=line` shortens the log with the test results.
	The parameter `--reruns N` can be used for rerunning the failed tests, where N is the number of the reruns.
	
	You can initialize custom marks in pytest.ini.
	
	Add the following parameter into command line when executong the tests to perform the ones with a certain mark:
	
	```bash
	-m <marking name>
	```
	
   - The key `-k` can be added to execute separate tests:

	```bash
	-k <test_name>
	```

7. To finish the work or before switching to another prject you need to deactivate the virtual environment:

	```bash
	deactivate
	```
