#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import easygui as g
import random as r
class Pick:
    def __init__(self):
        self.di={'1':'能天使','2':'银灰','3':'斯卡蒂','4':'塞雷亚','5':'星熊','6':'夜莺','7':'伊芙利特','8':'安洁莉娜','9':'推进之王','10':'陈'
                 ,'11':'黑','12':'蓝毒','13':'因陀罗','14':'赫默','15':'阿米娅','16':'凛冬','17':'陨星','18':'火神','19':'临光','20':'守林人'
                 ,'21':'崖心','22':'夜魔','23':'诗怀雅','24':'炎客','25':'幽灵鲨','26':'白金','27':'蛇屠箱','28':'远山','29':'砾','30':'红豆'
                 ,'31':'霜叶','32':'白雪','33':'桃金娘','34':'调香师','35':'末药','36':'缠丸','37':'杜宾','38':'猎峰','39':'慕斯','40':'安比尔'
                 ,'41':'红云','42':'杰西卡','43':'流星','44':'梅','45':'古米','46':'坚雷','47':'克洛斯','48':'安塞尔','49':'斑点','50':'玫兰莎'
                 ,'51':'泡普卡','52':'月见夜','53':'空爆','54':'卡提','55':'米格鲁','56':'芙蓉','57':'梓蓝','58':'炎熔','59':'芬','60':'香草'}
        # Set the original probability
        self.pos=[]
        self.pos.extend(range(1,12))
        for p in range(4):
            self.pos.extend(range(12,27))
        for p in range(25):
            self.pos.extend(range(27,47))
        for p in range(20):
            self.pos.extend(range(47,61))
        self.pos2=self.pos[:]
    # Raise the probability of six-star character if it is not picked
    def choosecard(self):
        for i in range(1,12):
            self.pos.append(i)
    # Recover to the original probility if a six-star character is picked
    def reset(self):
        self.pos=self.pos2[:]
        
pick=Pick()

while True:        
    response=g.buttonbox('招募方式:','明日方舟抽卡模拟器',('单次招募','十次招募'))
    if response=="单次招募":
        b=r.choice(pick.pos)
        if b<12:
            pick.reset()
        else:
            pick.choosecard()
        e=g.ccbox('%s'%pick.di[str(b)],title='模拟结果')
     

        
    elif response=="十次招募":
        d=[]
        for i in range(10):
            b=r.choice(pick.pos)
            if b<12:
                pick.reset()
            else:
                pick.choosecard()
            d.append(pick.di[str(b)])
        g.msgbox(d,title='模拟结果')   
        
        
        


# In[2]:





# In[3]:





# In[ ]:




