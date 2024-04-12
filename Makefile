.PHONY: run i f t  c

# Run the projet
run:
	@poetry shell
	
# Install dev dependences
i:
	@poetry add --group dev pytest isort mkdocs blue pylint python-dotenv pyinstaller
	@pylint --generate-rcfile > .pylintrc
	@mkdocs new .

# Format the code
f:
	@isort .
	@blue .

# Teste the code 
t:
	@pytest .

# Preper project to commit
c:
	@pytest .
	@isort .
	@blue .
	@pylint .