from profanity_check import predict


def check_abuse(text):
    offensive = False
    while not offensive:
    #text = input("Please kindly enter the text: \n")
        result = predict([text])
        print(result)
        if result == [0]:
            print("Text is okay")
            return "Okay"
            offensive = True
        else:
            return "Bad"
            print("The text is offensive")
##            
##while not offensive:
##    text = input("Please kindly enter the text: \n")
##    result = predict([text])
##    print(result)
##    if result == [0]:
##        print("Text is okay")
##        offensive = True
##    else:
##        print("The text is offensive")
    
