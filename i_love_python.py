reason_list = ["simple","easy to read","powerful","open-sourse","checkiO-ble","gifted with modules","same year old as me"]
adv_list = ["surprisingly","utterly","incredibly","beautifully","heart warmingly","happily","solemnly","justly","kindly","cheerfully","always"]

def i_love_python(retweets = 0):
    from random import randint
    if retweets ==0: return "I love Python!"
    else:
        reason = randint(0,6)
        adv = randint(0,10)
        for retweets in range(retweets):
            if reason < 6: reason +=1
            else: reason = 0
            if adv < 10: adv += 1
            else: adv = 0
            print( "I love Python! Because it is " + adv_list[adv] + " " + reason_list[reason] +"!")
        print("In short...")
        print("I love Python!")
        return "I love Python!"
            
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
