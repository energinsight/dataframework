<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Installation Guide</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>Installation</h1>

    <h2>Linux</h2>
    <pre><code>cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

<!-- git clone https://github.com/energinsight/dataframework.git -->

python3 -m venv .myenv

source .myenv/bin/activate

python3 -m pip install -r requirement.txt
    </code></pre>

    <h2>Windows</h2>
    <pre><code>cd /to/target/directory

curl -o requirement.txt https://raw.githubusercontent.com/energinsight/dataframework/main/requirement.txt

python -m venv myenv

myenv\Scripts\activate

pip install -r requirement.txt
    </code></pre>

    <h2>Download the sample script:</h2>
    <pre><code>curl -o Loader.py https://raw.githubusercontent.com/energinsight/dataframework/main/Loader.py
    </code></pre>

    <h2>Note: the API keys</h2>
    <p>If you are not going to use some sources, their API keys do not need to be added to the env variables. For example, if you only want to read data from ENTSOe, you only need to add <code>ENTSOE_API_KEY</code>.</p>

    <h3>Linux:</h3>
    <p>Add the following lines (with your API keys) to the end of <code>.venv/bin/activate</code> file:</p>
    <pre><code>export ENTSOE_API_KEY='Your-API-Key'

export netztransparenz_CLIENT_ID='Your-API-Key'

export netztransparenz_Client_Secret='Your-API-Key'
    </code></pre>

    <h3>Windows:</h3>
    <pre><code>setx ENTSOE_API_KEY "Your-API-Key"

echo %ENTSOE_API_KEY%
    </code></pre>
    <p>Repeat the same steps for other API keys that are required.</p>

    <h3>Please restart the env.</h3>

    <h4>Test:</h4>
    <pre><code>import os

api_key = os.getenv('ENTSOE_API_KEY')

print(api_key)
    </code></pre>
</body>
</html>
