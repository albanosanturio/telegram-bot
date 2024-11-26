# telegram-bot
playing around with a bot


#### Overview:
Learning to create a telegram bots with its commands.

#### References:
https://core.telegram.org/bots
https://www.youtube.com/watch?v=vZtm1wuA2yc
https://web.telegram.org/k/#@BotFather


Script processes interval data read by energy meters.
Main goal is to parse the .xml input format to a .tsv needed
It's also needed to filter out some unneeded readings:
    - Filter out meters not included in an "approved meters" list
    - Filter out readings based on the "approval date" of the meters (Reading time must be AFTER approval date)
    - Process only meters of the selected company (opco)

#### Requirements:
requirements

##### Config.json file
.json file

##### Arguments
Arguments


#### Sample .XML input
sample input


 #### Sample .TSV output:
sample output