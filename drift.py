import os
from openstack import connection

conn = connection.Connection(auth_url= "https://api.skyhigh.iik.ntnu.no:8774/v2.1",
                             project_name=str(os.getenv("OS_PROJECT_NAME")),
                             username=str(os.getenv("OS_USERNAME")),
                             password=str(os.getenv("OS_PASSWORD")),
                             user_domain_id=str(os.getenv("OS_USER_DOMAIN_NAME")),
                             project_domain_id=str(os.getenv("OS_PROJECT_DOMAIN_ID"))
                             )

def list_servers(connection):
    print("list servers:")
    for server in conn.compute.servers():
        print(server)

list_servers(conn)
