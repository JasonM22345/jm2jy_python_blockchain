"""
Jason Mensah-Homiah
University of Virginia, Wise

-- Check Readme


works on python 3

Execution instructions:
        execution command:      python3 Ass4.py


NB: The indexing of the number of blocks begins from 1

    To make handling of files easier, this program generates all block files into a folder
        named "jm2jy_Blockchain"

    Program loops until the program exits

    Folder is emptied each time the program is run.

    "Chain is invalid at block n" means the hash of block n-1 is different from the one stored in block n
"""
import random
import string
import datetime
import base64
import os
import  glob
import sys
from hashlib import sha256


BlockLength = 0
NonceLength = 6
FolderName = "jm2jy_Blockchain"
curr_block_nonce = ""
target = ""
has_initial = False

def generate_nonce(): #generates a nonce that meets the target
    def find_nonce():
        global BlockLength
        block = BlockLength #BlockLength-1 if BlockLength > 0 else BlockLength
        file_dir = str(block) + ".txt"
        temp_file_dir = str(block) + "_temp.txt"
        nonce_start = 0
        found = False


        target_hex = ""
        for j in target: #convert target to hex
            target_hex += str(hex(ord(j)))[2:]
        #print("Target Hex = " + str(target_hex))  #''' Intentionally left for you to test hex generated'''

        #data_to_be_hashed = open(FolderName +"/"+ file_dir, "r", encoding='utf-8').readlines()
        nonce_temp = nonce_start #variable to hold the nonce value as its incremented
        ########

        #remove_nonce(block)

        #########

        data_to_be_hashed = open(FolderName + "/" + file_dir, "r", encoding='utf-8').readlines()

        print("\t Calculating For the Nonce Value")
        while found == False:
            x = str(data_to_be_hashed) + "\n" + str(nonce_temp)
            hashed_tmp = sha256(x.encode('utf-8')).hexdigest()
            th_lenght = len(target_hex) #lenght of the hex of the target
            if str(hashed_tmp)[:th_lenght] == str(target_hex):
                #print("\t Nonce Value Found")  ''' These three lines were left for you to test....'''
                print("hash w n: " + str(hashed_tmp))
                print("nonce :  " + str(nonce_temp))
                found = True
                break
            #print("tmp hash: " + str(hashed_tmp))
            nonce_temp += 1


        return str(nonce_temp)

    nonce_gen = find_nonce() #nonce found
    return nonce_gen
    #return ''.join([str(random.randint(0,9)) for i in range(NonceLength)])

