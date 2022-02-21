''' as downloading using provided links is not working,
    instead copy from ftp location. To do this:
    First mount ftp.sra.ebi.ac.uk
    then find location of this mount on your machine,
    on ubuntu this should be something similar to base below,
    Run this script in the same folder as E-MTAB-9786 file,
    run with any python 3

    then run resulting .sh file on local machine
    - todo so, setup connection to server as bbt-remote

    this is a hacky solution to something which shouldn't be a problem...
'''

import os
file = open('E-MTAB-9786.sdrf.txt', 'r')
write = open('scp_ftps.sh', 'w')
base = '/run/user/1000/gvfs/ftp:host=ftp.sra.ebi.ac.uk/vol1/fastq/ERR485/'
for line in file:
    splits = line.split('\t')
    if splits[29][0] == 'f':
        fp = splits[29].split('/')
        fp = '/'.join(fp[-3:])
        path = os.path.join(base, fp)
        write.write(f'scp {path} bbt-remote:data/ \n')
file.close()
write.close()
