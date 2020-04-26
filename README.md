# parse_google_sms
Extract text/SMS chats from Google Voice and save them as text files

Python 3.5+ only

## Installation
`pip3 install google_voice_parser`


## Download your Google Voice data
 - Visit the [Google Takeout landing page](https://takeout.google.com/settings/takeout?utm_source=ob&utm_campaign=takeout&hl=en)
 - Download your Voice data
 - Extract your Voice data


## Usage
- Locate the folder in which your Google Voice data is stored

  Example: `~/Downloads/Takeout/Voice/Calls`

```
alex@mbp:~/Projects/parse_google_sms$ parse_sms --help
Usage: parse_sms [OPTIONS] DIR

Options:
  --help  Show this message and exit.

alex@mbp:~/Projects/parse_google_sms$ python3 parse_google_sms.py ~/Downloads/Takeout/Voice/Calls
chat_14_Nov_2012_04_04_59_Person1_Me.txt
chat_08_Feb_2016_09_01_56_Person2_Me.txt
chat_16_Mar_2015_09_53_46_Person3_Me.txt
chat_02_Dec_2015_05_30_53_Person4_Me.txt
chat_30_Dec_2015_11_24_16_Person5_Me.txt
...
```

## License
See `LICENSE`. Message me if you'd like to use this project with a different license.
