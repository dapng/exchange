hello:
	echo "this is my first make"
run:
	docker-compose up
round:
	docker-compose up -d
stop:
	docker-compose stop
down:
	docker-compose down
migration:
	docker-compose exec web alembic revision --autogenerate -m $(name)
upgrade:
	docker-compose exec web alembic upgrade head
downgrade:
	docker-compose exec web alembic downgrade -1
stamp:
	docker-compose exec web alembic stamp head