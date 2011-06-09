#/!bin/bash

function check_interrupt {
	val=`cat /home/jhuttner/pb-command.interrupt_sent`
	if [[ "$val" = "1" ]]; then
		exit 0
	fi
}

if [[ "$1" = "--stash" ]]; then
	history > /home/jhuttner/pb-command.history
	do_pbcommand.py --stash
	check_interrupt
	echo
	echo 'Complete!'
	echo
	echo "List of stashed commands:"
	cat /home/jhuttner/pb-command.append_only
	echo 
	echo

elif [[ "$1" = "--recall" ]]; then
	do_pbcommand.py --recall
	check_interrupt
	cat /home/jhuttner/pb-command.buffer | pbcopy
	echo "Sent to buffer!"

else
	history > /home/jhuttner/pb-command.history
	do_pbcommand.py
	check_interrupt
	cat /home/jhuttner/pb-command.buffer | pbcopy
	echo "Sent to buffer!"
fi
