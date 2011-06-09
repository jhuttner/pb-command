#!/usr/local/bin/python

import sys

MAX_COMMANDS = 20

long_term_store = '/home/jhuttner/pb-command.append_only'
buffer_store = '/home/jhuttner/pb-command.buffer'
history_store = '/home/jhuttner/pb-command.history'
interrupt = '/home/jhuttner/pb-command.interrupt_sent'

def store_interrupt(val):
  fobj = open(interrupt, 'w')
  fobj.write(str(int(val)))
  fobj.close()
  return val

def main(args):

  if len(args) and args[0] == '--stash':
    msg = 'Indexes to put into long-term store, space-delimited (default=0, x to quit): '
    store = history_store
    mode = 'stash'
  elif len(args) and args[0] == '--recall':
    msg = 'Indexes to put into copy buffer, space-delimited (default=0, x to quit): '
    store = long_term_store
    mode = 'recall'
  else:
    msg = 'Indexes to put into copy buffer, space-delimited (default=0, x to quit): '
    store = history_store
    mode = 'store'

  fobj = open(store)
  last_n = []
  while 1:
    curr_line = fobj.readline()
    if not curr_line:
      fobj.close()
      break
    else:
      if len(last_n) > MAX_COMMANDS + 1:
        last_n.pop(0)
      last_n.append(curr_line.strip())

  if store == history_store:
    # get rid of last 'store' call from the list
    last_n.pop()

    # get rid of spaces and leading number
    last_n = [i.strip().lstrip(' 0123456789') for i in last_n]

  print ''
  for index, cmd in enumerate(last_n):
    print str(len(last_n) - index - 1).rjust(2) + ':', cmd
  print ''
  
  ints = raw_input(msg)

  if store_interrupt(ints == 'x'):
    return

  indices = map(int, ints.split()) or [0]

  last_n.reverse() # so that user indices match up
  cmd_to_store = '\n'.join([last_n[i] for i in indices])

  if mode == 'recall' or mode == 'store':
    fobj = open(buffer_store, 'w')
    fobj.write(cmd_to_store)
    fobj.close()

  if mode == 'stash':
    fobj = open(long_term_store, 'a')
    fobj.write(cmd_to_store)
    fobj.write('\n')
    fobj.close()


if __name__ == "__main__":
  main(sys.argv[1:])
