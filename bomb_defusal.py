#user shivamzaz
t=int(raw_input())
while(t):
    a,b,c,d,e=map(int,raw_input().split())
    if((b==d)and(c==e)):
        print("Counter Terrorists Win !")
    else:
        #print("JK")
        cnt=0
        g=0
        i=0
        p=d+e
        while(1):
             if(b+c==p):
              break;
             b=b+1
             c=c+1
             cnt=cnt+1
        g+=1
       # print(b,c,g)
        while(1):
        #print(i)
           if((b+i==d)and(c+i==e)):
              g=g+i
              #print(g)
              if(g>=a):
                 print("Terrorists Win !")
              else:
                 print("Counter Terrorists Win !")
              break;
           elif((b+i==d)and(c-i==e)):
              g=g+i
              #print(g)
              if(g>=a):
                 print("Terrorists Win !")
              else:
                print("Counter Terrorists Win !")
              break;
           elif((b-i==d)and(c-i==e)):
              g=g+i
             # print(g)
              if(g>=a):
                print("Terrorists Win !")
              else:
                print("Counter Terrorists Win !")
              break;
           elif((b-i==d)and(c+i==e)):
              g=g+i
              #print(g)
              if(g>=a):
                 print("Terrorists Win !")
              else:
                 print("Counter Terrorists Win !")
              break;

           i+=1
    t=t-1
