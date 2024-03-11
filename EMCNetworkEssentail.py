#Help: Ability Mayfly's ID is 10. 

import json
import random
import time

ll.registerPlugin("ENEssentials", "A plugins to add essentials funation.", [1,0,0,Version.Release], {})
#输出启动日志...
log("Server is startuping.")
#读取文件
global lang
config = json.loads(File.readFrom("plugins\\ENEssentials\\config.json"))
lang = json.loads(File.readFrom("plugins\\ENEssentials\\lang\\"+config['language']+".json"))
#这是一个空参数,用于在需要无操作但必须需要提供函数的函数使用
def passFuncation(*args):
    pass

def flyCmd(pl,args):
    fly = json.loads(File.readFrom("plugins\\ENEssentials\\fly.json"))
    flyFlag = False
    for i in fly['allowedFlyPlayers']:
        if i == str(pl.xuid) or i == str(pl.realName) or pl.isOP():
            flyFlag = True
    if flyFlag == False:
        pl.tell(lang['fly.help'])
    elif len(args) == 0 and not pl.getAbilities()['mayfly']:
        pl.setAbility(10,True)
        pl.tell(lang['fly.toggle_sucess.on'])
    elif len(args) == 0 and pl.getAbilities()['mayfly']:
        pl.setAbility(10,False)
        pl.tell(lang['fly.toggle_sucess.off'])
    elif flyFlag and args[0] == "true" and len(args) == 1:
        pl.setAbility(10,True)
        pl.tell(lang['fly.toggle_sucess.on'])
    elif flyFlag and args[0] == "false" and len(args) == 1:
        pl.setAbility(10,False)
        pl.tell(lang['fly.toggle_sucess.off'])
    elif flyFlag and args[0] == "true" and len(args) == 2:
       usr = None
       for i in mc.getOnlinePlayers():
           if i.name == args[1]:
               usr = i
               break
       if usr == None:
           pl.tell(lang['generic.error'])
       else:
           usr.setAbility(10,True)
           pl.tell(lang['fly.toggle_sucess.on'])
    elif flyFlag and args[0] == "false" and len(args) == 2:
       usr = None
       for i in mc.getOnlinePlayers():
           if i.name == args[1]:
               usr = i
               break
       if usr == None:
           pl.tell(lang['generic.error'])
       else:
           usr.setAbility(10,False)
           pl.tell(lang['fly.toggle_sucess.off'])

def flyCmd_con(args):
    fly = json.loads(File.readFrom("plugins\\ENEssentials\\fly.json"))
    if len(args) == 0 or len(args) == 1:
        log(lang['fly.con_help'])
    elif args[0] == "true" and len(args) == 2:
       usr = None
       for i in mc.getOnlinePlayers():
           if i.name == args[1]:
               usr = i
               break
       if usr == None:
           log(lang['console.error'])
       else:
           usr.setAbility(10,True)
           log(lang['fly.toggle_sucess.on_con'])
    elif args[0] == "false" and len(args) == 2:
       usr = None
       for i in mc.getOnlinePlayers():
           if i.name == args[1]:
               usr = i
               break
       if usr == None:
           log(lang['console.error'])
       else:
           usr.setAbility(10,False)
           log(lang['fly.toggle_sucess.off_con'])

