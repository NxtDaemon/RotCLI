import argparse
import string
import sys
import re
import string

# Argparse setup
Parser = argparse.ArgumentParser()
Parser.add_argument(
    "-M", help="Pass the Message to run through the rotational cipher", required=True, type=str)
Parser.add_argument(
    "-N", help="Pass the N-rotational value [Default is 13]", default=13,  type=int)
Parser.add_argument(
    "-B", help="Switch for bruteforce the N-val", action='store_true')
Parser.add_argument(
    "-L", help="Switch for Letter-Goodness", action='store_true')

# Move a argparse value into a stored variable
Args = Parser.parse_args()
Message = Args.M
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

    def LG_KeyOutput(LG_Dict):
        Order = sorted(list(LG_Dict.keys()), reverse=True)
        Notify.Info("Printing Message with Highest Letter Goodness\n")
        AcceptList = ["YES", "Y"]
        c = 0
        while True:
            Top = LG_Dict[Order[c]]
            TopKey = Top[0]
            TopValue = Top[1]
            Notify.KeyOutput(TopKey, TopValue, Order[c])
            Res = Notify.Question("Do you Want to Print the Next Value?")
            if Res.upper() not in AcceptList:
                Notify.Success("Hope you Got your Result ／人◕ __ ◕人＼")
                break
            c += 1

    def KeyOutput(Key, Message, LG=""):
        'Key Output'
        if LG:
            LG = f"[{LG}]"
        Message = Message.replace("\n", " ").replace("\r", " ")
        Message = re.findall(r"[\s\S]{0,110}", Message)
        print(f"{Color.YELLOW}[🔑] -> {Key} {LG}{Color.RESET}")
        for _ in Message:
            print(" "*8 + _)

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
        tmp = input(f"{Color.QuestionColor}[?] - {Message}{Color.RESET}")
        print()
        return(tmp)


def GetLetter(List, char, key):
    x = (List.index(char) + key) % 26
    Letter = List[x]
    return(Letter)


class Decrypt:
    'Class for decrypting rotational ciphers'

    def __init__(self, Message, N, LGS):
        'init message and N-value'
        self.Message = Message
        self.N = N % 26
        self.LetterGoodnessSwitch = LGS

    def Bruteforce(self):
        'Bruteforce the key for Args.Message'
        TranslatedList = []
        LetterGoodness_TranslatedDict = {}
        for key in range(0, 26):
            Translated = ""
            for char in str(self.Message):
                if char.isalpha():
                    if char.isupper():
                        Letter = GetLetter(string.ascii_uppercase, char, key)
                        Translated += Letter
                    elif char.islower():
                        Letter = GetLetter(string.ascii_lowercase, char, key)
                        Translated += Letter
                else:
                    Translated += char
            TranslatedList.append([f"{key}", f"{Translated}"])
        for _ in TranslatedList:
            Key = _[0].rjust(2)
            Message = str(_[1])
            if self.LetterGoodnessSwitch:
                LetterGoodness = self.LetterGoodnessEvaluation(Message)
                LetterGoodness_TranslatedDict.update({LetterGoodness: _})
            else:
                Notify.KeyOutput(Key, Message)

        if self.LetterGoodnessSwitch:
            Notify.LG_KeyOutput(LetterGoodness_TranslatedDict)

    def Standard(self):
        'Perform Caesar cipher of N=K or N=13 as default on Args.Message'
        Translated = ""
        key = N

        for char in str(Message):
            if char.isalpha():
                if char.isupper():
                    Letter = GetLetter(string.ascii_uppercase, char, key)
                    Translated += Letter
                elif char.islower():
                    Letter = GetLetter(string.ascii_lowercase, char, key)
                    Translated += Letter
            else:
                Translated += char
        if self.LetterGoodnessSwitch:
            LG = self.LetterGoodnessEvaluation(Translated)
        else:
            LG = None

        Notify.KeyOutput(N, Translated, LG)

    def LetterGoodnessEvaluation(self, Message):
        'Calculate English Letter Goodness for Message'
        LetterGoodness_Score = 0
        LetterGoodnessDict = dict(zip(string.ascii_uppercase,
                                      [.0817, .0149, .0278, .0425, .1270, .0223, .0202,
                                       .0609, .0697, .0015, .0077, .0402, .0241, .0675,
                                       .0751, .0193, .0009, .0599, .0633, .0906, .0276,
                                       .0098, .0236, .0015, .0197, .0007]))
        for char in Message:
            if char.upper() in string.ascii_uppercase:
                LetterGoodness_Score += LetterGoodnessDict[char.upper()]

        return(LetterGoodness_Score)


def Main(Message, N):
    D = Decrypt(Message, N, LGS=Args.L)
    if Args.B:
        D.Bruteforce()
    else:
        D.Standard()


if __name__ == "__main__":
    Main(Message, N)
