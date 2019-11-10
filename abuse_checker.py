from profanity_check import predict

offensive = False
while not offensive:
    text = input("Please kindly enter the text: \n")
    result = predict([text])
    print(result)
    if result == [0]:
        print("Text is okay")
        offensive = True
    else:
        print("The text is offensive")
    