def flylistCmd(pl,args):
    fly = json.loads(File.readFrom("plugins\\ENEssentials\\fly.json"))
    if len(args) == 0:
        pl.tell(lang['flylist.help'])
    elif args[0] == 'list':
        afl = ""
        for i in fly['allowedFlyPlayers']:
            afl = afl + str(i)+", "
        pl.tell(lang['flylist.flylist'].replace("$players$",afl))
    elif (args[0] == 'add' or args[0] == "remove") and len(args) == 0:
        pl.tell(lang['generic.error'])
    elif args[0] == 'add' and len(args) == 2:
        if data.name2xuid(args[1]) == "": 
            pl.tell(lang['generic.error'])
            return 1
        args[1] = int(data.name2xuid(args[1]))
        try:
            fly['allowedFlyPlayers'].remove(args[1])
            fly['allowedFlyPlayers'].append(args[1])
        except:
            fly['allowedFlyPlayers'].append(args[1])
        File.writeTo("plugins\\ENEssentials\\fly.json",json.dumps(fly))
        pl.tell(lang['generic.sucess'])
    elif args[0] == 'remove' and len(args) == 2:
        if data.name2xuid(arg[1]) == "": 
            pl.tell(lang['generic.error'])
            return 1
        args[1] = int(data.name2xuid(args[1]))
        try:
            fly['allowedFlyPlayers'].remove(args[1])
            File.writeTo("plugins\\ENEssentials\\fly.json",json.dumps(fly))
            pl.tell(lang['generic.sucess'])
        except BaseException:
            pl.tell(lang['generic.error'])
    else:
        pl.tell(lang['flylist.help'])
def flylistCmd_con(args):
    fly = json.loads(File.readFrom("plugins\\ENEssentials\\fly.json"))
    if len(args) == 0:
        log(lang['flylist.help'])
    elif args[0] == 'list':
        afl = ""
        for i in fly['allowedFlyPlayers']:
            afl = afl + str(i)+", "
        log(lang['flylist.flylist'].replace("$players$",afl))
    elif (args[0] == 'add' or args[0] == "remove") and len(args) == 0:
        log(lang['generic.error'])
    elif args[0] == 'add' and len(args) == 2:
        #log(data.name2xuid(args[1]))
        if data.name2xuid(args[1]) == "": 
            log(lang['generic.error'])
            return 1
        args[1] = int(data.name2xuid(args[1]))
        try:
            fly['allowedFlyPlayers'].remove(args[1])
            fly['allowedFlyPlayers'].append(args[1])
        except:
            fly['allowedFlyPlayers'].append(args[1])
        File.writeTo("plugins\\ENEssentials\\fly.json",json.dumps(fly))
        log(lang['generic.sucess'])
    elif args[0] == 'remove' and len(args) == 2:
        if data.name2xuid(args[1]) == "": 
            log(lang['generic.error'])
            return 1
        args[1] = int(data.name2xuid(args[1]))
        try:
            fly['allowedFlyPlayers'].remove(args[1])
            File.writeTo("plugins\\ENEssentials\\fly.json",json.dumps(fly))
            log(lang['generic.sucess'])
        except BaseException:
            log(lang['generic.error'])
    else:
        log(lang['flylist.help'])
def accountInfo(pl,args):
    global lang
    accountInfoForm = mc.newSimpleForm()
    accountInfoForm.setTitle(lang['uid.title'])
    accountInfoForm.setContent(lang['uid.descrption']+lang['uid.info'].replace("$username$",pl.name).replace("$xuid$",str(pl.xuid)).replace("$uuid$",str(pl.uuid)))
    #accountInfoForm.addButton(lang['generic.understand'])
    #accountInfoForm.addButton(lang['uid.show_key'],"textures/ui/accessibility_glyph_color.png")
    pl.sendForm(accountInfoForm,passFuncation)

def onPreJoinListener(pl):
    blacklist = json.loads(File.readFrom("plugins\\ENEssentials\\blacklist.json"))
    for i in blacklist:
        if (i['xuid'] == str(pl.xuid) or i['name'] == pl.realName) and i['endtime'] == -1 and i['type'] == "banned":
            pl.kick(lang['disconnect.banned'].replace("$name$",pl.name).replace("$xuid$",str(pl.xuid)).replace("$reason$",i['reason']).replace("$operator$",i['operator']))
            break
        elif (i['xuid'] == str(pl.xuid) or i['name'] == pl.realName) and i['endtime'] >= time.time() and i['type'] == "banned":
            pl.kick(lang['disconnect.tempbanned'].replace("$name$",pl.name).replace("$xuid$",str(pl.xuid)).replace("$reason$",i['reason']).replace("$endtime$",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['endtime']))).replace("$operator$",i['operator']))
            break
        elif (i['xuid'] == str(pl.xuid) or i['name'] == pl.realName) and i['endtime'] < time.time() and i['type'] == "banned":
            blacklist.remove(i)
            File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(blacklist))
            break
    
