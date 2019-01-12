# -*- coding: utf-8 -*-
import requests

session = requests.Session()
data={'username':'kingname','password':'genius','remember':'Yes'}
session.post(
    'http://exercise.kingname.info/exercise_login',data=data)
source=session.get('http://exercise.kingname.info/exercise_login_success').content.decode()
print(source)