# PB-command -- copy commands to your Mac buffer remotely.

## Usage

    01:~ jhuttner$ pbcommand // PUT RECENT COMMANDS TO MAC BUFFER 
    01:~ jhuttner$ pbcommand --stash // STASH COMMANDS TO FILE
    01:~ jhuttner$ pbcommand --recall // PUT STASHED COMMANDS TO BUFFER

You must have a reverse SSH tunnel setup from your remote box to your Mac.
Note: This is a rather specific setup for people that develop on a cloud from a Mac.

## Install
  
Take a look at the .py and .sh files in the repo.  Make sure you have your paths as you want them, and that the shebang lines are correct.

You will probably have to 'touch' the four files, or Python will bark.

Get your paths correct:

    01:pb-command(master) jhuttner$ pwd
    /home/jhuttner/git-repos/pb-command
    01:pb-command(master) jhuttner$ ln -s /home/jhuttner/git-repos/pb-command/pbcommand.sh /home/jhuttner/bin/pbcommand
    01:pb-command(master) jhuttner$ ln -s /home/jhuttner/git-repos/pb-command/do_pbcommand.py /home/jhuttner/bin/do_pbcommand.py
