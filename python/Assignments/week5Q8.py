class player:
    count=0
    def __init__(self,name,level):
        self.name=name
        self.level=level
        player.count+=1
p1=player("himal","Division")
p1=player("anikku","national")
p1=player("rifat","school")
print(f'total player is {player.count}')