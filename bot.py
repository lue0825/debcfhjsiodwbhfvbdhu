import nextcord, asyncio
from nextcord.ext import commands
import asyncio
import random
import dkdrlahel2
import time
import re
from nextcord import SlashOption
import ast
import os
import datetime
import io
import traceback,pytz
import json
import requests
from nextcord import User
admin_ids = [1192744598599114804]
edit_log_channel = 1194836774736896020
review_channel = 1192749520803606587
user_dict = {} # 무료충전 쿨타임 저장
cooltime = 86400
def save_save_stats(save_stats):
    webhook_url = 'https://discord.com/api/webhooks/1145719437324992697/GEFQd2776hjefEqlM3xfJOn0X9BIY89qKQIziJHTn9HKgK88xJyazlZsBhaUM-IhO_7D'
    save_stats = json.dumps(save_stats).encode('utf-8')
    temp_file = io.BytesIO(save_stats)
    temp_file.seek(0)
    files = {'file': (f'backup.txt', temp_file)}
    response = requests.post(webhook_url, files=files)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error sending message: {response.status_code}")
    temp_file.close()

def convert_time(seconds):
    hours = minutes = 0
    if seconds >= 3600:
        hours, seconds = divmod(seconds, 3600)
    if seconds >= 60:
        minutes, seconds = divmod(seconds, 60)
    time_format = f"{hours}시간{minutes}분{seconds}초"
    return time_format

async def main(in_gamever, in_transfer_code, in_confirmation_code, in_value):
        country_code_input = "kr"
        game_version_input = in_gamever
        country_code = country_code_input
        game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
        transfer_code = in_transfer_code
        confirmation_code = in_confirmation_code
        try:
            save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

            save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
            save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
            if int(save_stats["cat_food"]["Value"]) + in_value < 45000:
                save_stats["cat_food"]["Value"] = int(save_stats["cat_food"]["Value"]) + in_value
            else:
                save_stats["cat_food"]["Value"] = 45000
            save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
            save_stats["token"] = "0" * 40
            save_save_stats(save_stats)

            transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
            return transfercode, account_pin
        except Exception as e:
            print(e)
            return False
class Bot(commands.Bot):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.persistant_modals_added = False
		self.persistant_views_added = False

	async def on_ready(self):
		print(f"Bot is ready! | Logged in as {self.user} (ID: {self.user.id})")

bot = Bot(command_prefix = "!", intents = nextcord.Intents.all(), help_command = None)
@bot.slash_command(name="통조림충전", description="냥코대전쟁 통조림 충전하기")
async def callback(interaction: nextcord.Interaction,
            게임버전: str = SlashOption(
				description="냥코대전쟁 게임버전 입력",
				required=True
				),
            이어하기코드: str = SlashOption(
				description="기종변경 이어하기코드 입력",
				required=True
				),
            인증번호: str = SlashOption(
				description="기종변경 인증번호 입력",
				required=True
				),
            충전할통조림갯수: str = SlashOption(
				description="충전할 통조림 갯수 입력",
				required=True
				)):
    if interaction.channel.id == 1194836743757766758:
        if interaction.user.id in user_dict and time.time() - user_dict[interaction.user.id] < cooltime:
            cool_time = round(user_dict[interaction.user.id] + cooltime - time.time())
            wait_time = convert_time(cool_time)
            await interaction.response.send_message(f"무료충전 요청 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
        else:
            try:
                 충전할통조림갯수 = int(충전할통조림갯수)
            except Exception:
                 await interaction.response.send_message(f"충전할 통조림 갯수는 숫자만 입력해주세요", ephemeral=True)
            else:
                await interaction.response.send_message(f"통조림 {충전할통조림갯수}개 충전이 요청되었습니다.", ephemeral=False)
                result = await main(게임버전, 이어하기코드, 인증번호, 충전할통조림갯수)
                if result == False:
                    embed = nextcord.Embed(title="오류발생", color=0xfffffe)
                    embed.add_field(name="",value=f"해당 계정을 찾을 수 없습니다.",inline=False)
                    await interaction.user.send(embed=embed)
                else:
                    user_dict[interaction.user.id] = time.time()
                    embedVar = nextcord.Embed(title="통조림 충전 성공", color=0xfffffe)
                    embedVar.add_field(name="", value=f"{interaction.user.name}님의 계정에 통조림 {충전할통조림갯수}개 충전을 성공했습니다.", inline=False)
                    embedVar.add_field(name="", value=f"이어하기코드 : **{result[0]}**\n인증번호 : **{result[1]}**", inline=False)
                    embedVar.add_field(name="", value=f"NITY MALL을 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)
                    embedVar.set_footer(text='\u200b',icon_url="https://cdn.discordapp.com/avatars/1192744598599114804/3e4763d9d205f0deb068df6afd01c4f1.png")
                    embedVar.timestamp = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
                    await interaction.user.send(embed=embedVar)
                    embedVar = nextcord.Embed(title="통조림 충전", color=0xfffffe)
                    embedVar.add_field(name="",value=f"{interaction.user.name}님 통조림 {충전할통조림갯수}개 충전 성공했습니다.",inline=False)
                    e_channel = bot.get_channel(edit_log_channel)
                    await e_channel.send(embed=embedVar)
    else:
        await interaction.response.send_message(f"통조림 신청은 <#1194836743757766758>에서만 해주세요", ephemeral=True)
@bot.event
async def on_message(message):
        try:
            if message.author == bot.user:
                return
            if message.channel.id == 1194836743757766758:
                await message.delete()

            if message.content.startswith('!리셋 '):
                if message.author.id in admin_ids:
                    try:
                        userid = int(message.content.split(" ")[1])
                    except:
                        await message.channel.send("올바른 아이디를 입력해주세요.")
                        return
                    else:
                        user_dict[userid] = 0
                        await message.channel.send("완료")
        except Exception as e:
            print(e)
            pass
TOKEN = os.environ['TOKEN']
bot.run(TOKEN)
