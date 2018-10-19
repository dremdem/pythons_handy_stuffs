connect_parameters = {
	"host": "10.77.0.111",
	"port": "5432",
	"user": "postgres",
    "password": "0mni@300!",
    "dbname": "minfin"
}

dns = " ".join([k+'='+v for k, v in connect_parameters.items()])

print(dns)