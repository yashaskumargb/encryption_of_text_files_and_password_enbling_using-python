#Attention:Ensure pyminizip and time module is installed and imported in your code
# ensure your file to encrypted and protected is available in colab
pip install pyminizip
def read_file(file):
    '''this fucation reads contents of file 
    and convert it to string and returns it'''
    f=open(file,'r')
    str=f.read()
    return str
#-----------------------------------------------------------------------------
def encoding(str):
    '''this function takes input as string and gives output
       in the form od numerical string'''
    enc_str=''
    enc_dict={'!': '000', '@': '001', '#': '002', '$': '003', '%': '004', '^': '005', '&': '006', '*': '007', '(': '008', ')': '009', '_': '010',
             '-': '011', '+': '012', '=': '013', '~': '014', '`': '015', '{': '016', '}': '017', '[': '018', ']': '019', '|': '020',
             '||': '021', '"': '022', "'": '023', ':': '024', ';': '025', '?': '026', '/': '027', '>': '028', '<': '029', '.': '030',
             ',': '031', 'A': '032', 'B': '033', 'C': '034', 'D': '035', 'E': '036', 'F': '037', 'G': '038', 'H': '039', 'I': '040', 
             'J': '041', 'K': '042', 'L': '043', 'M': '044', 'N': '045', 'O': '046', 'P': '047', 'Q': '048', 'R': '049', 'S': '050',
             'T': '051', 'U': '052', 'V': '053', 'W': '054', 'X': '055', 'Y': '056', 'Z': '057', '\n': '058', '\t': '059',' ': '060',
             '0': '061', '1': '062', '2': '063', '3': '064', '4': '065', '5': '066', '6': '067', '7': '068', '8': '069', '9': '070',
             'a': '071', 'b': '072', 'c': '073', 'd': '074', 'e': '075', 'f': '076', 'g': '077', 'h': '078', 'i': '079', 'j': '080',
             'k': '081', 'l': '082', 'm': '083', 'n': '084', 'o': '085', 'p': '086', 'q': '087', 'r': '088', 's': '089', 't': '090',
             'u': '091', 'v': '092', 'w': '093', 'x': '094', 'y': '095', 'z': '096'}
    for char in str:
        x=enc_dict[char]
        enc_str+=x
    return enc_str
#-----------------------------------------------------------------------------
def dec_to_bin(str):
    '''this function take numerical string as input and gives output
    as string with corresponding BCD valued string'''
    new_str=''
    for i in str:
        i=int(i)
        dict={0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 
              5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001'}
        k=dict[i]
        new_str+=k
    return new_str
#-----------------------------------------------------------------------------
def str_to_list(str):
    ''' this function returns takes input as string
    converts it into a list with elements as string of length 20'''
    l=len(str)
    new_list=[]
    for k in range(0,l,100):
        new_string=str[0+k:100+k]+'\n'
        new_list.append(new_string)
    return new_list   
    
#-----------------------------------------------------------------------------
def list_to_file(list,Write_file):
    '''this function takes list as input containg lines of the file 
       gives the file with loaded content'''
    fr=open(Write_file,'w')
    for lines in list:
            fr.write(lines)
    return Write_file
#-----------------------------------------------------------------------------
import time as t
st=t.time_ns()   #start time
#-----------------------------------------------------------------------------
Read_file=input("enter the source  filename to be encoded     :")
Write_file=input("enter the destination  filename where encoded data to be dumped     :")

red_string=read_file(Read_file)
encoded_string=encoding(red_string)
bin_string=dec_to_bin(encoded_string)
encoded_list=str_to_list(bin_string)
encoded_filename=list_to_file(encoded_list,Write_file)
#-----------------------------------------------------------------------------
et=t.time_ns()    #end time
ttns=et-st        # taken taken for encoding in nanoseconds
ttss=ttns/(10**9) # taken taken for encoding in standard seconds

print("ENCODING SUCESS".center(77,"$"))
print("time taken for encoding  :%f seconds"%(ttss))
#-------------------------------------------------------------------------------
import pyminizip
file_to_be_protected=Write_file
password=input("enter the password     :")
passcode=input("Confirm your Password  :")
output_zip_file=input("enetr the zip name:")  
  
# compress level
com_lvl = 5
  
# compressing file
if(password==passcode):
      pyminizip.compress(file_to_be_protected, None, output_zip_file,password, com_lvl)
      print("sucess..password protection is enabled\n")
else:
  print("password not matching plese try once again  \n")
