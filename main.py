from get_token import *
from qiskit import IBMQ


# Authenticate for access to remote backends
try:
    IBMQ.enable_account(API_TOKEN)
except:
    print("""WARNING: There's no connection with the API for remote backends.
             Have you initialized a file with your personal token?
             For now, there's only access to local simulator backends...""")


def main():
  pass
  

if __name__ == "__main__":
  main()
