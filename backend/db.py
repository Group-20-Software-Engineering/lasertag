import os
from supabase import create_client, client

url: str = os.environ.get("https://jmfukmeanfezxzgrsitj.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImptZnVrbWVhbmZlenh6Z3JzaXRqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNTEyMDMsImV4cCI6MjAyMjgyNzIwM30.r99dqev77H1YPfAudZ9xm5heBt-jR-dNDiuI8-xVuZk")
supabase: Client = create_client(url, key)

"""
example data retrieval: 
"response = supabase.table('player')
    .select("*")
    .execute()"

example data insertion: 
"data, count = supabase.table('player')
    .insert({ "id": 1, "codename": "77" })
    .execute()"

example data update: 
"data, count = supabase.table('player')
    .update({'codename': '69'})
    .eq('id', 1)
    .execute()"

example data upsert (if present, then updates; if not present, then inserts):
"data, count = supabase.table('player')
    .upsert({'id': 1, 'codename': '50'})
    .execute()"

example data deletion:
"data, count = supabase.table('player')
  .delete()
  .eq('id', 1)
  .execute()"

"""


