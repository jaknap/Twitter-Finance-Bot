import tweepy
import os
import pytz
import codecs
import sys
import datetime
from pytz import timezone
from time import strftimes
from keys import keys
import xlrd
import dt
book = xlrd.open_workbook("new_ch.xlsx")

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
f = open('Notify_T.tweetid', 'r')
idValue = f.read()
f.close()
idValue = int(idValue)
print "- - - - - - - - - - - - - - - - -"
print "tweetID file found! "
print "Latest Tweet ID: " +str(idValue)
print idValue
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
sheet = book.sheet_by_index(0)

def exit(text,user_):
    for i in range(18):
        if(val[i]==text and user_!='@Notify_T'):
            a=strftime("%H:%M")
            if(a=="17:31"):
                #api.send_direct_message( user = user_ , text= "Please wait, values being updated")
                sys.exit()


def date_():
    new = dt.d
    newstr = new.replace(",", "")
    da = newstr[6:]
    month = da[:3]
    day = da[4:6]
    year = da[-4:]
    fn = day + "-"+ month+"-"+ year
    return fn


def list_(text,user_):
    if(text=="@Notify_T #Tweet4NAV" or text=="@Notify_T #Tweet4Nav" or text=="@Notify_T #TWEET4NAV" or text=="@Notify_T #tweet4nav" or text=="@Notify_T #tweet4Nav" or text=="@Notify_T #Tweet4nav"):
        #msg = 'Mutual Fund Investments are subject to market risks, read all scheme related documents carefully'
        lnk = 'For Statutory details http://bit.ly/1URUqPe'
        api.update_with_media('/home/jaknap/tw.png', status='@'+user_+" "+ "Tweet the shortcode and we will DM you the NAV." +"\n" + lnk)
    elif(text=="@Notify_T \n#Tweet4NAV" or text=="@Notify_T \n#Tweet4Nav" or text=="@Notify_T \n#TWEET4NAV" or text=="@Notify_T \n#tweet4nav" or text=="@Notify_T \n#tweet4Nav"):
        #msg = 'Mutual Fund Investments are subject to market risks, read all scheme related documents carefully'
        lnk = 'For Statutory details http://bit.ly/1URUqPe'
        api.update_with_media('/home/jaknap/tw.png', status='@'+user_+" "+ "Tweet the shortcode and we will DM you the NAV." +"\n" + lnk)


handle = '@Notify_T'
val = [' #BD', ' #CM', ' #DB', ' #EA', ' #EF', ' #IO', ' #AF', ' #AG',
        ' #GO', ' #IF', ' #IS', ' #CF', ' #TS', ' #MC', ' #ST', ' #TA', ' #TP', ' #ES' ]
low = [x.lower() for x in val]


