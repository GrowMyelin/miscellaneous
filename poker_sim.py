import random

highCards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
hands = ['High','1pair','2pair','3kind','4kind','Straight','Flush','FullHouse','StraightFlush','RoyalFlush']
suits = ['C','D','H','S']
def deal(players,hand_size):
    all_cards = [n+s for n in highCards for s in suits]
    hands = []
    for p in range(players):
        hand = []
        for i in range(hand_size):
            x = random.choice(all_cards)
            all_cards.remove(x)
            hand.append(x)
        hands.append(hand)
    return hands

def handResult(hand):
    
    results = {
        'High':False,
        '1pair':False,
        '2pair':False,
        '3kind':False,
        '4kind':False,
        'Straight':False,
        'Flush':False,
        'FullHouse':False,
        'StraightFlush':False,
        'RoyalFlush':False
    }
    resultDetails = {
        'High':[],
        'Pairs':[],
        '3kind':[],
        '4kind':[],
        'Straight':[],
        'Flush':[],
        'FullHouse':[],
        'StraightFlush':[],
        'RoyalFlush':[]
    }
    suitCount = {
        'C':0,
        'D':0,
        'H':0,
        'S':0
    }
    cardCount = {
        'A':0,
        'K':0,
        'Q':0,
        'J':0,
        'T':0,
        '9':0,
        '8':0,
        '7':0,
        '6':0,
        '5':0,
        '4':0,
        '3':0,
        '2':0
    }
    highCardIdx = highCards.index(hand[0][0])
    for card in hand:
        suitCount[card[1]] += 1
        cardCount[card[0]] += 1
        highCardIdx = min(highCardIdx,highCards.index(card[0])) 

    results['High'] = True
    resultDetails['High'] = highCards[highCardIdx]
    for keys,values in suitCount.items():
        if values == 5:
            results['Flush']=True
            resultDetails['Flush'] = keys
    straightCount = 0
    for keys,values in cardCount.items():
        straightCount += 1
        if values == 0:
            straightCount = 0
        if straightCount == 5:
            results['Straight'] = True
            resultDetails['Straight'].append(keys)
        if values == 2:
            resultDetails['Pairs'].append(keys)
            results['1pair']=True
        elif values == 3:
            resultDetails['3kind'].append(keys)
            results['3kind']=True
        elif values == 4:
            resultDetails['4kind'].append(keys)
            results['4kind']=True
    if len(resultDetails['Pairs']) > 1:
        results['2pair']=True
    if results['1pair']==True and results['3kind']==True:
        results['FullHouse']=True
        resultDetails['FullHouse'].append(resultDetails['3kind'][0])
        resultDetails['FullHouse'].append(resultDetails['Pairs'][0])
    if results['Straight']==True and results['Flush']==True:
        results['StraightFlush']=True
        resultDetails['StraightFlush'].append(resultDetails['Straight'][0])
        resultDetails['StraightFlush'].append(resultDetails['Flush'])
        if resultDetails['StraightFlush'][0]=='T':
            results['RoyalFlush']=True
            resultDetails['RoyalFlush'].append(resultDetails['Flush'][0])
    if results['RoyalFlush']:
        return ['RoyalFlush',resultDetails['RoyalFlush']]
    elif results['StraightFlush']:
        return ['StraightFlush',resultDetails['StraightFlush']]
    elif results['FullHouse']:
        return ['FullHouse',resultDetails['FullHouse']]
    elif results['Flush']:
        return ['Flush',resultDetails['Flush']]
    elif results['Straight']:
        return ['Straight',resultDetails['Straight']]
    elif results['4kind']:
        return ['4kind',resultDetails['4kind']]
    elif results['3kind']:
        return ['3kind',resultDetails['3kind']]
    elif results['2pair']:
        return ['2pair',resultDetails['Pairs']]
    elif results['1pair']:
        return ['1pair',resultDetails['Pairs'][0]]
    else:
        return ['High',resultDetails['High']]

def compareHands(hand1,hand2):
    hand1Result = handResult(hand1)
    hand1ResultIdx = hands.index(hand1Result[0])
    hand2Result = handResult(hand2)
    hand2ResultIdx = hands.index(hand2Result[0])
    if hand1ResultIdx > hand2ResultIdx:
        return 'Hand1 wins!'
    elif hand1ResultIdx < hand2ResultIdx:
        return 'Hand2 wins!'
    elif hand1ResultIdx == hand2ResultIdx:
        if hand1Result[0] == 'Flush':
            hand1Suit = hand1Result[1]
            hand2Suit = hand2Result[1]
            hand1SuitIdx = suits.index(hand1Suit)
            hand2SuitIdx = suits.index(hand2Suit)
            if hand1SuitIdx > hand2SuitIdx:
                return 'Hand1 wins!'
            elif hand1SuitIdx < hand2SuitIdx:
                return 'Hand2 wins!'
            else:
                return 'Tie'
        else:
            if len(hand1Result[1]) < 2:
                hand1Val = hand1Result[1]
            else:
                hand1Val = hand1Result[1][0]
            hand1ValIdx = highCards.index(hand1Val)

            if len(hand2Result[1]) < 2:
                hand2Val = hand2Result[1]
            else:
                hand2Val = hand2Result[1][0]
            hand2ValIdx = highCards.index(hand2Val)
            if hand1ValIdx < hand2ValIdx:
                return 'Hand1 wins!'
            elif hand1ValIdx > hand2ValIdx:
                return 'Hand2 wins!'
            else:
                print(f"1 : {hand1Result} \n 2: {hand2Result}")
                return 'Tie'
    else:
        return 'Unclear'

def simulate_hands():
    dealt_hands = deal(2,7)
    for h in dealt_hands:
        print(f"{h} : {handResult(h)}")
    return compareHands(dealt_hands[0],dealt_hands[1])

print(simulate_hands())
