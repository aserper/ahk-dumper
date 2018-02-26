# ahk-dumper

Ahk-dumper is a tool to dump AutoHotKey code from the RDATA section of a PE file.

##Usage is very simple:
$ python ahk-dumper.py <ahk-pe-file.exe>

##Prerequisites: 
[The Lief Python library](https://github.com/lief-project/LIEF)

##Note: 
This was a quick-and-dirty one off for a specific case of AHK malware. It should work for other AHK files as well.
Please let me know if there are any bugs.

