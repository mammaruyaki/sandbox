# %%
import sqlite3

# %%
dbpath = f"db/basic_crud.db"

# %%
conn = sqlite3.connect(dbpath)

# %%
conn.close()