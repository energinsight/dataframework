# intsalation

## Linux
cd /to/target/directory

git clone https://github.com/energinsight/intradayinsight.git

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirement.txt

Note: the API keys need to be saved as env variables.

If you only want to install the dataframework package, then run "pip install git+https://github.com/energinsight/dataframework.git" in the activated env.



## Windows
cd /to/target/directory

python -m venv venv

venv\Scripts\activate
