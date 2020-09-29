import os
import re
from csv import reader 


def setup_moneydance():
  pass


def load_categories(csv_file): 
  cat_dict = dict()  
  with open(csv_file, 'r') as f:
    csv_reader = reader(f)
    headers = csv_reader()

    # spendee_type, spendee_category, moneydance_category
    if headers != ["spendee_type", "spendee_category", "moneydance_category"]:
      raise ValueError("CSV headers don't fit TYPE, CATEGORY, MONEYDANCE.")

    for row in csv_reader():
      cat_dict[row[1]] = (row[2], row[0])
    
  return cat_dict



def csv_to_list(csv_file): 
  rows = []

  with open(csv_file, 'r') as f:
    csv_reader = reader(f)
    headers = csv_reader()

    for row in csv_reader():
      rows.append(row)
    
  return (headers, rows)
    

def latest_file(dir, pattern=None):

  pattern = pattern or r".*([\d-]*).*"

  matches = []
  for a_file in os.listdir(dir):
    does_match = re.match(pattern, a_file)
    if does_match:
      a_tuple = (does_match.expand(r"\1"), does_match.string)
      matches.append(a_tuple)

  return max(matches)[1]


def save_transaction(book, txn_ls, type=None):
  if type is None:
    raise ValueError("Must specify TYPE of transaction.")

  # Date, Description, Category, Payment/Deposit, Memo, Tags
  if type == "spendee": 
    # Date, Wallet, Category Type, Category Name, Amount, Currency, Note, 
    # First Name, Last Name
    pass 

  elif type == "banamex": 
    # Fecha dd-mm-yyyy, Descripción, Débito, Crédito, Saldo, Moneda
    pass
  else:
    raise ValueError("Specified TYPE isn't known.")



def importer_ready(file, type=None):
  if type is None:
    raise ValueError("Must specify TYPE of file (spendee, banamex).")
  
  if type == "spendee": 
    pass 
  elif type == "banamex":
    pass
  else:
    raise ValueError("Specified TYPE is not known.")
  
  

