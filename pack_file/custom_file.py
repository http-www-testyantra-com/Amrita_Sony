from configparser import ConfigParser

c=ConfigParser()
c["settings"]={'debug':'true',
               'secret_key':'abc123',
               'log_path':'D:\\pyth_config'}

c['DB']={'db_name':'Mysql',
         'db_type':'RDBMS',
         'db_port':8888}

# with open("D:\\pyth_config\\Sample.ini","w") as f:
#     c.write(f)
f=open("D:\\pyth_config\\Sample1.ini","w")
c.write(f)
f.close()
