import argparse
import re

print('''\033[1;31m 
There are several reasons why you want to change the MAC address of your device. 
        Let's go through them one by one:
            1) Increasing anonymity
            2) Impersonation of other devices
            3) Bypass filters
And this will help you...
     __  __    _    ____           __  __    _    ____  _  __
    |  \/  |  / \  / ___|         |  \/  |  / \  / ___|| |/ /
    | |\/| | / _ \| |      _____  | |\/| | / _ \ \___ \| ' / 
    | |  | |/ ___ \ |___  |_____| | |  | |/ ___ \ ___) | . \ 
    |_|  |_/_/   \_\____|         |_|  |_/_/   \_\____/|_|\_\ 

                     Creator: Instructor
    ''')


def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--interface', dest='interface', help='Interface name whose MAC is to be changed')
  parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC Address')
  options = parser.parse_args()

  # Check for errors i.e if the user does not specify the interface or new MAC
  # Quit the program if any one of the argument is missing
  # While quitting also display an error message

  if not options.interface:
    # Code to handle if interface is not specified
    parser.error('[-] Please specify an interface in the arguments, use --help for more info.')

  elif not options.new_mac:
    # Code to handle if new MAC Address is not specified
    parser.error('[-] Please specify a new MAC Address, use --help for more info.')

  return options


def change_mac(interface, new_mac):
  # Cecking if the new MAC Address has a length of 17 or not. If not print an error and quit, else change the MAC Address
  if len(new_mac) != 17:
    print('[-] Please enter a valid MAC Address')
    quit()

  print('\n\033[1;32m[+]\033[1;32m\033[1;35m Изменение MAC-адреса на', new_mac)
  sub.call(['sudo', 'ifconfig', interface, 'down'])
  sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
  sub.call(['sudo', 'ifconfig', interface, 'up'])


def get_current_mac(interface):
  output = sub.check_output(['ifconfig', interface], universal_newlines=True)
  search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
  if search_mac:
    return search_mac.group(0)
  else:
    print('[-] Could not read the MAC Address')


command_args = get_args()

prev_mac = get_current_mac(command_args.interface)
print('\n\033[1;32m[+]\033[1;32m\033[1;35m MAC-адрес до изменения -> {}\033[1;37m'.format(prev_mac))

change_mac(command_args.interface, command_args.new_mac)

changed_mac = get_current_mac(command_args.interface)
print('\n\033[1;32m[+]\033[1;32m\033[1;35m MAC-адрес после изменения -> {}'.format(changed_mac))

# Checking if the current MAC is same as the what the user intended to be
# If not then display an error
# Else display a message that says MAC Changed successfully
if changed_mac == command_args.new_mac:
  print('\n\033[1;32m[+]\033[1;32m\033[1;32m MAC-адрес был успешно изменен с {} на {}'.format(prev_mac, changed_mac))
else:
  print('\n[-] Could not change the MAC Address')
