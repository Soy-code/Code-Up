#!/usr/bin/env python
# coding: utf-8

# In[2]:


def baseball() :
    # 정답 생성
    import random as rnd
    answer = []
    while True :
        rd_num = rnd.randint(0, 9)
        if len(answer) == 4 :
            break
        if rd_num not in answer :
            answer.append(rd_num)
            
    print("The answer is: \n", answer, 
          "\n >>> If you want to quit this game, press the answer <<<")
    
    # input number 입력
    while True :
        num = int(input("Input number: "))
        call = list(map(int, str(num)))
        
        # 네자리 수 체크
        if len(call) == 4 :
            # 중복값 체크
            if len(set(call)) == 4 :
                if call == answer :
                    print("Bingo!")
                    break
                else : 
                    ball = 0
                    strike = 0
                    for i in range(4) :
                        if (call[i] in answer) :
                            if call.index(call[i]) == answer.index(call[i]) :
                                strike += 1
                            else :
                                ball += 1
                print("{} S {} B".format(strike, ball))
            else :
                print("duplicated numbers exist")
        else :
            print("input 4 digits.") 


# In[3]:


baseball()


# In[ ]:




