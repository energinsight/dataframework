# intsalation


## Linux
cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

<!-- git clone https://github.com/energinsight/dataframework.git -->

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirement.txt



## Windows
cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

python -m venv venv

venv\Scripts\activate

pip install -r requirement.txt


## Download the sample script:
curl -o Loader.py https://raw.githubusercontent.com/energinsight/dataframework/main/Loader.py

## Note: the API keys need to be saved as env variables.

### Linux:
Add the following lines (with your API keys) to the end of .venv/bin/activate file:

export ENTSOE_API_KEY='Your-API-Key'
export netztransparenz_CLIENT_ID='Your-API-Key'
export netztransparenz_Client_Secret='Your-API-Key'



