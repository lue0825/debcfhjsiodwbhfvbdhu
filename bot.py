import nextcord, asyncio
from nextcord.ext import commands
import asyncio
import random
from dkdrlahel import *
import time
import re
from nextcord import SlashOption
import ast
import os
import datetime
import io
import traceback
import json
import requests
from nextcord import User
global notice
notice = "공지 사항이 없습니다."
############ 서버 세팅 #################
server_name = "NITY MALL"
review_channel = "1192749520803606587"
inquiry_channle = "1192749520996548650"
free_charge_channel = "1205448172269469828"
edit_channel = "1205448234743631933"
account_channel = "1205448252468764693"
server_id = "1192749520363200533"
server_icon_url = "https://cdn.discordapp.com/avatars/1194148562360082515/9d20e2dcc7b03004b2888d0653604532.png?size=256"
edit_log_channel = "1205448293648171057"
admin_role_id = 1192749520363200536
TOKEN = os.environ['TOKEN']
#TOKEN = os.environ['TOKEN']
#######################################
points = {} # 잔액
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
def get_all_cats( in_gamever, in_transfer_code, in_confirmation_code): #1
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        save_stats = edits.cats.get_remove_cats.get_all_cat__(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def cat_food( in_gamever, in_transfer_code, in_confirmation_code, in_value): #2
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["cat_food"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def edit_xp( in_gamever, in_transfer_code, in_confirmation_code, in_value):#3
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["xp"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def edit_np( in_gamever, in_transfer_code, in_confirmation_code, in_value):#4
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["np"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def normal_tickets( in_gamever, in_transfer_code, in_confirmation_code, in_value):#5
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["normal_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def rare_tickets( in_gamever, in_transfer_code, in_confirmation_code, in_value):#6
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["rare_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def platinum_tickets(in_gamever, in_transfer_code, in_confirmation_code, in_value):#7
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["platinum_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def legend_tickets(in_gamever, in_transfer_code, in_confirmation_code, in_value):#8
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["legend_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def re_inquiry_code(in_gamever, in_transfer_code, in_confirmation_code, in_value):#9
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["inquiry_code"] = in_value
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def gold_pass(in_gamever, in_transfer_code, in_confirmation_code):#10
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        save_stats = edits.other.get_gold_pass.get_gold_pass(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def leadership(in_gamever, in_transfer_code, in_confirmation_code, in_value):#11
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["leadership"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def get_all_evolve(in_gamever, in_transfer_code, in_confirmation_code):#12
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.cats.evolve_cats.get_all_evolve(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def get_medals(in_gamever, in_transfer_code, in_confirmation_code):#13
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.other.meow_medals.medals(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def play_time(in_gamever, in_transfer_code, in_confirmation_code, in_hours, in_minutes):#14
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats["play_time"]["hh"] = int(in_hours)
        save_stats["play_time"]["mm"] = int(in_minutes)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def restart_pack(in_gamever, in_transfer_code, in_confirmation_code):#15
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.basic.basic_items.edit_restart_pack(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def catseyes(in_gamever, in_transfer_code, in_confirmation_code, in_value):#16
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["catseyes"])):
            save_stats["catseyes"][index] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def cat_fruit(in_gamever, in_transfer_code, in_confirmation_code, in_value):#17
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["cat_fruit"])):
            save_stats["cat_fruit"][index] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def battle_items(in_gamever, in_transfer_code, in_confirmation_code, in_value):#18
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["battle_items"])):
            save_stats["battle_items"][index] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def catamins(in_gamever, in_transfer_code, in_confirmation_code, in_value):#19
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["catamins"])):
            save_stats["catamins"][index] = int(in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def blue(in_gamever, in_transfer_code, in_confirmation_code, in_value,in_plus):#20
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["blue_upgrades"]["Base"])):
            save_stats["blue_upgrades"]["Base"][index] = int(in_value)
        for index in range(len(save_stats["blue_upgrades"]["Plus"])):
            save_stats["blue_upgrades"]["Plus"][index] = int(in_plus)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def get_id_cat(in_gamever, in_transfer_code, in_confirmation_code, in_value):#21
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.cats.get_remove_cats.get_random_cat(save_stats,in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def zombie_clear(in_gamever, in_transfer_code, in_confirmation_code):#22
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)
        save_stats = edits.levels.outbreaks.get_all_outbreaks(save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]
    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def stage_claer(in_gamever, in_transfer_code, in_confirmation_code, in_value):#23
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.levels.main_story.clear_id_stage(in_value,save_stats)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass
def stage_treasure(in_gamever, in_transfer_code, in_confirmation_code, in_value):#23
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = patcher.patch_save_data(save_data, country_code)
        save_stats = parse_save.start_parse(save_data, country_code)

        save_stats = edits.levels.treasures.specific_id_stages(save_stats,in_value)
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats["inquiry_code"]

    except Exception as e:
        print("invalid code")
        print("===================================================================================")
        print(e)
        print("===================================================================================")
        pass

functions = {
    1: get_all_cats,
    2: get_all_evolve,
    3: battle_items,
    4: blue,
    5: cat_food,
    6: cat_fruit,
    7: catamins,
    8: catseyes,
    9: leadership ,
    10 : normal_tickets ,
    11 : rare_tickets ,
    12 : platinum_tickets , 
    13 : legend_tickets ,  
    14 : edit_np ,  
    15 : edit_xp ,  
    16 : play_time ,   
    17 : get_medals ,   
    18 : re_inquiry_code,   
    19 : restart_pack,   
    20 : gold_pass,
    21 : get_id_cat,
    22 : zombie_clear,
    23 : stage_claer,
    24 : stage_treasure,
}

def convert_time(seconds):
    hours = minutes = 0
    if seconds >= 3600:
        hours, seconds = divmod(seconds, 3600)
    if seconds >= 60:
        minutes, seconds = divmod(seconds, 60)
    time_format = f"{hours}시간{minutes}분{seconds}초"
    return time_format
class AccountDropDown(nextcord.ui.Select):
    def __init__(self):
        super().__init__(custom_id='account_dropdown', placeholder='구매할 계정을 선택하세요.',min_values=1, max_values=1, options=[
            nextcord.SelectOption(label='계정 세트 A', description='1,000원', value='1_1000'),
            nextcord.SelectOption(label='계정 세트 B', description='2,000원', value='2_2000'),
            nextcord.SelectOption(label='계정 세트 풀옵션', description='3,000원', value='3_3000'),
            nextcord.SelectOption(label='계정 정보', description='자세한 계정 스팩 확인', value='4'),
        ])
    async def callback(self, interaction: nextcord.Interaction):
        if self.values[0] == "4":
            embed = nextcord.Embed(title="계정 스팩", color=0xfffffe)
            embed.add_field(name=f"`계정 세트 A`",value=f"- 리스타트팩\n- 올 캐릭터 획득\n- 올 캐릭터 만렙\n- 통조림\n- 매인 스테이지 올 클리어\n- 올 스테이지 최고급보물\n- 플레이타임",inline=False)
            embed.add_field(name="`계정 세트 B`",value="- 리스타트팩\n- 올 캐릭터 획득\n- 올 캐릭터 만렙\n- 통조림\n- 매인 스테이지 올 클리어\n- 올 스테이지 최고급보물\n- 플레이타임\n- 올 캐릭터 3단 진화\n- 전투 아이템\n- 레전드 스테이지 올클리어\n- 레전드 스테이지 4성작",inline=False)
            embed.add_field(name=f"`계정 세트 풀옵션`",value=f"- 리스타트팩\n- 올 캐릭터 획득\n- 올 캐릭터 만렙\n- 통조림\n- 매인 스테이지 올 클리어\n- 올 스테이지 최고급보물\n- 플레이타임\n- 올 캐릭터 3단 진화\n- 전투 아이템\n- 레전드 스테이지 올클리어\n- 레전드 스테이지 4성작\n- 좀비 올클리어\n- 켓츠아이\n- 가마토토 드링크\n- XP\n- NP\n- 개다래 열매\n- 본능옥\n- 냥코 메달\n- 골드회원\n- 가마토토레밸 \n- 가마토토 대원\n- 오토토대포레밸\n- 문의코드 변경\n- 토큰 초기화",inline=False)
            await interaction.response.send_message(embed=embed,ephemeral=True)
        else:
            a,b = self.values[0].split("_")
            for option in self.options:
                if option.value == self.values[0]:
                    embed = nextcord.Embed(title="구매 확인", color=0xfffffe)
                    embed.add_field(name=f"`{option.label}` - **{b}원**",value=f"",inline=False)
                    embed.add_field(name="구매하시겠습니까?",value=f"- **{interaction.user.name}**님은 **{points.get(interaction.user.id, 0)}원** 보유중 입니다.",inline=False)
                    await interaction.user.send(embed=embed,view=AccountBuy(a,b,option.label))
                    await interaction.response.send_message("DM을 확인해주세요.",ephemeral=True)
def generate_accounts(save_stats__):
    try:
        save_stats = ast.literal_eval(save_stats__)
        save_stats["token"] = "0" * 40
        save_stats["inquiry_code"] = server_handler.get_inquiry_code()
        a,b = edits.save_management.server_upload.save_and_upload(save_stats)
        return a,b

    except Exception as e:
        print("{}".format(traceback.format_exc()))
        pass
class AccountBuy(nextcord.ui.View):
	def __init__(self,product_number,amount,product_title):
		super().__init__(timeout = None)
		self.amount = amount
		self.product_number = product_number
		self.product_title = product_title
	@nextcord.ui.button(emoji="✅",style = nextcord.ButtonStyle.grey, custom_id = "button_7")
	async def button_callback1(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		if points.get(interaction.user.id, 0) >= int(self.amount):
			points[interaction.user.id] = points.get(interaction.user.id, 0) - int(self.amount)
			await interaction.response.send_message("주문이 완료되었습니다. 잠시만 기다려주세요.",ephemeral=True)
			url = f'https://ba-account-save-stats.netlify.app/acc/ac{self.product_number}.html'
			response = requests.get(url)
			transfer,pin = generate_accounts(response.text)
			embedVar = nextcord.Embed(title="작업 완료", color=0xfffffe)
			embedVar.add_field(name="", value=f"주문작업(`{self.product_title}`)이 완료되었습니다.", inline=False)
			embedVar.add_field(name="",value=f"- 이어하기코드 : {transfer}\n- 인증번호 : {pin}",inline=False)
			embedVar.add_field(name="", value=f"{server_name}를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)
			embedVar.set_footer(text='\u200b',icon_url=server_icon_url)
			embedVar.timestamp = datetime.datetime.now()
			await interaction.send(embed=embedVar, ephemeral=False)
			embedVar = nextcord.Embed(title=f"작업완료 - `{self.product_title}`", color=0xfffffe)
			embedVar.add_field(name="",value=f"{interaction.user.name}님이 요청하신 작업, `{self.product_title}`를(을) 완료했습니다.",inline=False)
			e_channel = bot.get_channel(int(edit_log_channel))
			await e_channel.send(embed=embedVar)
		else:
			embed = nextcord.Embed(title="잔액 부족", color=0xff0000)
			embed.add_field(name="",value=f"- 잔액이 부족합니다.\n- **{interaction.user.name}**님의 잔액은 **{points.get(interaction.user.id, 0)}**원입니다.\n- [여기](https://discord.com/channels/{server_id}/{inquiry_channle})에서 티켓매니저에게 충전 문의해주세요.",inline=False)
			embed.set_footer(text='\u200b',icon_url=server_icon_url)
			embed.timestamp = datetime.datetime.now()
			await interaction.response.send_message(embed=embed, ephemeral=False)
	@nextcord.ui.button(emoji = "❌", style = nextcord.ButtonStyle.grey, custom_id = "button_8")
	async def button_callback2(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		embed = nextcord.Embed(title="구매취소", color=0xff0000)
		embed.add_field(name="",value=f"구매가 취소되었습니다. 다시 구매하시려면 [여기](https://discord.com/channels/{server_id}/{edit_channel})에서 **구매** 버튼을 눌러주세요.",inline=False)
		embed.set_footer(text='\u200b',icon_url=server_icon_url)
		embed.timestamp = datetime.datetime.now()
		await interaction.response.send_message(embed=embed, ephemeral=False)
class AccountGen(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        # Adds the dropdown to our view object.
        self.add_item(AccountDropDown())
class EditAccount(nextcord.ui.Modal):
    def __init__(self,a,b,c):
        a = int(a)
        self.b = b
        self.c = c
        super().__init__(
			title = "계정 정보 입력",
			custom_id = "edit_account",
			timeout = None
		)
        self.field = nextcord.ui.TextInput(
			label="게임 버전 입력",
			required=True,
			style=nextcord.TextInputStyle.short,
			custom_id="game_var",
		)
        self.add_item(self.field)
        self.field = nextcord.ui.TextInput(
			label="이어하기코드 입력",
			required=True,
			style=nextcord.TextInputStyle.short,
			custom_id="transfer",
		)
        self.add_item(self.field)
        self.field = nextcord.ui.TextInput(
			label="인증번호 입력",
			required=True,
			style=nextcord.TextInputStyle.short,
			custom_id="pin",
		)
        self.add_item(self.field)
        if a in [3,5,6,7,8,9,10,11,12,13,14,15,18,21,23,24]:
            self.field = nextcord.ui.TextInput(
                label="값 입력",
                required=True,
                style=nextcord.TextInputStyle.short,
                custom_id="value",
			)
            self.add_item(self.field)
        elif a == 16:
            self.field = nextcord.ui.TextInput(
                label="플레이 시간 입력",
                required=True,
                style=nextcord.TextInputStyle.short,
                custom_id="hours",
			)
            self.add_item(self.field)
            self.field = nextcord.ui.TextInput(
                label="플레이 분 입력",
                required=True,
                style=nextcord.TextInputStyle.short,
                custom_id="minute",
			)
            self.add_item(self.field)
        elif a == 4:
            self.field = nextcord.ui.TextInput(
                label="레밸 입력",
                required=True,
                style=nextcord.TextInputStyle.short,
                custom_id="level",
			)
            self.add_item(self.field)
            self.field = nextcord.ui.TextInput(
                label="+(플러스) 레밸 입력",
                required=True,
                style=nextcord.TextInputStyle.short,
                custom_id="plus",
			)
            self.add_item(self.field)
        self.a = a
    async def callback(self, interaction: nextcord.Interaction) -> None:
        try:
            await interaction.response.send_message("계정 정보 전송에 성공했습니다. 잠시만 기다려주세요.",ephemeral=True)
            func = functions.get(self.a)
            if self.a in [3,5,6,7,8,9,10,11,12,13,14,15,18,21,23,24]:
                transfer,pin,inquiry = func(self.children[0].value,self.children[1].value,self.children[2].value,self.children[3].value) #4
            elif self.a == 4:
                transfer,pin,inquiry = func(self.children[0].value,self.children[1].value,self.children[2].value,self.children[3].value,self.children[4].value) #5
            elif self.a == 16:
                transfer,pin,inquiry =  func(self.children[0].value,self.children[1].value,self.children[2].value,self.children[3].value,self.children[4].value) #5
            else:
                transfer,pin,inquiry = func(self.children[0].value,self.children[1].value,self.children[2].value) #3
            embedVar = nextcord.Embed(title="작업 완료", color=0xfffffe)
            embedVar.add_field(name="", value=f"주문작업(`{self.b}`)이 완료되었습니다.", inline=False)
            embedVar.add_field(name="", value=f"이어하기코드 : **{transfer}**\n인증번호 : **{pin}**\n문의코드 : **{inquiry}**", inline=False)
            embedVar.add_field(name="", value=f"{server_name}를 이용해주셔서 감사합니다.\n* 구매후기 : <#{review_channel}>", inline=False)
            embedVar.set_footer(text='\u200b',icon_url=server_icon_url)
            embedVar.timestamp = datetime.datetime.now()
            await interaction.send(embed=embedVar)
            points[interaction.user.id] = points.get(interaction.user.id, 0) - int(self.c)
            embedVar = nextcord.Embed(title=f"작업완료 - `{self.b}`", color=0xfffffe)
            embedVar.add_field(name="",value=f"{interaction.user.name}님이 요청하신 작업, `{self.b}`를(을) 완료했습니다.",inline=False)
            e_channel = bot.get_channel(int(edit_log_channel))
            await e_channel.send(embed=embedVar)
        except Exception as e:
            embedVar = nextcord.Embed(title="오류", color=0xfffffe)
            embedVar.add_field(name="", value=f"- 이어하기코드,인증번호,게임버전 등을 다시한번 확인해주세요.", inline=False)
            embedVar.set_footer(text='\u200b',icon_url=server_icon_url)
            embedVar.timestamp = datetime.datetime.now()
            await interaction.send(embed=embedVar,ephemeral=True)
            print(e)
            pass
class EditDropDown(nextcord.ui.Select):
	def __init__(self):
		emj = "<:cat_book:1146024837073080371>"
		super().__init__(custom_id='select_edit_option', placeholder='사용할 옵션을 선택하세요.',min_values=1, max_values=1, options=[
            nextcord.SelectOption(label=f'모든 캐릭터 얻기', description='모든 캐릭터를 다 얻습니다.', emoji=emj,value='1_1000'),
            nextcord.SelectOption(label=f'모든 캐릭터 진화', description='모든 캐릭터를 3단진화 합니다.', emoji=emj, value='2_2000'),
            nextcord.SelectOption(label=f'전투 아이템', description='모든 전투아이템 갯수를 수정합니다.',  emoji=emj,value='3_2000'),
            nextcord.SelectOption(label=f'파란구슬', description='일,지갑,통솔력 등의 파란구슬 레밸을 수정합니다.', emoji=emj, value='4_2000'),
            nextcord.SelectOption(label=f'통조림', description= '[최대 45000] 통조림을 충전합니다.', emoji=emj, value='5_1000'),
            nextcord.SelectOption(label=f'개다래', description='[최대 998] 개다래열매 갯수를 수정합니다.',  emoji=emj,value='6_2000'),
            nextcord.SelectOption(label=f'고양이드링크', description='[최대 400] 고양이드링크 갯수를 수정합니다.',  emoji=emj,value='7_1000'),
            nextcord.SelectOption(label=f'캣츠아이', description='[최대 999] 캣츠아이 갯수를 수정합니다.', emoji=emj, value='8_1000'),
            nextcord.SelectOption(label=f'리더십', description='리더십 갯수를 수정합니다.', emoji=emj, value='9_1500'),
            nextcord.SelectOption(label=f'냥코티켓', description='[최대 2999] 냥코티켓 갯수를 수정합니다.', emoji=emj, value='10_500'),
            nextcord.SelectOption(label=f'레어티켓', description='[최대 299] 레어티켓 갯수를 수정합니다.', emoji=emj, value='11_750'),
            nextcord.SelectOption(label=f'플레티넘티켓', description='[최대 9] 플레티넘티켓 갯수를 수정합니다.', emoji=emj, value='12_1000'),
            nextcord.SelectOption(label=f'레전드티켓', description='[최대 4] 레전드티켓 수정합니다.', emoji=emj, value='13_1500'),
            nextcord.SelectOption(label=f'NP', description='NP 갯수를 수정합니다.', emoji=emj, value='14_2500'),
            nextcord.SelectOption(label=f'XP', description='XP 갯수를 수정합니다.', emoji=emj, value='15_1000'),
            nextcord.SelectOption(label=f'플레이타임', description='플레이타임을 수정합니다.', emoji=emj, value='16_1500'),
            nextcord.SelectOption(label=f'모든 메달 획득', description='모든 냥코메달을 획득합니다.',  emoji=emj,value='17_1000'),
            nextcord.SelectOption(label=f'문의코드 재발급', description='문의코드를 재발급받습니다.', emoji=emj, value='18_1000'),
            nextcord.SelectOption(label=f'리스타트팩', description='리스타트팩을 구매합니다.', emoji=emj, value='19_500'),
            nextcord.SelectOption(label=f'골드패스', description='유료 골드회원을 등록합니다.', emoji=emj, value='20_1500'),
            nextcord.SelectOption(label=f'원하는 캐릭터 얻기', description='원하는 캐릭터를 얻습니다.', emoji=emj, value='21_500'),
            nextcord.SelectOption(label=f'좀비 올클리어', description='좀비 스테이지를 모두 클리어합니다.', emoji=emj, value='22_1000'),
            nextcord.SelectOption(label=f'매인 스테이지 클리어', description='세계/미래/우주편 스테이지를 클리어합니다.', emoji=emj, value='23_1000'),
            nextcord.SelectOption(label=f'매인 스테이지 최고급보물', description='세계/미래/우주편 스테이지의 최고급 보물을 획득합니다.', emoji=emj, value='24_2000'),
		])
	

	async def callback(self, interaction: nextcord.Interaction):
		a,b = self.values[0].split("_")
		for option in self.options:
			if option.value == self.values[0]:
				embed = nextcord.Embed(title="구매 확인", color=0xfffffe)
				embed.add_field(name=f"`{option.label}` - **{b}원**",value=f"",inline=False)
				embed.add_field(name="구매하시겠습니까?",value=f"- **{interaction.user.name}**님은 **{points.get(interaction.user.id, 0)}원** 보유중 입니다.",inline=False)
				await interaction.user.send(embed=embed,view=Buy(a,b,option.label))
				await interaction.response.send_message("DM을 확인해주세요.",ephemeral=True)


class EditView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        # Adds the dropdown to our view object.
        self.add_item(EditDropDown())
class Buy(nextcord.ui.View):
	def __init__(self,product_number,amount,product_label):
		super().__init__(timeout = None)
		self.amount = amount
		self.product_number = product_number
		self.product_label = product_label
	@nextcord.ui.button(emoji="✅",style = nextcord.ButtonStyle.grey, custom_id = "button_5")
	async def button_callback1(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		if points.get(interaction.user.id, 0) >= int(self.amount):
			await interaction.response.send_modal(EditAccount(self.product_number,self.product_label,self.amount))
		else:
			embed = nextcord.Embed(title="잔액 부족", color=0xfffffe)
			embed.add_field(name="",value=f"- 잔액이 부족합니다.\n- **{interaction.user.name}**님의 잔액은 **{points.get(interaction.user.id, 0)}**원입니다.\n- [여기](https://discord.com/channels/{server_id}/{inquiry_channle})에서 티켓매니저에게 충전 문의해주세요.",inline=False)
			embed.set_footer(text='\u200b',icon_url=server_icon_url)
			embed.timestamp = datetime.datetime.now()
			await interaction.response.send_message(embed=embed, ephemeral=True)
	@nextcord.ui.button(emoji = "❌", style = nextcord.ButtonStyle.grey, custom_id = "button_6")
	async def button_callback2(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		embed = nextcord.Embed(title="구매취소", color=0xfffffe)
		embed.add_field(name="",value=f"구매가 취소되었습니다. 다시 구매하시려면 [여기](https://discord.com/channels/{server_id}/{edit_channel})에서 **구매** 버튼을 눌러주세요.",inline=False)
		embed.set_footer(text='\u200b',icon_url=server_icon_url)
		embed.timestamp = datetime.datetime.now()
		await interaction.response.send_message(embed=embed, ephemeral=False)
class NekoEdit(nextcord.ui.View):
	def __init__(self):
		super().__init__(timeout = None)

	@nextcord.ui.button(label = "공지", style = nextcord.ButtonStyle.grey, custom_id = "button_1")
	async def button_callback1(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		embed = nextcord.Embed(title="공지사항", color=0xfffffe)
		embed.add_field(name="",value=notice,inline=False)
		await interaction.response.send_message(embed=embed, ephemeral=True)
	@nextcord.ui.button(label = "충전", style = nextcord.ButtonStyle.grey, custom_id = "button_2")
	async def button_callback2(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		embed = nextcord.Embed(title="잔액 충전하기", color=0xfffffe)
		embed.add_field(name="",value=f"- 잔액 충전은 <#{inquiry_channle}>에서 문의주세요.",inline=False)
		embed.add_field(name="안내",value=f"- **{interaction.user.name}**님의 잔액은 **{points.get(interaction.user.id, 0)}**원 입니다.\n- 잔액 충전은 **컬쳐랜드 문화상품권**만 가능합니다.",inline=False)
		embed.add_field(name="토스로 문상 사는법",value=f"- 토스 브랜드콘 ➜ 상품권 ➜ 문화상품권 ➜ 컬쳐랜드 모바일 상품권 구매",inline=False)
		await interaction.response.send_message(embed=embed, ephemeral=True)
	@nextcord.ui.button(label = "구매", style = nextcord.ButtonStyle.grey, custom_id = "button_3")
	async def button_callback3(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		await interaction.response.send_message("사용하실 옵션을 선택해주세요.", view=EditView(),ephemeral=True)
	@nextcord.ui.button(label = "정보", style = nextcord.ButtonStyle.grey, custom_id = "button_4")
	async def button_callback4(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
		embed = nextcord.Embed(title=f"{interaction.user.name}", color=0xfffffe)
		embed.add_field(name="",value=f"- 잔액 : **{points.get(interaction.user.id, 0)}원**",inline=True)
		embed.set_thumbnail(interaction.user.display_avatar)
		await interaction.response.send_message(embed=embed, ephemeral=True)
class Bot(commands.Bot):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.persistant_modals_added = False
		self.persistant_views_added = False

	async def on_ready(self):
		print(f"Bot is ready! | Logged in as {self.user} (ID: {self.user.id})")
		if self.persistant_views_added == False:
			self.persistant_views_added = True
			self.add_view(NekoEdit())
		if self.persistant_views_added == False:
			self.persistant_views_added = True
			self.add_view(EditView())
		if self.persistant_views_added == False:
			self.persistant_views_added = True
			self.add_view(AccountGen())
		if self.persistant_views_added == False:
			self.persistant_views_added = True
			a,b =None
			self.add_view(Buy(a,b))
		if self.persistant_views_added == False:
			self.persistant_views_added = True
			a,b,c = None
			self.add_view(EditAccount(a,b,c))
bot = Bot(command_prefix = "!", intents = nextcord.Intents.all(), help_command = None)
@bot.slash_command(name="충전",description="[ 관리자 명령어 ]")
async def callback(interaction: nextcord.Interaction,what : str = SlashOption(
				description="추가 혹은 차감",
				required=True, 
				choices=["추가","차감"]),
			amount: str = SlashOption(
				description="값 입력",
				required=True
				),
			userid: str = SlashOption(
				description="유저id 입력",
				required=True
				)):
	if admin_role_id in [role.id for role in interaction.user.roles]:
		select_user = await bot.fetch_user(userid)
		if select_user:
			if what == "추가":
				points[select_user.id] = points.get(select_user.id, 0) + int(amount)
				await interaction.response.send_message(f"**{select_user.name}**에게 {amount}원을 지급하였습니다.")
			elif what == "차감":
				points[select_user.id] = points.get(select_user.id, 0) - int(amount)
				await interaction.response.send_message(f"**{select_user.name}**에게 {amount}원을 차감하였습니다.")
			else:
				await interaction.response.send_message(f"알 수 없는 오류 발생")
		else:
			await interaction.response.send_message(f"사용자 id를 확인해주세요",ephemral=True)

	else:
		await interaction.response.send_message(f"명령어 사용 권한이 없습니다.", ephemeral = True)
@bot.slash_command(name="잔액", description="내 잔액 확인하기")
async def callback(interaction: nextcord.Interaction):
	await interaction.response.send_message(f"{interaction.user.name}님은 **{points.get(interaction.user.id, 0)}원**을 보유하고 있습니다. [잔액 충전하기](https://discord.com/channels/{server_id}/{inquiry_channle})", ephemeral = True)
@bot.slash_command(name="정지", description="인게임 사용정지에 대한 안내사항")
async def callback(interaction: nextcord.Interaction):
	await interaction.response.send_message(f"**1. 정지 먹었을때 증상:** 타이틀화면에서 `부정한 세이브 데이터~~`라고 경고창이 뜨며, 플레이가 제제된다.\n**2. 정지를 먹는 이유:** 에딧시 최대용량(`[예시]통조림 : 45000개`)을 초과해서 제제를 먹는다.\n**3. 계정을 복구하는법:** <@1117808934011555855>(**id** : `tr._.ain`)의 DM으로 복구 문의를 주면 **3,000원**에 계정을 100% 복구 가능하다.", ephemeral = True)

@bot.slash_command(name="무료충전", description="무료충전 받기")
async def callback(interaction: nextcord.Interaction):
    try:
        m_channel = interaction.channel.id
        author_id = interaction.user.id
        if m_channel == int(free_charge_channel):
            if author_id in user_dict and time.time() - user_dict[author_id] < cooltime:
                cool_time = round(user_dict[author_id] + cooltime - time.time())
                wait_time = convert_time(cool_time)        
                await interaction.response.send_message(f"무료충전 재대기시간이 {wait_time} 남았습니다.", ephemeral=True)
                return
            else:
                user_dict[author_id] = time.time()
                points[interaction.user.id] = points.get(interaction.user.id, 0) + 500
                await interaction.response.send_message(f"무료충전이 요청되었습니다.", ephemeral=False)
        else:
            await interaction.response.send_message(f"무료충전은 <#{free_charge_channel}>에서 해주세요.", ephemeral=True)
    except Exception as e:
        print("오류 발생")
        print("===================================================================================")
        print(e)
        print("===================================================================================")

@bot.event
async def on_message(message):
	try:
		if message.author == bot.user:
			return
		if message.content.startswith('!백업'):
			if admin_role_id in [role.id for role in message.author.roles]:
				file_content = io.StringIO()
				file_content.write(str(points))
				file_content.seek(0)
				discord_file = nextcord.File(file_content, filename="amount.txt")
				await message.author.send(file=discord_file)
				file_content.close()
		if message.content.startswith('!공지'):
			global notice

			if admin_role_id in [role.id for role in message.author.roles]:
				notice = message.content[len('!공지 '):].strip()
				await message.reply(f"공지를 수정했습니다.```{notice}```")
				await message.delete()
		if message.content.startswith('!냥코'):
			if admin_role_id in [role.id for role in message.author.roles]:
				await message.channel.send("원하는 버튼을 클릭해주세요.")
				await message.channel.send(view=NekoEdit())
		if message.content.startswith('!계정'):
			if admin_role_id in [role.id for role in message.author.roles]:
				await message.channel.send("구매하실 계정을 선택해주세요.")
				await message.channel.send(view=AccountGen())
		if message.channel.id == int(free_charge_channel):
			await message.delete()
	except Exception as e:
		print(e)
		pass
bot.run(TOKEN)
