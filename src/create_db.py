# %%
import sqlite3

# %%
dbpath = f"db/firstdb.db"

# %%
conn = sqlite3.connect(dbpath)

# %%
conn.close()