def onChat(pl,msg):
    blacklist = json.loads(File.readFrom("plugins\\ENEssentials\\blacklist.json"))
    prefix = json.loads(File.readFrom("plugins\\ENEssentials\\prefix.json"))
    for i in blacklist:
        if (str(pl.xuid) == i['xuid'] or pl.realName == i['name']) and i['endtime'] == -1 and i['type'] == "muted":
            pl.tell(lang['muted.msg'].replace("$endtime$","永久").replace("$reason$",i['reason']))
            return False
        elif (pl.xuid == i['xuid'] or pl.name == i['name']) and i['type'] == "muted" and i['endtime'] >= time.time():
            pl.tell(lang['muted.msg'].replace("$reason$",i['reason']).replace("$endtime$",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['endtime']))))
            return False
        elif (pl.xuid == i['xuid'] or pl.name == i['name']) and i['type'] == "muted" and i['endtime'] < time.time():
            blacklist.remove(i)
            File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(blacklist))
    if msg == "I love you, EMCNetwork Dev.":
        pl.tell("I love you too, $player$".replace("$player$",pl.name))
    for j in prefix:
        if j['playerXuid'] == pl.xuid or j['playerName'] == pl.realName:
            tag = j['playerTag']
    for i in mc.getOnlinePlayers():
        if config['playerChatMessage']['enabled']: 
            i.tell(config['playerChatMessage']['chatFormat'].replace("$device$",i.getDevice().os).replace("$ping$",str(i.getDevice().avgPing)).replace("$name$",i.name).replace("$message$",msg).replace("$prefix$",tag))
    return False

def blCmd(pl,args):
    fly:list = json.loads(File.readFrom("plugins\\ENEssentials\\blacklist.json"))
    if len(args) == 0:
        pl.tell(lang['blacklist.help'])
    elif args[0] == 'list':
        afl = ""
        for i in fly:
            afl = afl + (i['name']+"(xuid:"+str(i['xuid'])+",reason:"+i['reason']+",operator:"+i['operator']+",bantime:"+str(i['bantime'])+",endtime:"+str(i['endtime'])+",type:"+i['type']+")")+", "
        pl.tell(lang['blacklist.list'].replace("$players$",afl))
    elif (args[0] == 'add' or args[1] == "remove") and len(args) == 0:
        pl.tell(lang['blacklist.help'])
        return 1
    elif args[0] == "add" and len(args) >= 3:
        if data.name2xuid(args[1]) == pl.xuid:
            pl.tell(lang['blacklist.selfban'])
            return 1
        if not args[2] == "banned" and not args[2] == "muted":
            pl.tell(lang['blacklist.help'])
            return 1
        for i in fly:
            if i['xuid'] == data.name2xuid(args[1]): fly.remove(i)
            elif i['name'] == args[1]: fly.remove(i)
        banData = {
            "xuid": data.name2xuid(args[1]),
            "name": args[1],
            "bantime": time.time(),
            "type": args[2],
            "operator": pl.realName,
            "reason": "",
            "endtime": -1
        }
        try:
            banData['reason'] = args[3]
        except BaseException: pass
        try:
            if args[4].isdigit():
                banData['endtime'] = int(args[4])+time.time()
        except BaseException: pass
        fly.append(banData)
        File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(fly))
        for i in mc.getOnlinePlayers():
            if (str(i.xuid) == banData['xuid'] or i.name == banData['name']) and banData['endtime'] == -1:
                i.kick(lang['disconnect.banned'])
            elif (str(i.xuid) == banData['xuid'] or i.name == banData['name']) and banData['endtime'] >= 0:
                i.kick(lang['disconnect.tempbanned'])
        pl.tell(lang['generic.sucess'])
    elif args[0] == "remove" and len(args) == 2:
        for i in fly:
            if i['xuid'] == data.name2xuid(args[1]): fly.remove(i)
            elif i['name'] == args[1]: fly.remove(i)
        pl.tell(lang['generic.sucess'])
        File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(fly))
    else:
        pl.tell(lang['blacklist.help'])

 

