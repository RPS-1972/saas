


import requests
from redminelib import Redmine



redmine = Redmine('http://a86da68e182334d1ba803f60cfb0d60c-1500208688.ap-southeast-1.elb.amazonaws.com/', username='user', password='hEKru8B3nM')

users = redmine.user.all()
print(users)

