import streamlit.web.cli as stcli
import os, sys

def main():
    # Aapka streamlit run wala code yahan hoga
    sys.argv = ["streamlit", "run", "app.py", "--server.port", "8000"]
    sys.exit(stcli.main())

# Yahan par niche ye line add kar do:
if __name__ == "__main__":
    main()