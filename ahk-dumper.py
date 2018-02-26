import lief
from sys import argv,exit

binary = lief.parse(argv[1])

# Check if binary has a resources section
if binary.has_resources:
    rsrc_directory = binary.data_directory(lief.PE.DATA_DIRECTORY.RESOURCE_TABLE)
    print "Found resource section:\n"
    print(rsrc_directory.section)
else:
    exit("Error: No resource section")

#Build the resource manager
resource_manager = binary.resources_manager

#print resource_manager
print "\n\nSuccessfully built the resource manager! dumping RCDATA section:\n"
print resource_manager.get_node_type(lief.PE.RESOURCE_TYPES.RCDATA)

#Iterate over the RC_DATA section children, print the content inside
for i in resource_manager.get_node_type(lief.PE.RESOURCE_TYPES.RCDATA).childs:
    for i in i.childs:
        res =[chr(n) for n in i.content]
        print "==================== Hooray! Here is the code: ===================="
        print ''.join(res)