def codes(text,user_):
    for i in range(18):
        if(handle+val[i]==text or handle+low[i]==text):
            date = datetime.datetime.now(timezone('Asia/Kolkata')) - datetime.timedelta(days=1)
            now = 'NAV as on' + " " + date_()
            time = date.strftime('%H:%M:%S')
            tmsg = 'Sent at '+time
            msg = 'Mutual Fund Investments are subject to market risks, read all scheme related documents carefully'
            lnk = 'http://bit.ly/1URUqPe'
            if(i==0):     #BD
                new1= i+1
                new2= i+2
                new3= i+3
                new4= i+4
                new5= i+5
                new6= i+6
                new7= i+7
                new8= i+8
                new9= i+9
                n1=sheet.row(new1)[1].value
                n2=sheet.row(new2)[1].value
                n3=sheet.row(new3)[1].value
                n4=sheet.row(new4)[1].value
                n5=sheet.row(new5)[1].value
                n6=sheet.row(new6)[1].value
                n7=sheet.row(new7)[1].value
                n8=sheet.row(new8)[1].value
                n9=sheet.row(new9)[1].value
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+ " - " +n2  +"\n"+"Daily Dividend"+ " - "+n1  +"\n"+ "Weekly Dividend"+ " - "+n4  +"\n" +"Monthly Dividend"+ " - "+n3)
                api.send_direct_message( user = user_ , text= "Axis Banking Debt Fund- Direct Plan" +"\n"+ "Growth"+" - "+n7 +"\n"+"Monthly Dividend"+ " - "+n8 +"\n"+"Daily Dividend"+ " - "+n6 +"\n" +"Weekly Dividend"+ " - "+n9 +"\n"+ "Bonus"+" - "+n5)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg )
                print 'ok'
            elif(i==1):     #CM
                new1= i+9
                new2= i+10
                new3= i+11
                new4= i+12
                new5= i+13
                new6= i+14
                new7= i+15
                n1=sheet.row(new1)[1].value
                n2=sheet.row(new2)[1].value
                n3=sheet.row(new3)[1].value
                n4=sheet.row(new4)[1].value
                n5=sheet.row(new5)[1].value
                n6=sheet.row(new6)[1].value
                n7=sheet.row(new7)[1].value
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+" - "+n2 +"\n"+ "Regular Dividend"+" - "+n1  +"\n"+ "Half Yearly Dividend"+" - "+n3)
                api.send_direct_message( user = user_ , text= "Axis Constant Maturity Fund- Direct Plan"  +"\n"+ "Growth"+" - "+n6 +"\n"+ "Regular Dividend "+" - "+n5 +"\n"+"Half Yearly Dividend"+" - "+n7 +"\n"+"Bonus"+" - "+n4 )
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk+"\n"+  tmsg)
                print 'ok'
            elif(i==2):
                new1= i+15
                new2= i+16
                new3= i+17
                new4= i+18
                new5= i+19
                new6= i+20
                n1=sheet.row(new1)[1].value
                n2=sheet.row(new2)[1].value
                n3=sheet.row(new3)[1].value
                n4=sheet.row(new4)[1].value
                n5=sheet.row(new5)[1].value
                n6=sheet.row(new6)[1].value
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+" - "+n4  +"\n"+"Quarterly Dividend"+ " - "+n6 +"\n" +"Half Yearly Dividend"+ " - "+n5)
                api.send_direct_message( user = user_ , text= "Axis Dynamic Bond Fund- Direct Plan"  +"\n"+ "Growth"+" - "+n1 +"\n"+ "Half Yearly Dividend "+" - "+n2 +"\n"+"Quarterly Dividend"+" - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==3):
                new1= i+20
                new2= i+21
                new3= i+22
                new4= i+23
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth" + " - "+n4  +"\n"+ "Dividend"+ " - "+n3)
                api.send_direct_message( user = user_ , text= "Axis Enhanced Arbitrage Fund - Direct Plan" +"\n"+ "" + "Direct Growth "+" - "+n2  +"\n"+ "Direct Dividend" + " - "+n1)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==4):
                new1= i+23
                new2= i+24
                new3= i+25
                new4= i+26
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth" + " - "+n2  +"\n"+ "Dividend"+ " - "+n1)
                api.send_direct_message( user = user_ , text= "Axis Equity Fund - Direct Plan" +"\n"+ "Direct Growth "+ " - "+n4  +"\n"+ "Direct Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==5):
                new1= i+26
                new2= i+27
                new3= i+28
                new4= i+29
                new5= i+30
                new6= i+31
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth" + " - "+n4  +"\n"+ "Weekly Dividend" + " - "+n6  +"\n"+ "Monthly Dividend" + " - "+n5 )
                api.send_direct_message( user = user_ , text= "Axis Fixed Income Opportunities Fund - Direct Plan" +"\n"+ "Growth" + " - "+n1 +"\n"+ "Weekly Dividend" + " - "+n3 +"\n"+ "Monthly Dividend" + " - "+n2)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==6):
                new1= i+31
                new2= i+32
                new3= i+33
                new4= i+34
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + " - "+n2  +"\n"+ "Dividend" + " - "+n1)
                api.send_direct_message( user = user_ , text= "Axis Focus 25 Fund - Direct Plan" +"\n"+ "Growth "+ " - "+n4  +"\n"+ "Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk+"\n"+tmsg)
                print 'ok'
            elif(i==7): #AG
                new1= i+34
                n1=(sheet.row(new1)[1].value)
                api.send_direct_message( user = user_ , text= now + "\n " + sheet.cell_value(rowx=new1, colx=0) + " - "+n1)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk+"\n"+tmsg)
                print 'ok'
            elif(i==8): #go
                new1= i+34
                new2= i+35
                new3= i+36
                new4= i+37
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + " "+n2  +"\n"+ "Dividend" + " "+n1)
                api.send_direct_message( user = user_ , text= "Axis Gold Fund - Direct Plan" +"\n"+ "Growth "+ " - "+n4  +"\n"+ "Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+tmsg)
                print 'ok'
            elif(i==9):    #IF
                new1= i+37
                new2= i+38
                new3= i+39
                new4= i+40
                new5= i+41
                new6= i+42
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+" - "+n4  +"\n"+"Quarterly Dividend"+ " - "+n6 +"\n" +"Half Yearly Dividend"+ " - "+n5)
                api.send_direct_message( user = user_ , text= "Axis Income Fund- Direct Plan"  +"\n"+ "Growth"+" - "+n1 +"\n"+ "Half Yearly Dividend "+" - "+n2 +"\n"+"Quarterly Dividend"+" - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==10):
                new1= i+42
                new2= i+43
                new3= i+44
                new4= i+45
                new5= i+46
                new6= i+47
                new7= i+48
                new8= i+49
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                n7=(sheet.row(new7)[1].value)
                n8=(sheet.row(new8)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+" - "+n2  +"\n"+"Quarterly Dividend"+ " - "+n4 +"\n" +"Half Yearly Dividend"+ " - "+n3 +"\n" +"Annual"+ " - "+n1 )
                api.send_direct_message( user = user_ , text= "Axis Income Saver Fund- Direct Plan"  +"\n"+ "Growth"+" - "+n6 +"\n"+ "Quarterly Dividend "+" - "+n8 +"\n"+"Half Yearly Dividend"+" - "+n7 +"\n" +"Annual"+ " - "+n5)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk + "\n" +tmsg)
                print 'ok'
            elif(i==11):
                new1= i+49
                new2= i+50
                new3= i+51
                new4= i+52
                new5= i+53
                new6= i+54
                new7= i+55
                new8= i+56
                new9= i+57
                new10= i+58
                new11= i+59
                new12= i+60
                new13= i+61
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                n7=(sheet.row(new7)[1].value)
                n8=(sheet.row(new8)[1].value)
                n9=(sheet.row(new9)[1].value)
                n10=(sheet.row(new10)[1].value)
                n11=(sheet.row(new11)[1].value)
                n12=(sheet.row(new12)[1].value)
                n13=(sheet.row(new13)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+ " - " +n7  +"\n"+"Daily Dividend"+ " - "+n6  +"\n"+ "Weekly Dividend"+ " - "+n9  +"\n" +"Monthly Dividend"+ " - "+n8)
                api.send_direct_message( user = user_ , text= "Axis Liquid Fund- Retail Plan" +"\n"+ "Growth"+" - "+n11 +"\n"+" Daily Dividend"+ " - "+n10 +"\n" +" Weekly Dividend"+ " - "+n13+"\n"+" Monthly Dividend"+ " - "+n12)
                api.send_direct_message( user = user_ , text= "Axis Liquid Fund- Direct Plan" +"\n"+ "Growth_"+" - "+n3 +"\n"+"Daily Dividend"+ " - "+n2 +"\n" +"Weekly Dividend"+ " - "+n5+"\n"+"Monthly Dividend"+ " - "+n4  +"\n"+ "Direct Bonus"+" - "+n1)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n " + tmsg)
                print 'ok'
            elif(i==12):
                new1= i+61
                new2= i+62
                new3= i+63
                new4= i+64
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + "-"+n2  +"\n"+ "Dividend" + " -"+n1)
                api.send_direct_message( user = user_ , text= "Axis Long Term Equity Fund - Direct Plan" +"\n"+ " Growth "+ " - "+n4  +"\n"+ " Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk+"\n"+ tmsg)
                print 'ok'
            elif(i==13):
                new1= i+64
                new2= i+65
                new3= i+66
                new4= i+67
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + " - "+n2  +"\n"+ "Dividend" + " - "+n1)
                api.send_direct_message( user = user_ , text= "Axis Mid Cap Fund - Direct Plan" +"\n"+ " Growth "+ " - "+n4  +"\n"+ " Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==14):
                new1= i+67
                new2= i+68
                new3= i+69
                new4= i+70
                new5= i+71
                new6= i+72
                new7= i+73
                new8= i+74
                new9= i+75
                new10= i+76
                new11= i+77
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                n7=(sheet.row(new7)[1].value)
                n8=(sheet.row(new8)[1].value)
                n9=(sheet.row(new9)[1].value)
                n10=(sheet.row(new10)[1].value)
                n11=(sheet.row(new11)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+ " - " +n5  +"\n"+"Monthly Dividend"+ " - "+n6   +"\n" +"Regular Dividend"+ " - "+n7  +"\n"+ "Weekly Dividend"+ " - "+ n8   +"\n" +"Bonus"+ " - "+n4)
                api.send_direct_message( user = user_ , text= "Axis Short Term Fund- Retail Plan" +"\n"+ "Growth"+" - "+n9 +"\n"+"Monthly Dividend"+ " - "+n10 +"\n" +"Weekly Dividend"+ " - "+n11)
                api.send_direct_message( user = user_ , text= "Axis Short Term Fund- Direct Plan" +"\n"+ "Growth"+" - "+n1 +"\n"+"Monthly Dividend"+ " - "+n2 +"\n" +"Direct Weekly Dividend"+ " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==15):
                new1= i+77
                new2= i+78
                new3= i+79
                new4= i+80
                new5= i+81
                new6= i+82
                new7= i+83
                new8= i+84
                new9= i+85
                new10= i+86
                new11= i+87
                new12= i+88
                new13= i+89
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                n7=(sheet.row(new7)[1].value)
                n8=(sheet.row(new8)[1].value)
                n9=(sheet.row(new9)[1].value)
                n10=(sheet.row(new10)[1].value)
                n11=(sheet.row(new11)[1].value)
                n12=(sheet.row(new12)[1].value)
                n13=(sheet.row(new13)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0)+"\n"+ "Growth"+ " - " +n7  +"\n"+"Daily Dividend"+ " - "+n6  +"\n" +"Weekly Dividend"+ " - "+n9  +"\n"+ "Monthly Dividend"+ " - "+ n8)
                api.send_direct_message( user = user_ , text= "Axis Treasury Advantage Fund- Direct Plan" +"\n"+ "Growth"+" - "+n3 +"\n"+"Daily Dividend"+ " - "+n2 +"\n" +"Weekly Dividend"+ " - "+n5 +"\n" +"Monthly Dividend"+ " - "+n4 +"\n"+"Bonus"+ " - "+n1)
                api.send_direct_message( user = user_ , text= "Axis Treasury Advantage Fund- Retail Plan" +"\n"+ "Growth"+" - "+n11 +"\n"+"Daily Dividend"+ " - "+n10 +"\n" +"Weekly Dividend"+ " - "+n13+"\n"+"Monthly Dividend"+ " - "+n12)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk+"\n"+ tmsg)
                print 'ok'
            elif(i==16):
                new1= i+89
                new2= i+90
                new3= i+91
                new4= i+92
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + " "+n2  +"\n"+ "Dividend" + " "+n1)
                api.send_direct_message( user = user_ , text= "Axis Triple Advantage Fund - Direct Plan" +"\n"+ "Growth "+ " - "+n4  +"\n"+ "Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'
            elif(i==17):
                new1= i+92
                new2= i+93
                new3= i+94
                new4= i+95
                new5= i+96
                new6= i+97
                n1=(sheet.row(new1)[1].value)
                n2=(sheet.row(new2)[1].value)
                n3=(sheet.row(new3)[1].value)
                n4=(sheet.row(new4)[1].value)
                n5=(sheet.row(new5)[1].value)
                n6=(sheet.row(new6)[1].value)
                api.send_direct_message( user = user_ , text= now +"\n"+  sheet.cell_value(rowx=new1, colx=0) +"\n"+ "Growth" + " "+n4  +"\n"+ "Monthly Dividend" + " "+n5 +"\n"+ "Quarterly Dividend" + " - "+n6)
                api.send_direct_message( user = user_ , text= "Axis Equity Saver Fund - Direct Plan" +"\n"+ "Growth "+ " - "+n1 +"\n"+ "Monthly Dividend" + " - "+n2 +"\n"+ "Quarterly Dividend" + " - "+n3)
                api.send_direct_message( user = user_ ,text= msg +"\n"+ lnk +"\n"+ tmsg)
                print 'ok'

def verify(user_id):
    verify_= api.show_friendship(target_id=user_id)
    name=[mention_.followed_by for mention_ in verify_]
    print name[0]
    if (name[0]):
        print 'Done'
        exit(text,user_)
        list_(text,user_)
        codes(text,user_)




statuses= api.mentions_timeline(since_id=idValue)

for mention in statuses:
    text= mention.text
    user_= mention.user.screen_name
    #user_f = mention.user.following
    user_id=mention.user.id
    tweetid_=mention.id
    #print text
    print user_
    print tweetid_
    verify(user_id)




#------------------------------------------------------------------------------------------------------------

theUserName = 'Notify_T'
archiveFile = 'data.txt'
homeTZ = 'Asia/Kolkata'
homeTZ = pytz.timezone(homeTZ)

# lastTweetId file location
idFile = theUserName + '.tweetid'
pwd = os.path.dirname(__file__) # get script directory
idFile = os.path.join(pwd, idFile) # join dir and filename

utc = pytz.utc

# helpful variables
status_list = [] # Create empty list to hold statuses
cur_status_count = 0 # set current status count to zero

print "- - - - - - - - - - - - - - - - -"
print "autoTweetArchiver.py"

if os.path.exists(idFile):
    # Get most recent tweet id from file
    print 'ok'
    f = open(idFile, 'r')
    idValue = f.read()
    f.close()
    idValue = int(idValue)
    print "- - - - - - - - - - - - - - - - -"
    print "tweetID file found! "
    print "Latest Tweet ID: " +str(idValue)
    print "Gathering unarchived tweets... "

    if statuses != []:
        theUser = statuses[0].author
        total_status_count = theUser.statuses_count

    while statuses != []:
        cur_status_count = cur_status_count + len(statuses)
        for status in statuses:
            status_list.append(status)

        theMaxId = statuses[-1].id
        theMaxId = theMaxId - 1
        # Get next page of unarchived statuses
        statuses = api.mentions_timeline(count=10,since_id=idValue, max_id=theMaxId)

else:
    # Request first status page from twitter
    statuses = api.mentions_timeline(count=10)
    # Get User information for display
    theUser = statuses[0].author
    total_status_count = theUser.statuses_count
    print "- - - - - - - - - - - - - - - - -"
    print "No tweetID file found..."
    print "Creating a new archive file"
    print "- - - - - - - - - - - - - - - - -"

    while statuses != []:
        cur_status_count = cur_status_count + len(statuses)
        for status in statuses:
            status_list.append(status)

        # Get tweet id from last status in each page
        theMaxId = statuses[-1].id
        theMaxId = theMaxId - 1

        # Get new page of statuses based on current id location
        statuses = api.mentions_timeline(count=10,max_id=theMaxId)
        print "%d of %d tweets processed" % (cur_status_count, total_status_count)

   
    print "Writing statuses to log file:"

# Write tweets to archive
if status_list != []:
    print "Writing tweets to archive..."
    print "Archive file:"
    print archiveFile
   
    f = codecs.open(archiveFile, 'a', 'utf-8')
    for status in reversed(status_list):
        theTime = utc.localize(status.created_at).astimezone(homeTZ)
        # Format your tweet archive here!
        f.write(status.text + '\n')
        f.write(status.user.screen_name + '\n')
        f.write(theTime.strftime("%B %d, %Y at %I:%M%p\n"))
        f.write('http://twitter.com/'+status.author.screen_name+'/status/'+str(status.id)+'\n')
        f.write('- - - - - \n\n')
    f.close()

    # Write most recent tweet id to file for reuse
    print "Saving last tweet id for later..."
    f = open(idFile, 'w')
    f.write(str(status_list[0].id))
    f.close()

if status_list == []:
    print "- - - - - - - - - - - - - - - - -"
    print "No new tweets to archive!"
print "Total Statuses Retrieved: " + str(len(status_list))
print "Finished!"
print "- - - - - - - - - - - - - - - - -"

