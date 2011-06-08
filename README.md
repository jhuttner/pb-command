# PB-command -- copy recent commands to your Mac buffer remotely.

## Purpose

Look at a list of your recent commands, select one, and then hit enter.  It will go into your Mac's copy
buffer provided that you have a reverse SSH tunnel setup from your remote box to your Mac.

Yeah yeah, I know this is a rather specific setup for people that develop on a cloud from a Mac.  Sorry.

## Make sure to get the pathing correct.  I have /home/jhuttner/bin in my path.

    01:pb-command(master) jhuttner$ pwd
    /home/jhuttner/git-repos/pb-command
    01:pb-command(master) jhuttner$ ln -s /home/jhuttner/git-repos/pb-command/store.sh /home/jhuttner/bin/store.sh
    01:pb-command(master) jhuttner$ ln -s /home/jhuttner/git-repos/pb-command/store.py /home/jhuttner/bin/store.py
