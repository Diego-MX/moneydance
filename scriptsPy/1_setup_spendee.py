# 1. Indicate which file to open. 
# 2. Load category equivalence. 
# 3. Read each transaction. 
# 4. Identify possible problems. 
# 5. Store each transaction. 

import os
import sys
from dotenv import load_dotenv

load_dotenv(".env")
sys.path.append(os.getenv("REPO_DIR"))

spendee_dir = pd.read_csv("%s/data/spendee/spendee_latest.csv" % REPO_DIR)

categories = pd.read_csv("%s/data/schema/wallet.csv" % REPO_DIR)






