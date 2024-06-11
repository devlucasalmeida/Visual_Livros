import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Books.py"]
sys.exit(stcli.main())