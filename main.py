class Kratos:
    def __init__(game, KID, leviathanaxe_thrown, HP):
        game.KID = KID
        game.leviathanaxe_thrown = leviathanaxe_thrown
        game.HP = HP

    def weapon_launch(game):
        if game.leviathanaxe_thrown == "False" and (game.HP>str(1) or game.HP == 1):
            game.leviathanaxe_thrown = True
            return "Левиафан запущен."
        if game.leviathanaxe_thrown == "True" and (game.HP > str(1) or game.HP == 1):
            return "Левиафан уже запущен."
        if game.leviathanaxe_thrown == "False" and game.HP < str(1):
            return "Ты помер."
        if game.leviathanaxe_thrown == "True" and game.HP < str(1):
            return "Помер и потерял топор."
    def weapon_return(game):
        if game.leviathanaxe_thrown == "False":
            return "Левиафан в руках у Кратоса."
        if game.HP<1 and game.leviathanaxe_thrown == "True":
            return "Левиафана нет в руках."
    #def KID_as_companion(game):

print('How many HP does Kratos have?')
X=input()
print('Is Leviathan Launched? (T/F)')
Y=input()
if Y == "F" or "f":
    Y = "False"
if Y == "T" or "t":
    Y = "True"

PC = Kratos(KID = "Атрей", leviathanaxe_thrown=Y, HP=X)
print(PC.weapon_launch())