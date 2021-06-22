import argparse
import string

# Argparse setup 
Parser = argparse.ArgumentParser()
Parser.add_argument("-m",help="pass the Message to run through the rotational cipher",nargs="+",required=True)
Parser.add_argument("-N",help="Pass the N-rotational value [Default is 13]",default=13)
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

class Decrypt:
   def __init__(self,Message,N):
      self.Message = Message
      self.N = N

   def Bruteforce(self):
      TranslatedList = []
      for key in range(0,25): 
         for character in Message:
            Translated = ""

            if character.isalpha():
               num = ord(character)
               num += key
               if num < 0:
                  num = num + 26
               Translated += string.ascii_lowercase[num]
            else:
               Translated += character    

            TranslatedList.append([f"{key}",f"{Translated}"]) 
      for _ in TranslatedList:
         Notify.Info(f"{_[0].rjust(3)} : {_[1]}")

   def Standard(self):
      print("x")


def Main(Message,N):
   D = Decrypt(Message,N)
   if Message:
      Message = " ".join(Message)
   if Args.B:
      D.Bruteforce()
   else:
      D.Standard()


if __name__ == "__main__":
      Main(Message,N)