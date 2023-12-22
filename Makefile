install: #installing 
	poetry install 

brain-games: #run the app
	poetry run brain-games

build: #poetry building
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

