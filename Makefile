# Makefile
# Usage: make build
build:
	docker compose build
run:
	docker compose up
stop:
	docker compose down

# Migration
# Usage: make makemigrations
makemigrations:
	docker compose run --rm todolist sh -c "python manage.py makemigrations"
migrate:
	docker compose run --rm todolist sh -c "python manage.py migrate"

# Fixtures
# Usage: make fixtures
fixtures:
	docker compose run --rm todolist sh -c "python manage.py flush && docker compose run --rm todolist sh -c "python manage.py loaddata fixtures.json

# Run tests
# Usage: make test
test:
	docker compose run --rm todolist sh -c "python manage.py test && flake8"

# Run django shell
# Usage: make shell
shell:
	docker compose run --rm todolist sh -c "python manage.py shell"
