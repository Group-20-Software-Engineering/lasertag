from dotenv import load_dotenv
load_dotenv()

import os

from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

data = supabase.table('player').insert({ 'id': 2, 'codename': 'Razor' }).execute()
data = supabase.table('player').select("*").execute()

print(data)

"""
example data retrieval: 
"response = supabase.table('player').select("*").execute()"

example data insertion: 
"data, count = supabase.table('player').insert({ "id": 1, "codename": "77" }).execute()"

example data update: 
"data, count = supabase.table('player').update({'codename': '69'}).eq('id', 1).execute()"

example data upsert (if present, then updates; if not present, then inserts):
"data, count = supabase.table('player').upsert({'id': 1, 'codename': '50'}).execute()"

example data deletion:
"data, count = supabase.table('player').delete().eq('id', 1).execute()"

"""


