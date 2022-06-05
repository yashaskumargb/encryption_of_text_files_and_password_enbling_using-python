#Attention:Ensure pyminizip and time module is installed and imported in your code
# ensure your file to encrypted and protected is available in colab
pip install pyminizip
import os as o
import re
import random as r
def path_adder(ftbe_p,file_to_be_encoded,ftbd_p,file_to_be_dumped):
    '''this adds paths to file from where it tobe fetched.
    and to where it has to be dumped'''
    print("1.file name   :{}".format(file_to_be_encoded))
    pattern=r"\w+."
    folder_name=re.findall(pattern,file_to_be_dumped)
    folder_name=folder_name[0]
    folder_name=folder_name[0:(len(folder_name)-1)]
    print("2.folder name   :{}".format(folder_name))
    
    try:
        final_path_enc=ftbe_p+"\\"+file_to_be_encoded
        final_path_dump=ftbd_p+"\\"+folder_name+"\\"+file_to_be_dumped
        #this f_temp will holds the path from drive name to until folder only
        f_temp=ftbd_p+"\\"+folder_name
    except:
        msg="invalid file path"
        return msg
    o.mkdir(f_temp)
    return final_path_enc,final_path_dump
def read_file(file):
    '''this fucation reads contents of file 
    and convert it to string and returns it'''
    try:
        f=open(file,'r')
        str=f.read()
        return str
    except:
        msg="invalid file path"
        return msg
   #-----------------------------------------------------------------------------

def random_list():

    DS= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    
    LC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 
         'q','r', 's', 't', 'u', 'v', 'w', 'x', 
         'y','z']
     
    
    UC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
          'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q',
          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
          'Z']
    
    SM = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
          '_', '-', '+', '=', '~', '`', '{', '}', '[', ']',
          '|', '||', '"', '\'',':',';', '?', '/', '>', '<',
          '.', ',']
    
    ES=['\n','\t',' ']
    Main=[DS,SM,UC,LC,ES]
   
    cl=[]#cl means combined list
    enc_str_key=""
    for i in range(1,5+1,1):
        dummy_var=r.choice(Main)
        a=dummy_var[0]
        if(a=="\n"):
            a="e"
        enc_str_key=enc_str_key+a
        
        Main.remove(dummy_var)
        '''
        if(dummy_var=="\n"):
            dummy_var="e"
        '''
        cl=cl+dummy_var
    enc_str_key=list(enc_str_key)

    ref_dict1={"a":"0","A":"1","!":"2","e":"3","0":"4"}
    new_key="" 
    for j in enc_str_key:
         sx=ref_dict1[j]
         new_key=new_key+sx
    #this new key is encrypted form forenc_str_key 
    return new_key, cl
#------------------------------------------------------------------------------
def dict_gen(my_list):
    num=[ '00', '01','02','03','04','05','06','07','08','09','10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                 '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                 '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
                 '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
                 '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
                 '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
                 '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
                 '91', '92', '93', '94', '95', '96', '97']
    dictor_enc={} 
    for char in my_list:
        for numb in num:
            dictor_enc[char]=numb
            num.remove(numb)
            break
    return dictor_enc
#------------------------------------------------------------------------------
def encoding(key_to_be_encoded,str,enc_dict):
    '''this function takes input as string and gives output
       in the form od numerical string'''
    enc_str=''
    for char in str:
        try:
            x=enc_dict[char]
            enc_str+=x
        except:
            pass
    
    enc_str=key_to_be_encoded+enc_str
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
    for k in range(0,l,189):
        new_string=str[0+k:189+k]+'\n'
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
#read the file names
#Read_file=input("enter the source  filename to be encoded     :")
#Write_file=input("enter the destination  filename where encoded data to be dumped     :")
Read_file=input("enter the source  filename to be encoded     :")
Write_file=input("enter the destination  filename where encoded data to be dumped     :")
rf_path=input("enter the path of source file  :")
wf_path=input("enter the address path where file to be dumped  :")
#------------------------------------------------------------------------------
import time as t
st=t.time()#start time
#-----------------------------------------------------------------------------
#add the  apths to file names
Read_file_path,Write_file_path = path_adder(rf_path,Read_file,wf_path,Write_file)
print("dest paath   :{}".format(Write_file_path))
#read the data out of the file
red_string=read_file(Read_file_path)
#genrate the encoded dict
encoding_key,encoded_list=random_list()
print("encoding key  :",encoding_key)
encoded_dict= dict_gen(encoded_list)
#print(encoded_dict)
#encode the original data with the new data
encoded_string=encoding(encoding_key,red_string,encoded_dict)
#print("encoded string :",encoded_string,"lentgh :",len(encoded_string))
#convert  bcd to binary
bin_string=dec_to_bin(encoded_string)
print("length of binary string  :",len(bin_string))
#convert to list
encoded_list=str_to_list(bin_string)
#write the enoced data to new file
encoded_filename=list_to_file(encoded_list,Write_file_path)
#-----------------------------------------------------------------------------
et=t.time()#end time
ttns=et-st        # taken taken for encoding in seconds
#------------------------------------------------------------------------------
print("ENCODING SUCESS".center(77,"$"))
print("time taken for encoding  :%f seconds"%(ttns))
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