def blCmd_con(args):
    fly:list = json.loads(File.readFrom("plugins\\ENEssentials\\blacklist.json"))
    if len(args) == 0:
        log(lang['blacklist.help'])
    elif args[0] == 'list':
        afl = ""
        for i in fly:
            afl = afl + (i['name']+"(xuid:"+str(i['xuid'])+",reason:"+i['reason']+",operator:"+i['operator']+",bantime:"+str(i['bantime'])+",endtime:"+str(i['endtime'])+",type:"+i['type']+")")+", "
        log(lang['blacklist.list'].replace("$players$",afl))
    elif (args[0] == 'add' or args[1] == "remove") and len(args) == 0:
        log(lang['blacklist.help'])
        return 1
    elif args[0] == "add" and len(args) >= 3:
        if not args[2] == "banned" and not args[2] == "muted":
            log(lang['blacklist.help'])
            return 1
        for i in fly:
            if i['xuid'] == data.name2xuid(args[1]): fly.remove(i)
            elif i['name'] == args[1]: fly.remove(i)
        banData = {
            "xuid": data.name2xuid(args[1]),
            "name": args[1],
            "bantime": time.time(),
            "type": args[2],
            "operator": "Console",
            "reason": "",
            "endtime": -1
        }
        try:
            banData['reason'] = args[3]
        except BaseException: pass
        #log(args)
        try:
            banData['endtime'] = int(args[4])+time.time()
        except BaseException: log("error")
        fly.append(banData)
        File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(fly))
        for i in mc.getOnlinePlayers():
            if (str(i.xuid) == banData['xuid'] or i.name == banData['name']) and banData['endtime'] == -1:
                i.kick(lang['disconnect.banned'].replace("$name$",banData['name']).replace("$xuid$",banData['xuid']).replace("$reason$",banData['reason']).replace("$operator$",banData['operator']))
            elif (str(i.xuid) == banData['xuid'] or i.name == banData['name']):
                i.kick(lang['disconnect.tempbanned'].replace("$name$",banData['name']).replace("$xuid$",str(banData['xuid'])).replace("$reason$",banData['reason']).replace("$endtime$",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(banData['endtime']))).replace("$operator$",banData['operator']))
        log(lang['generic.sucess'])
    elif args[0] == "remove" and len(args) == 2:
        for i in fly:
            if i['xuid'] == data.name2xuid(args[1]): fly.remove(i)
            elif i['name'] == args[1]: fly.remove(i)
        log(lang['generic.sucess'])
        File.writeTo("plugins\\ENEssentials\\blacklist.json",json.dumps(fly))
    else:
        log(lang['blacklist.help'])

def tsFuncation(pl,choice):
    servers = json.loads(File.readFrom("plugins\\ENEssentials\\transServer.json"))
    if choice == None: 
        return False
    elif len(servers) < choice:
        pl.tell(lang['generic.error'])
    elif not servers[choice]['server_open']:
        pl.tell(lang['transServer.closed'])
    else:
        pl.transServer(servers[choice]['server_ip'],servers[choice]['server_port'])
        

def tsCmd(pl,args):
    servers = json.loads(File.readFrom("plugins\\ENEssentials\\transServer.json"))
    fm = mc.newSimpleForm()
    fm.setTitle(lang['transServer.title'])
    fm.setContent(lang['transServer.descrption'])
    for i in servers:
        if not i['server_open']:
            fm.addButton(i['ui_name']+"\n"+lang['transServer.closed'],i['ui_icon'])
        else:
            fm.addButton(i['ui_name']+"\n"+i['ui_descrption']+" | "+lang['transServer.opening'],i['ui_icon'])
    pl.sendForm(fm,tsFuncation)
