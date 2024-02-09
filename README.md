# Sample event driven implementation with pub/sub model


# YugabyteDB Connection
To connect to YBDB through the CLI, install ysqlsh tool and then run:
```bash
ysqlsh "host=us-east-1.ea53f2e6-4666-4fce-999c-2f7d7fc6b4ea.aws.ybdb.io \
user=admin \
dbname=yugabyte \
sslmode=verify-full \
sslrootcert=/Users/cesar/workspaces/pubsub-microservices/certs/root.crt"
```
Replace the following:
1. <DB USER> with your database username. You will be prompted for the password after the connection is established.
2. yugabyte with the database name, if you're connecting to a database other than the default (yugabyte).
3. <ROOT_CERT_PATH> with the path to the root.crt CA certificate you downloaded.
