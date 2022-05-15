import pandas as pd
from pandas.io.json import json_normalize
import requests

URL = 'https://jsonplaceholder.typicode.com/posts'

r = requests.get(URL)

j = r.json()

df = pd.json_normalize(j)
df.to_csv('Output.csv')
