"""
  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you CANNOT create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).

  For example, if you're given `coins = [1,2,5]`, the minimum amount of change 
  that you can't create is 4. If you're given no coins, the minimum amount of 
  change that you can't create is 1. 

  Sample Input:
    coins = [5,7,1,1,2,3,22]

  Sample Output:
    20
"""

MINIMUM_CHANGE = 1

def nonConstructibleChange_1(coins):
    # Write your code here.
    # maxChange = sum(coins)

    coins.sort()    
    if len(coins) != 0 and coins[0] == 1:
        currentSum = 1
        for idx, val in enumerate(coins):
            if val > currentSum + 1:
                return currentSum+1
            currentSum = (sum(coins[:idx+1]))

        return sum(coins) + 1          
    else:
        return MINIMUM_CHANGE

def nonConstructibleChange_2(coins):
    coins.sort()

    # print(coins)
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            # print("Returning: {}".format(currentChangeCreated + 1))
            return currentChangeCreated + 1
        currentChangeCreated += coin
        # print(currentChangeCreated)

    # print("Returning: {}".format(currentChangeCreated + 1))
    return currentChangeCreated + 1


def main():
    sampleCoins = [5,7,1,1,2,3,22]
    print(nonConstructibleChange_1(sampleCoins)) 
    print(nonConstructibleChange_2(sampleCoins)) 

if __name__ == "__main__":
    main()   