def onJoin(pl):
    config = json.loads(File.readFrom("plugins\\ENEssentials\\config.json"))
    if config['joinToastMessage']['enabled']:
        pl.sendToast(config['joinToastMessage']['title'].replace("$player$",pl.name),config['joinToastMessage']['message'].replace("$player$",pl.name))
    if config['loginTeleportToLobby']['enabled']:
        pl.teleport(config['loginTeleportToLobby']['xPos'],config['loginTeleportToLobby']['yPos'],config['loginTeleportToLobby']['zPos'],config['loginTeleportToLobby']['dimid'])  
    for i in mc.getOnlinePlayers():
        i.tell(lang['message.join_message'].replace("$player$",pl.name))
        

def noDamage():
    if config['noDamage']:
        for i in mc.getOnlinePlayers():
            i.setHealth(200)
def shop(pl,args): shopd(pl)

def shopd(pl):
    #print(args)
    shop = json.loads(File.readFrom("plugins\\ENEssentials\\shop.json"))
    fm = mc.newSimpleForm()
    fm.setTitle(lang['shop.title'])
    fm.setContent(lang['shop.descrption'].replace("$money$",str(pl.getMoney())))
    for i in shop:
        fm.addButton(i['name'],i['icon'])
    pl.sendForm(fm,shop_chd)

def shop_chd(pl,aux):
    global caux
    shop = json.loads(File.readFrom("plugins\\ENEssentials\\shop.json"))
    caux = aux
    if aux==None: return False
    else:
        fm = mc.newSimpleForm()
        fm.setTitle(lang['shop.title'])
        fm.setContent(lang['shop.descrption'].replace("$money$",str(pl.getMoney())))
        for i in shop[aux]['childItems']:
            fm.addButton(i['name']+"\n"+lang['shop.ides'].replace("$bm$",str(i['buy-money'])).replace("$sm$",str(i['sell-money'])),i['icon'])
        pl.sendForm(fm,shop_form)

def shop_form(pl,aux):
    global daux
    daux = aux
    shop = json.loads(File.readFrom("plugins\\ENEssentials\\shop.json"))
    if aux == None: 
        shopd(pl)
    else:
        fm = mc.newCustomForm()
        fm.setTitle(lang['shop.title'])
        fm.addLabel(lang['shop.form_descrption'].replace("$item$",shop[caux]['childItems'][aux]['name']).replace("$money$",str(pl.getMoney())))
        fm.addDropdown(lang['shop.type'],[lang['shop.buy'],lang['shop.sell']],0)
        fm.addSlider(lang['shop.value'],1,64,1,1)
        pl.sendForm(fm,shop_formOpt)    

def shop_formOpt(pl,data):
    shop = json.loads(File.readFrom("plugins\\ENEssentials\\shop.json"))
    if data == None:
        shop_chd(pl,caux)
        return False
    log(data)
    if data[1] == 0:
        if pl.reduceMoney(shop[caux]['childItems'][int(daux)]['buy-money']*data[2]):
            it = mc.newItem(shop[caux]['childItems'][int(daux)]['id'],1)
            it.setAux(shop[caux]['childItems'][int(daux)]['aux'])
            pl.giveItem(it,data[2])
            pl.tell(lang['shop.ok'].replace("$money$",str(shop[caux]['childItems'][int(daux)]['buy-money']*int(data[2]))))
        else: pl.tell(lang['shop.no_money'])
    elif data[1] == 1:
        p = pl.clearItem(shop[caux]['childItems'][int(daux)]['id'],int(data[2]))
        if p < int(data[2]): 
            pl.clearItem(shop[caux]['childItems'][int(daux)]['id'],64-p)
            pl.tell(lang['shop.no_money'])
        else:
            pl.addMoney(shop[caux]['childItems'][int(daux)]['sell-money']*int(data[2]))
            it = mc.newItem(shop[caux]['childItems'][int(daux)]['id'],1)
            it.setAux(shop[caux]['childItems'][int(daux)]['aux'])
            pl.giveItem(it,p-data[2])
            pl.tell(lang['shop.sell_ok'].replace("$money$",str(shop[caux]['childItems'][int(daux)]['sell-money']*int(data[2]))))
