#db-init:
#	docker-compose exec web flask db init

db-migrate: # run after changes are made to model
	docker-compose exec web flask db migrate

db-upgrade: # upgrade the database according to migrations
	docker-compose exec web flask db upgrade

flask-shell:
	docker-compose exec web flask shell
