import discord


bot = discord.Bot()
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="the best song ever"))
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hi(ctx):
    await ctx.send(f"Hey! {ctx.user.mention}")





@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.slash_command(name = "add", description = "Adds Two Sums together.")
# pycord will figure out the types for you
async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
  # you can use them as they were actual integers
  sum = first + second
  await ctx.respond(f"The sum of {first} and {second} is {sum}.")


class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    async def on_timeout(self):
        self.disable_all_items()
        await self.message.edit(content="You Took too long! Disabled Buttons!",  view=self)
    @discord.ui.button(label="Bot Invite Link", style=discord.ButtonStyle.red) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("<https://discord.com/api/oauth2/authorize?client_id=1122259720397394011&permissions=8&scope=bot>")
    
    @discord.ui.button(label="Support Server Link", row=1, style=discord.ButtonStyle.red)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("https://dsc.gg/syxsupport")

@bot.slash_command() # Create a slash command
async def bothelp(ctx):
    await ctx.respond("Click It!", view=MyView()) # Send a message with our View class that contains the button

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Info",
        description="Info About wuidBot",
        color=discord.Colour.red(), # Pycord provides a class with default colors you can choose from
    )
    embed.add_field(name="Fully Coded And Made By", value="**.wuid**")

    embed.add_field(name="Using ", value="Py-cord", inline=True)

    embed.add_field(name="do /bothelp", value="For More!", inline=True)
 
    embed.set_footer(text="Info!") # footers can have icons too
    embed.set_author(name="Info Embed", icon_url="https://pfps.gg/assets/pfps/1268-girl-pfp-1.png")
    embed.set_thumbnail(url="https://pfps.gg/assets/pfps/1268-girl-pfp-1.png")
    embed.set_image(url="https://pfps.gg/assets/banners/3332-90s-clouds.png")
 
    await ctx.respond("Info!", embed=embed) # Send the embed with some text




bot.run("TOKEN HERE (not file)")
