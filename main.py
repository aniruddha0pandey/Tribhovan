from get_token import *
from qiskit import IBMQ

def main():
  IBMQ.enable_account(API_TOKEN)

if __name__ == "__main__":
  main()
