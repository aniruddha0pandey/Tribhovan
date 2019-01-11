from get_token import *
from qiskit import IBMQ


# Authenticate for access to remote backends
try:
    IBMQ.enable_account(API_TOKEN)
except:
    print("""WARNING: There's no connection with the API for remote backends.
             Have you initialized a file with your personal token?
             For now, there's only access to local simulator backends...""")

def execute():
    # Compile and run on a real device backend
    try:
        # select least busy available device and execute.
        least_busy_device = least_busy(IBMQ.backends(simulator=False))
        print("Running on current least busy device: ", least_busy_device)
        # running the job
        # Show the results
    except:
        print("All devices are currently unavailable.")

def main():
    # Quantum and Classical Register
    # Main Gate Initilization
    execute()

if __name__ == "__main__":
  main()