def empty_directory(): #empties blockchain folder, typically when the code is re-run
    files = glob.glob(FolderName + "/**/*.txt", recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("\t\t\t => Directory clearing error: " + e)

def create_folder(): #creates The folder to store the blockchain files
    if os.path.exists(FolderName):
        empty_directory()
    try:
        if not os.path.exists(FolderName):
            os.makedirs(FolderName)
    except OSError:
        print("\t\t\t => Directory Creation Error")

def create_initial_block(): #creates the genesis block
    global BlockLength
    BlockLength = 0
    dT_stamp_creation = str(datetime.datetime.now())
    initial_output_file = open(FolderName +"/0.txt", "w")
    temp_initial_output_file = open(FolderName + "/0_temp.txt", "w")
    transaction = str(datetime.datetime.now())

    initial_output_file.write(str(BlockLength) +"\n")
    initial_output_file.write(dT_stamp_creation +"\n")
    initial_output_file.write(transaction +"\n")

    temp_initial_output_file.write(str(BlockLength) +"\n")
    temp_initial_output_file.write(dT_stamp_creation +"\n")
    temp_initial_output_file.write(transaction +"\n")

    nonce_temporary = 6969
    initial_output_file.write(str(nonce_temporary) + "\n")
    temp_initial_output_file.write(str(nonce_temporary) + "\n")

    nonce = generate_nonce()
    #initial_output_file.write(str(nonce) +"\n")

#######

def remove_nonce(file_dir):
    #... Was in add ....
    #file_dir = str(blocknumber) + ".txt"
    inputfile4 = open(FolderName + "/" + file_dir, "r")

    input_data = inputfile4.read().splitlines()
    count = 0
    global has_initial

    def count_lines(): #counts lines to determine the index of the previous nonce (always last)
        nonlocal  count
        with open(r""+ FolderName + "/" + file_dir, "r") as fp:
            for x, line in enumerate(fp):
                nonlocal count
                count = x
                pass

    count_lines()

    print("count: " + str(count) + "\tNonce: " + str(input_data[count]))

    def rem_nonce(): # removes previous nonce
        os.remove(FolderName + "/" + file_dir)
        outputfile2 = open(FolderName + "/" + file_dir, "w")
        input_data.remove(input_data[count])
        for line in input_data:
            outputfile2.write(str(line) + "\n")

    rem_nonce()





####
def add_transaction(blocknumber): #adds a transaction

    file_dir = str(blocknumber) + ".txt"
    remove_nonce(file_dir)
    outputfile2 = open(FolderName + "/" + file_dir, "a")
    transaction = str(datetime.datetime.now())
    outputfile2.write(transaction + "\n")
    Nonce = generate_nonce()
    outputfile2.write(Nonce + "\n") #adds new nonce


    print ("\t\t\t\t\t=> Transaction Added")



def create_hash_block(): #creates a new hash block
        global BlockLength
        BlockLength += 1
        file_dir = str(BlockLength-1) + ".txt"
        output_file = str(BlockLength) + ".txt"
        inputfile2 = open(FolderName +"/" + file_dir, "r")
        outputfile = open(FolderName +"/" + output_file, "w")

        hashofpreviousblock = sha256((str(inputfile2.read())).encode()).hexdigest()
        DTstamp_creation = str(datetime.datetime.now())
        Transaction = str(datetime.datetime.now())
        Nonce = generate_nonce()

        outputfile.write(str(BlockLength) +"\n")
        outputfile.write(DTstamp_creation +"\n")
        outputfile.write(hashofpreviousblock +"\n")
        outputfile.write(Transaction +"\n")
        outputfile.write(Nonce +"\n")

        print("\n\t\t\t\t\t=> BLOCK SUCCESSFULLY ADDED")

def validate_chain(): #validates chain by comparing the hash stored to the actual hash of the previous block
    isChainValid = False
    global BlockLength

    def setvalidtrue():
        nonlocal isChainValid
        isChainValid = True

    def setvalidfalse():
        nonlocal isChainValid
        isChainValid = False

    for i in range(1, BlockLength+1):
        prev_dir = str(i-1) + ".txt"
        current_dir = str(i) + ".txt"
        prev = open(FolderName +"/" + prev_dir, "r")
        current = open(FolderName +"/" + current_dir, "r")

        current_content = current.readlines()
        sha_loc = 2  #location of the sha hash in the block
        current_sha256_hash =  str(current_content[sha_loc].strip('\n')) #stripped to remove '\n' originally added
        hash_of_prev = str(sha256((str(prev.read())).encode()).hexdigest())

        '''************ The two lines below were added for you to easy verify the results. Uncomment to use.'''
        #print("Hash of previous stored in current block (C): " + current_sha256_hash)
        #print("Actual Hash of previous of previous block (P) " + hash_of_prev)

        if not current_sha256_hash  == hash_of_prev:
            print("\n\t\t\t\t\t=> CHAIN IS INVALID AT BLOCK " + str(i))
            setvalidfalse()
            break
        else:
            setvalidtrue()

    if isChainValid:
        print("\n\t\t\t\t\t=> CHAIN IS VALID")




def simple_menu(): #Menu that provides the user with the required options
    completed = False
    create_initial_block()  # Create initial block
    while not completed:
        print("\nSELECT ONE OF THE FOLLOWING OPTIONS")
        print("\t\t1. Create New Block")
        print("\t\t2. Add Transaction")
        print("\t\t3. Validate Chain")
        print("\t\t4. Exit")
        print("\n")

        valid = False
        while not valid: #Ensures user enters a valid selection
            try:
                inp = int(input("Enter your selection: "))
                #if 0 > int(inp) <= 4:
                valid = True
                    #break
                #else: print("Invalid selection, try again")

            except ValueError:
                print("Invalid input, try again")

        if inp == 1:
            create_hash_block()
        elif inp == 2:
            add_transaction(BlockLength)
        elif inp == 3:
            validate_chain()
        elif inp == 4:
            print("Exiting")
            completed = True
            quit()
        else:
            print("Error 69420")



def main():
    global target
    if len(sys.argv) < 2:
        print("\t\t => Target was not provided.")
        targ = input("Enter the target now: ")
    else:
        targ = sys.argv[1]
    target = targ

    #print("Target: " + str(target))
    create_folder()
    simple_menu()
    print("Done")


if __name__ == "__main__":
    main()
