# %%
import sqlite3

# %%
dbpath = f"db/firstdb.db"

# %%
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

# %%
sql = """
create table if not exist users
    (
    
    )
"""

# %%
conn.close()