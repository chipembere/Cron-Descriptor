# Cron-Like-Syntax-Parser

This is a command line tool that takes a single (time) argument in the format ```HH:MM```, accepts STDIN config lines with the format ```* 19 /bin/run_me_sixty_times``` and returns the earliest time a command will be executed.

##  How To Run

You need to be using ** python 3 ** or above.
You need to have a ```config``` file in the same directory, the format.
```
30 1 /bin/run_me_daily
* 19 /bin/run_me_sixty_times
```

To run: ```./cron_reader.py 13:38 < config```
To run: ```python3 cron_reader.py 18:45 < config```
To  test: ```python3 test_cron_reader.py```