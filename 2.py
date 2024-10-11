#function is defined for checking anagram
def anagram_check():
   #taking inputs and converting it into lowercase and striping of spaces
   str1=input("str1 = ").lower().strip()
   str2=input("str2 = ").lower().strip()
   
   # if length of two strings are equal will continue to next operations
   if len(str1)==len(str2):
      #string is converted into list
      character_list1=list(str1)
      character_list2=list(str2)
      #Arranging the charactors into  ascending order
      character_list1.sort()
      character_list2.sort()
      #if two list are equal 
      if character_list2==character_list1:
       return True
      else:
        return False  
   else:
    return False
   
 #output details  
result=anagram_check()
if result==True:
  print("The two strings are anagrams")
elif result==False:
  print("The two strings are not anagrams")    