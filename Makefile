# Makefile
# Usage: make build
build:
	docker compose build
run:
	docker compose up -d
stop:
	docker compose stop
down:
	docker compose down

# Migration
# Usage: make migrate
migrate:
	docker compose exec  todolist python manage.py makemigrations
	docker compose exec  todolist python manage.py migrate

# Fixtures
# Usage: make fixtures
fixtures:
	docker compose exec todolist python manage.py flush && docker compose exec todolist python manage.py loaddata fixtures.json

# Run tests
# Usage: make test
test:
	docker compose exec todolist python manage.py test

# Run django shell
# Usage: make shell
shell:
	docker compose exec todolist python manage.py shell
