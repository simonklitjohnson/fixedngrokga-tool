# fixedngrokga

Tool to use for [fixedngrok.ga](http://fixedngrok.ga).

Run `fixedngrok` to update your URL when ngrok is running on your machine.

## Installation
### macOS and Linux
Install the primary script with this simple one-liner:

`curl -o fixedngrok https://raw.githubusercontent.com/simonklitjohnson/fixedngrokga-tool/master/fixedngrokga.py && chmod +x fixedngrok && mv fixedngrok /usr/local/bin && nano /usr/local/bin/fixedngrok`

Then update the bag_id and authtoken with your information and save.

In case you want fixedngrokga-tool to run automatically when you launch your ngrok instance, you have to install the bridge-script aswell. I usually install it as `ngrokk`, so that I simply run `ngrokk` instead of `ngrok` when I want it to update by fixedngrokga bag.

Install the bridge-script with the following one-liner:

`curl -o ngrokk https://raw.githubusercontent.com/simonklitjohnson/fixedngrokga-tool/master/bridge-script.py && chmod +x ngrokk && mv ngrokk /usr/local/bin`
