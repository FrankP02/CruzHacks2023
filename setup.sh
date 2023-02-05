#!\bin\bash

if [ $# -eq 0 ]; then
  DATA_DIR="./"
else
  DATA_DIR="$1"
fi

python -m pip install -r .\requirements.txt
