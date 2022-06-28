boss_blood_volume=100  # game boss的血条值
fist=10  #出拳的伤害值
kick=20  #出腿的伤害值
bigkill=35 #大招的伤害值
while ①:   #判断boss的血条值
    print('boss is alive')   # 活着
    attack=input('fist or kick or bigkill:')  #输入你的攻击类型
    if ②:   #如果出拳
        boss_blood_volume=boss_blood_volume-10   #出拳，boss血条值-10
    elif attack=='kick':
        boss_blood_volume=boss_blood_volume-③  #出腿，boss血条值-20
    ④ attack=='bigkill':
        boss_blood_volume=boss_blood_volume-35  #出大招，boss血条值-35
    ⑤:
        print('boss will kill you quick,please attack')
print('boss is dead final')   #boss 死了
