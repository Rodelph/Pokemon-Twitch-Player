from twitchio.ext import commands
import pyautogui
from time import sleep

choiceTimer = 0.05

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token='xtitxffsd1xsobjjdpo2budtvbozbu', prefix='!', initial_channels=['budget_bwipo'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is   | {self.user_id}')

    @commands.command()
    async def up(self, ctx: commands.Context, argument: int = 1):
        print("Key 'up' has been pressed with value {val}".format(val=argument))
        if isinstance(argument, int):
            for i in range(0, argument + 1):
                pyautogui.keyDown(key="up") 
                sleep(choiceTimer)
                pyautogui.keyUp(key="up")
        
    @commands.command()
    async def down(self, ctx: commands.Context, argument:int = 1):
        print("Key 'down' has been pressed with value {val}".format(val=argument))
        if isinstance(argument, int):
            for i in range(0, argument + 1):
                pyautogui.keyDown(key="down")
                sleep(choiceTimer)
                pyautogui.keyUp(key="down")

    @commands.command()
    async def left(self, ctx: commands.Context, argument: int = 1):
        print("Key 'left' has been pressed with value {val}".format(val=argument))
        if isinstance(argument, int):
            for i in range(0, argument + 1):
                pyautogui.keyDown(key="left")
                sleep(choiceTimer)
                pyautogui.keyUp(key="left")
        
    @commands.command()
    async def right(self, ctx: commands.Context, argument : int = 1):
        print("Key 'right' has been pressed with value {val}".format(val=argument))
        if isinstance(argument, int):
            for i in range(0, argument + 1):
                pyautogui.keyDown(key="right")
                sleep(choiceTimer)
                pyautogui.keyUp(key="right")

    @commands.command()
    async def x(self, ctx: commands.Context):
        print("Key 'x' has been pressed")
        pyautogui.keyDown(key="x")
        sleep(choiceTimer)
        pyautogui.keyUp(key="x")

    @commands.command()
    async def c(self, ctx: commands.Context):
        print("Key 'c' has been pressed")
        pyautogui.keyDown(key="c")
        sleep(choiceTimer)
        pyautogui.keyUp(key="c")

    @commands.command()
    async def com(self, ctx: commands.Context):
        await ctx.send("The list of commands are : !x !c !up !down !left !right")

    @commands.command()
    async def skip(self, ctx: commands.Context):
        print("Skipping scenes")
        for i in range(5):
            pyautogui.keyDown(key="x")
            sleep(1)
            pyautogui.keyUp(key="x")


if __name__ == "__main__":
    bot = Bot()
    bot.run()