from main_TV import TV

# Initial testing: Sets fixed values for channel and volume on both TVs
def test_tv():

    #TV no. 1
    tv_1 = TV()
    tv_1.turn_on()
    tv_1.set_channel(30)
    tv_1.set_volume(3)

    #TV no. 2
    tv_2 = TV()
    tv_2.turn_on()
    tv_2.set_channel(3)
    tv_2.set_volume(2)

    return tv_1, tv_2

def tv_status():
    bold = "\033[1m"
    blue = "\033[34m"
    reset = "\033[0m"

    for i in range (3, 0, -1):
        print(f"{bold}TV testing...{i}")
    print(f"\n{blue}TV1's channel is {tv_1.get_channel()} and volume is {tv_1.get_volume()}")
    print(f"{blue}TV2's channel is {tv_2.get_channel()} and volume is {tv_2.get_volume()}{reset}")
    print(f"\n{bold}End initial testing...\n")

tv_1, tv_2 = test_tv()
tv_status()

# Further testing: allows the user to interactively test channel and volume adjustments (up/down) for both TVs
while True:
    user_response = input("Would you like to test the TV again? (yes/no): ").lower()
    if user_response == "yes":
        tv_choice = int(input("Which TV would you like to control? (1 or 2): "))

        if tv_choice == 1:
            tv = tv_1
            change = input("Change channel and volume (up/down): ").lower()

            if change == "up":
                tv_1.channel_up()
                tv_1.volume_up()
                print(f"\nTV1's Channel changed to {tv_1.get_channel()} and volume set to {tv_1.get_volume()}\n")

            elif change == "down":
                tv_1.channel_down()
                tv_1.volume_down()
                print(f"\nTV1's Channel changed to {tv_1.get_channel()} and volume set to {tv_1.get_volume()}\n")
            else: 
                print("\nInvalid command. Please type 'up' or 'down'.\n")
               
        elif tv_choice == 2:
            tv = tv_2
            change = input("Change channel and volume (up/down): ").lower()

            if change == "up":
                tv_2.channel_up()
                tv_2.volume_up()
                print(f"\nTV2's Channel changed to {tv_2.get_channel()} and volume set to {tv_2.get_volume()}\n")
                
            elif change == "down":
                tv_2.channel_down()
                tv_2.volume_down()
                print(f"\nTV2's Channel changed to {tv_2.get_channel()} and volume set to {tv_2.get_volume()}\n")
            else:
                print("\nInvalid TV selected. Try again.\n")

        else:
            print("\nInvalid TV selected. Try again.\n")

    elif user_response == "no":
        break