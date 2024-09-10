def home_logo():
    print("""
        ####   ##     ##      ###        #####      #######     ####### 
         ##    ##     ##     ## ##      ##   ##    ##     ##   ##     ##
         ##    ##     ##    ##   ##    ##     ##   ##     ##   ##     ##
         ##    #########   ##     ##   ##     ##    #######     ########
         ##    ##     ##   #########   ##     ##   ##     ##          ##
         ##    ##     ##   ##     ##    ##   ##    ##     ##   ##     ##
        ####   ##     ##   ##     ##     #####      #######     #######
    
                                        Created by Arul Prakash.R
    """)

def Main():
    home_logo()
    print("1\tStart Server\n2\tConnect with server")
    select = int(input("Select ::: "))
    if select == 1:
        import server
    elif select == 2:
        import client
    else:
        print("Please choose 1 or 2")

if __name__ == "__main__":
    Main()
