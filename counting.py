import sys

coins = [1,5,10,25]

    
def partitions(n,k):
   """
    pre 0<k<=n, n>0
    post return the number of ways k partitions 
          can be formed out of n distinct elements
   """
   if (n == 0 or k == 0 or k > n): 
        return 0
   if (k == 1 or k == n):
        return 1
    # S(n+1, k) = k*S(n, k) + S(n, k-1) 
   return (k * partitions(n - 1, k) + partitions(n - 1, k - 1)) 
         
   	
   # if k==n or k==1 :
   #  there is only one way to form partitions
   # else :
   # select an element a, and
   #   either
   #     form k partitions with the rest of the elements
   #     and let a join one of these k groups
   #   or
   #     let a form its own partition, and
   #     form k-1 partitions with the rest


def count(S, m, n ): 
  
    # If n is 0 then there is 1 
    # solution (do not include any coin) 
    if (n == 0): 
        return 1
  
    # If n is less than 0 then no 
    # solution exists 
    if (n < 0): 
        return 0; 
  
    # If there are no coins and n 
    # is greater than 0, then no 
    # solution exist 
    if (m <=0 and n >= 1): 
        return 0
  
    # count is sum of solutions (i)  
    # including S[m-1] (ii) excluding S[m-1] 
    return count( S, m - 1, n ) + count( S, m, n-S[m-1])
def mkCh(a, c):
   """
    given coin set {1,5,10,25} count how many ways we can pay amount a,
    c indicates which coin is considered first.  c starts as the index
    of the last coin value (len(coins)-1)
   """
   return count(coins, 4, a)
   """
   if( c == 0):
      return 1
   else:
      amount = a%coins[c]
      if(a/coins[c] > 1):
         num = int(a/coins[c])
         
         print('a', a, 'n', num)
         return mkCh(amount,c-1) + num * mkCh(coins[c], c-1) + num
      else:
         print('b', a, 'c', coins[c])
         return 1 + mkCh(amount,c-1)
   """

if __name__ == "__main__":
  # partititions
  d = len(sys.argv)>3
  n = int(sys.argv[1])
  k = int(sys.argv[2])
  #print(combination(10,8))
  p = partitions(n,k)
  print("n:",n,"k:",k, "partitions:",p)
  
  # make change
  c = len(coins)-1
  a = 10*n+k
  ways = mkCh(a,c)
  print("amount:", a, "coins:", coins, "ways:", ways)


