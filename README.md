# Sample event driven implementation with pub/sub model

# Requirements
* You need [Redis](https://redis.io/docs/get-started/) before running the app. Redis will act as the message broker. Simply run `docker-compuse up`.
* [Poetry](https://python-poetry.org/!) for managing the dependencies of the app. Install it and then install the project doing `poetry install`.

# Running the app
After installing the project with `poetry install`, you can run the three apps simultaneously. Open your terminal and run:
1. Controller: This app is the central controller, it contains the processors for each of the applications and the event controller which routes the messages to each stream.
   1. `poetry run python3 src/controller/main.py mgnt`
   2. `poetry run python3 src/controller/main.py chef`
   3. `poetry run python3 src/controller/main.py staff`
2. Chef: The app that makes the cooking. `uwsgi --http 127.0.0.1:5001 --master -p 4 -w chef.uwsgi:app --enable-threads`
3. Staff: Take note of orders and sends them to kitchen. `uwsgi --http 127.0.0.1:5000 --master -p 4 -w staff.uwsgi:app --enable-threads`
4. Management: The guys in charge of reporting and closing/Opening the restaurant. `uwsgi --http 127.0.0.1:5002 --master -p 4 -w management.uwsgi:app --enable-threads`

You can navigate to the urls of each microservice and play around with their endpoints. Check the logs in the controller & processor units to see how messages are being sent and how they trigger other processes.


# YugabyteDB Connection
To connect to YBDB through the CLI, install ysqlsh tool and then run:
```bash
ysqlsh "host=us-east-1.ea53f2e6-4666-4fce-999c-2f7d7fc6b4ea.aws.ybdb.io \
user=admin \
dbname=yugabyte \
sslmode=verify-full \
sslrootcert=./certs/root.crt"
```
Replace the following:
1. <DB USER> with your database username. You will be prompted for the password after the connection is established.
2. yugabyte with the database name, if you're connecting to a database other than the default (yugabyte).
3. <ROOT_CERT_PATH> with the path to the root.crt CA certificate you downloaded.
