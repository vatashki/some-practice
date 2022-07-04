yearly_tax = int(input())

sneakers = yearly_tax * 0.6
outfit = sneakers * 0.8
ball = outfit * 0.25
accessories = ball * 0.2

spendings = yearly_tax +\
    sneakers +\
    outfit +\
    ball +\
    accessories

print(spendings)