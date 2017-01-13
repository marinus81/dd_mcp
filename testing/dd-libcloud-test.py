from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.base import NodeAuthPassword
from libcloud.compute.providers import get_driver
import libcloud.security

libcloud.security.VERIFY_SSL_CERT = False
DimensionData = get_driver(Provider.DIMENSIONDATA)



driver = DimensionData('david.hamann.demo','yJx1t3Na8fEC!',region='dd-na')
rootPw = NodeAuthPassword('password123')
location = driver.ex_get_location_by_id('NA9')
pprint(location)
network_domain = driver.ex_list_network_domains(location=location)[1]
vlan = driver.ex_list_vlans(location=location, network_domain=network_domain)[0]
pprint(vlan)

nodes=driver.list_nodes()
pprint(nodes)
 
