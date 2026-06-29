import streamlit.web.cli as stcli
import os, sys

def main():
    sys.argv = ["streamlit", "run", "api/index.py", "--server.port", "8000"]
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()