def sc1(pl,confirm):
    if confirm == True:
        pl.kill()

def sc(pl,args):
    pl.sendModalForm(lang['suicide.title'],lang['suicide.descrption'],lang['generic.ok'],lang['generic.cancel'],sc1)
def reportAction(pl,data):
    pass
def report(pl,args):
    name = []
    players = mc.getOnlinePlayers()
    for i in players:
        name.append(i.realName)
    fm = mc.newCustomForm()
    fm.setTitle(lang['report.title'])
    fm.addLabel(lang['report.description'])
    fm.addDropdown(lang['report.player'],name,0)
    fm.addDropdown(lang['report.type'],config['playerReportOptions']['reportType'],0)
    fm.addInput(lang['report.reason'],lang['report.reason'])
    fm.addSwitch(lang['report.confirm'],False)
    pl.sendForm(fm,reportAction)

def onpc(pl,cmd):
    log(cmd)
    blacklist = json.loads(File.readFrom("plugins\\ENEssentials\\blacklist.json"))
    for i in blacklist:
        for j in config['muteToBannedCmd']:
            if (pl.xuid == i['xuid'] or pl.realName == i['name']) and i['endtime'] == -1 and i['type'] == "muted" and cmd.split(" ")[0] == j:
                pl.tell(lang['muted.msg'].replace("$endtime$","永久").replace("$reason$",i['reason']))
                return False
            elif (pl.xuid == i['xuid'] or pl.name == i['name']) and i['type'] == "muted" and i['endtime'] >= time.time() and cmd.split(" ")[0] == j:
                pl.tell(lang['muted.msg'].replace("$reason$",i['reason']).replace("$endtime$",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['endtime']))))
                return False
            
def rc(cmd):
    global config
    config = json.loads(File.readFrom("plugins\\ENEssentials\\config.json"))

def menud(pl,menuid):
    #global menuid_copy
    global tag
    pl.setExtraData("menuid",menuid)
    _prefix = json.loads(File.readFrom("plugins\\ENEssentials\\prefix.json"))
    try:
        mf = json.loads(File.readFrom("plugins\\ENEssentials\\menu\\"+menuid+".json"))
    except:
        pl.tell(lang['menu.no_menu'])
        return False
    if mf['cmd_opRequired'] and not pl.isOP():
        pl.tell(lang['generic.no_permission'])
        return False
    fm = mc.newSimpleForm()
    fm.setTitle(mf['ui_title'])
    tag = ""
    for i in _prefix:
        if pl.xuid == i['playerXuid'] or pl.realName == i['playerName']: 
            tag = i['playerTag']
    fm.setContent(mf['ui_content'].replace("$player$",pl.name).replace("$prefix$",tag).replace("$money$",str(pl.getMoney())))
    for i in mf['ui_buttons']:
        fm.addButton(i['ui_name'],i['ui_icon'])
    pl.sendForm(fm,menuOpt)

