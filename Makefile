deps:
	pip install uv
	uv pip install --no-cache --system -r requirements.lock

format:
	uv run ruff check src/ --fix
	uv run ruff format src/

lint:
	uv run ruff check src/ --fix
	uv run mypy src/

test:
	echo("WIP")

migrate:
	rye run alembic revision --autogenerate
	rye run alembic upgrade head

run:
	fastapi run src/app.py --host 0.0.0.0 --reload

run-dev:
	rye run fastapi dev src/app.py --reload
