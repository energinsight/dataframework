# About dataframework

dataframework facilitates loading data from different sources.

Below is a sample:

![PTDF Plot](./newplot.png)

## Note:

The dataframework package is currently under development. Most of the content on the Jao website has already been added. The current focus is on the ENTSOe platform.

https://newtransparency.entsoe.eu/

https://transparency.entsoe.eu/dashboard/show

https://publicationtool.jao.eu/

https://www.netztransparenz.de/en/

https://www.elia.be/en/grid-data/open-data

https://www.tennet.eu/markets/transparency-netherlands

# Installation


## Linux
cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

<!-- git clone https://github.com/energinsight/dataframework.git -->

python3 -m venv .myenv

source .myenv/bin/activate

python3 -m pip install -r requirement.txt



## Windows
cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

python -m venv myenv

myenv\Scripts\activate

pip install -r requirement.txt


## Download the sample script:
curl -o Loader.py https://raw.githubusercontent.com/energinsight/dataframework/main/Loader.py

## Note: the API keys

If you are not going to use some sources, their API keys do not need to be added to the env variables. For example, if you only want to read data from ENTSOe, you only need to add ENTSOE_API_KEY. 

### Linux:
Add the following lines (with your API keys) to the end of .venv/bin/activate file:

export ENTSOE_API_KEY='Your-API-Key'

export netztransparenz_CLIENT_ID='Your-API-Key'

export netztransparenz_Client_Secret='Your-API-Key'


### Windows:

setx ENTSOE_API_KEY "Your-API-Key"

echo %ENTSOE_API_KEY%

Repeat the same steps for other API keys that are required.

### Please restart the env.

#### Test:
import os

api_key = os.getenv('ENTSOE_API_KEY')

print(api_key)


### Are you looking for some examples? Check out Loader.py...