def menuOpt(pl,aux):
    mf = json.loads(File.readFrom("plugins\\ENEssentials\\menu\\"+pl.getExtraData("menuid")+".json"))
    if aux == None: return 1
    elif mf['ui_buttons'][aux]['opt_opRequired'] and not pl.isOP():
        pl.tell(lang['generic.no_permission'])
    elif mf['ui_buttons'][aux]['opt_actionType'] == "menu" and (pl.reduceMoney(mf['ui_buttons'][aux]['opt_cost']) or mf['ui_buttons'][aux]['opt_cost'] == 0):
        menud(pl,mf['ui_buttons'][aux]['opt_actions'][0])
    elif mf['ui_buttons'][aux]['opt_actionType'] == "cmd" and (pl.reduceMoney(mf['ui_buttons'][aux]['opt_cost']) or mf['ui_buttons'][aux]['opt_cost'] == 0):
        for i in mf['ui_buttons'][aux]['opt_actions']:
            mc.runcmdEx(i.replace("$player$",pl.realName).replace("$xuid$",str(pl.xuid)))
    elif mf['ui_buttons'][aux]['opt_actionType'] == "plCmd" and (pl.reduceMoney(mf['ui_buttons'][aux]['opt_cost']) or mf['ui_buttons'][aux]['opt_cost'] == 0):
        for i in mf['ui_buttons'][aux]['opt_actions']:
            pl.runcmd(i.replace("$player$",pl.realName).replace("$xuid$",str(pl.xuid)))      
    #pl.delExtraData("menuid")
def onLeft(pl):
    for i in mc.getOnlinePlayers():
        i.tell(lang['message.leave_message'].replace("$player$",pl.name))
def pd(pl,source):
    m = random.randint(config['playerDeathPunish']['reduceMoneyRange'][0],config['playerDeathPunish']['reduceMoneyRange'][1])
    e = random.randint(config['playerDeathPunish']['reduceExperienceRange'][0],config['playerDeathPunish']['reduceExperienceRange'][1])
    pl.reduceMoney(m)
    pl.reduceExperience(e)
    pl.tell(lang['death.message'].replace("$money$",str(m)).replace("$exp$",str(e)))
def menu(pl,args):
    menuid = config['serverForm']['automaticOpenMenuOnExecuteCmd']
    try:
        menuid = args[0]
    except BaseException:
        pass
    menud(pl,menuid)

def scchat(pl,args):
    if len(args) == 0:
        pl.tell(lang['staff_chat.help'])
    else:
        msg = " ".join(args)
        for i in mc.getOnlinePlayers():
            if i.isOP(): i.tell(lang['staff_chat.chat_format'].replace("$player$",pl.realName).replace("$message$",msg))
mc.regPlayerCmd("account",lang['uid.cmd_descrption'],accountInfo,0)
mc.regPlayerCmd("fly",lang['fly.cmd_descrption'],flyCmd,0)
mc.regPlayerCmd("flylist",lang['flylist.descrption'],flylistCmd,1)
mc.regPlayerCmd("blacklist",lang['blacklist.cmd_descrption'],blCmd,1)
mc.regPlayerCmd("server",lang['transServer.descrption'],tsCmd,0)
mc.regPlayerCmd("shop",lang['shop.title'],shop,0)
mc.regPlayerCmd('suicide',lang['suicide.title'],sc,0)
mc.regPlayerCmd('report',lang['report.title'],report,0)
#mc.regPlayerCmd('notice',lang['notice.title'],notice,0)
mc.regPlayerCmd('menu',lang['menu.title'],menu,0)
mc.regPlayerCmd("m",lang['menu.title'],menu,0)
mc.regPlayerCmd('hchat',lang['staff_chat.description'],scchat,1)

mc.regConsoleCmd("ep fly","",flyCmd_con)
mc.regConsoleCmd("ep flylist","",flylistCmd_con)
mc.regConsoleCmd("ep blacklist","",blCmd_con)
mc.regConsoleCmd("ep reloadcfg","",rc)

mc.listen("onPreJoin",onPreJoinListener)
mc.listen("onChat",onChat)
mc.listen("onJoin",onJoin)
mc.listen("onLeft",onLeft)
mc.listen("onTick",noDamage)
mc.listen("onPlayerCmd",onpc)
mc.listen("onPlayerDie",pd)
#mc.listen("onRespawn",onJoin)