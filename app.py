from data.channel import Channel
C=Channel(
    'https://onlineattendence.art.blog',
    'stellerxotpsystem',
    'stellerx.incorrect'
)
def demostarate():
    global C
    print("""
   .--------------------.
   | 1 - new channel    |
   | 2 - send           |
   | 3 - recieve        |
   * -------------------*""")

    choice=int(input('Choice --- '))
    if choice == 1:
        print(C.NewChannel(input('Set Channel Name - ')))
        """
        if Channel.NewChannel(input('Set Channel Name - '))==True:
            print('New Channel Created Sucessfully ..')
        else:
            print('Error .. ')
        """
    elif choice == 2:
        if C.Send(input('Channel id : '),input('Data : ')) == True:
            print('Sent')
    elif choice == 3:
        data=C.Recieve(input('channel id : '))
        print(f'recieved [{data}]')

while True:
    demostarate()
    


