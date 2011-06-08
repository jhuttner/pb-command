#!/usr/local/bin/python

MAX_COMMANDS = 10

def main():
  fobj = open('/tmp/store')
  last_n = []
  while 1:
    curr_line = fobj.readline()
    if not curr_line:
      fobj.close()
      break
    else:
      if len(last_n) > MAX_COMMANDS + 1:
        last_n.pop()
      last_n.insert(0, curr_line)


  # get rid of spaces and leading number
  last_n = [i.strip().lstrip(' 0123456789') for i in last_n]

  # reverse so that most recent prints out on bottom
  last_n.reverse()

  # get rid of last 'store' call from the list
  last_n.pop()

  print ''
  for index, cmd in enumerate(last_n):
    print str(len(last_n) - index - 1).rjust(2),'--', cmd
  print ''
  
  which = raw_input('Which index (default=0)? ')
  which = int(which or 0)

  # reverse again so index user enters matches the list
  last_n.reverse()
  cmd_to_store = last_n[which]

  # store the command
  fobj = open('/tmp/store2', 'w')
  fobj.write(cmd_to_store)
  fobj.close()

if __name__ == "__main__":
  main()
