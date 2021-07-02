import argparse
import string

# Argparse setup 
Parser = argparse.ArgumentParser()
Parser.add_argument("-m",help="pass the Message to run through the rotational cipher",nargs="+",required=True)
Parser.add_argument("-N",help="Pass the N-rotational value [Default is 13]",default=13,type=int)
Parser.add_argument("-B",help="Switch for bruteforce the N-val",action='store_true')

# Move a argparse value into a stored variable
Args = Parser.parse_args()
Message = Args.m
N = Args.N

class Color:
    'Class for Colors to be used in Execution'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

    QuestionColor = BOLD+YELLOW
    ErrorColor = RED+BOLD
    InfoColor = CYAN 
    SuccessColor = GREEN

class Notify():
   'Managed what type of message is sent'

   def Error(Message):
      'Error Messages'
      print(f"{Color.ErrorColor}[!] - {Message}{Color.RESET}")

   def Info(Message):
      'Infomation Messages'
      print(f"{Color.InfoColor}[*] - {Message}{Color.RESET}")

   def Success(Message):
      'Success Messages'
      print(f"{Color.SuccessColor}[$] - {Message}{Color.RESET}")

   def Question(Message):
      'Get infomation from user'
      input(f"{Color.QuestionColor}[?] - {Message}{Color.RESET}")


def GetLetter(List,char,key):
   x = (List.index(char) - key) % 26
   Letter = List[x]
   return(Letter)


class Decrypt:
   'Class for decrypting rotational ciphers'
   def __init__(self,Message,N):
      'init message and N-value'
      self.Message = Message
      self.N = N % 26

   def Bruteforce(self):
      TranslatedList = []
      for key in range(0,26): 
         Translated = ""
         for char in str(Message):

            if char.isalpha():
               if char.isupper():
                  Letter = GetLetter(string.ascii_uppercase,char,key)
                  Translated += Letter
               elif char.islower():
                  Letter = GetLetter(string.ascii_lowercase,char,key)
                  Translated += Letter
            else:
               Translated += char    

         TranslatedList.append([f"{key}",f"{Translated}"]) 
      for _ in TranslatedList:
         key = _[0].rjust(2)
         value = str(_[1])
         Notify.Info(f"{key} : {value}")

   def Standard(self):
      Translated = ""
      key = N
      for char in str(Message):
         if char.isalpha():
            if char.isupper():
               Letter = GetLetter(string.ascii_uppercase,char,key)
               Translated += Letter
            elif char.islower():
               Letter = GetLetter(string.ascii_lowercase,char,key)
               Translated += Letter
         else:
            Translated += char
      Notify.Info(f"{N} : {Translated}")


def Main(Message,N):
   if Message:
      Message = " ".join(Message)
   D = Decrypt(Message,N)
   if Args.B:
      D.Bruteforce()
   else:
      D.Standard()


if __name__ == "__main__":
      Main(Message,N)