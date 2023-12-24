install: #installing 
	poetry install 

brain-games: #run the app
	poetry run brain-games

build: #poetry building
	poetry build

publish:
	poetry publish --dry-run

package-install:
	pip install --user --force-reinstall dist/*.whl

lint: #check code for the rules
	poetry run flake8 brain_games

