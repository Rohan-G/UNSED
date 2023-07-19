import pymysql
import pymysql.cursors
import subprocess as sp
import getpass
import sys
from pprint import pprint

def gsa():
    print("gsa")
    sys.stdout.flush()
    try:
        mission_name = input("Enter the mission name: ")
        query = "Select distinct Agency_Name, Agency_Country from mission_agencies where Name='%s'" % mission_name
        pprint(query)
        cur.execute(query)
        con.commit()
        results = cur.fetchall()
        if not results:
            print("Empty set")
            return
        for x in results:
            print(x)
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def rsa():
    print("rsa")
    sys.stdout.flush()
    try:
        s1 = input("Enter space agency 1 Name: ")
        s1c = input("Enter space agency 1 Country: ")
        s2 = input("Enter space agency 2 Name: ")
        s2c = input("Enter space agency 2 Country: ")
        query = "select Model_Name, Agency_Name, Agency_Country from Rocket R, Payload P, Mission M where R.Model_Name = P.Rocket_Name and R.Agency_Name='%s' and R.Agency_Country='%s' and P.Sender_Name='%s' and P.Sender_Country='%s' and P.Mission_Name=M.Name and M.Celestial_Body=\"Moon\"" % (s1, s1c, s2, s2c)
        pprint(query)
        cur.execute(query)
        con.commit()
        results = cur.fetchall()
        if(len(results)==0):
            print("No results found")
        for x in results:
            print(x)
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)

    return

def gsm():
    print("gsm")
    sys.stdout.flush()
    try:
        n = int(input("Enter the payload(int): "))
        query = "Select * from mission where Available_Payload > %d" % n
        pprint(query)
        cur.execute(query)
        con.commit()
        results = cur.fetchall()
        if not results:
            print("Empty set")
            return
        for x in results:
            print(x)
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)

    return

def fms():
    print("fms")
    sys.stdout.flush()
    try:
        cb = input("Enter the celestial body: ")
        ac = input("Enter the agency country: ")
        an = input("Enter the agency name: ")
        query = "select m.Name from mission m, mission_agencies ma where ma.Agency_Name='%s' and ma.Agency_Country='%s' and m.Name=ma.Name and m.Celestial_Body='%s'" % (an, ac, cb)
        pprint(query)
        cur.execute(query)
        con.commit()
        results = cur.fetchall()
        if not results:
            print("Empty set")
            return
        for x in results:
            print(x)
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)

    return

def gas():
    print("gas")
    sys.stdout.flush()
    try:
        name1 = input("Enter the name of the space agency: ")
        country1 = input("Enter the country of the space agency: ")
        # query = "select count(s.Status)/count(tm.Status) from mission tm, mission s, mission_agencies MisA1, mission_agencies MisA2 where MisA1.Agency_Name='%s' and MisA1.Agency_Country='%s' and MisA2.Agency_Name='%s' and MisA2.Agency_Country='%s' and tm.Name=MisA1.Name and s.Name=MisA2.Name and s.Status='Successful'" % (name1, country1, name1, country1)
        query = "select count(distinct s.Name)/count(distinct tm.Name) as sr from mission tm, mission s, mission_agencies misa1, mission_agencies misa2 where misa1.Agency_Name='%s' and misa1.Agency_Country='%s' and misa2.Agency_Country='%s' and misa2.Agency_Name='%s' and tm.Name=misa1.Name and s.Name=misa2.Name and s.Status='Successful'" % (name1, country1, country1, name1)
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if not results:
            print("Empty set")
            return
        for x in results:
            print(x)
        con.commit()
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)

    return

def msr():
    print("msr")
    sys.stdout.flush()
    try:
        # query = "select count(s.Status)/count(tm.Status) as sr, misa1.Agency_Name, misa1.Agency_Country from mission tm, mission s, mission_agencies misa1, mission_agencies misa2 where tm.Name=misa1.Name and s.Name=misa2.Name and s.Status='Successful' group by misa1.Agency_Name, misa1.Agency_Country order by sr desc limit 1"
        query = " select count(distinct s.Name)/count(distinct tm.Name) as sr, misa1.Agency_Name, misa1.Agency_Country from mission tm, mission s, mission_agencies misa1, mission_agencies misa2 where tm.Name=misa1.Name and s.Name=misa2.Name and misa1.Agency_Name=misa2.Agency_Name and misa1.Agency_Country=misa2.Agency_Country and s.Status='Successful' group by misa1.Agency_Name, misa1.Agency_Country order by sr desc limit 1"
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if not results:
            print("Empty set")
        for x in results:
            print(x)
        con.commit()
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Error occured when updating")
        print(">>>>>>>", e)
        tmp = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def mfe():
    print("mfe")
    sys.stdout.flush()
    try:
        query = "select * from rocket R where R.Fuel_Efficiency=(select max(Fuel_Efficiency) from rocket)"
        cur.execute(query)
        results = cur.fetchall()
        if not results:
            print("Empty set")
        for x in results:
            print(x)
        con.commit()
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def acm():
    print("acm")
    sys.stdout.flush()
    try:
        query = "select A.AstronautID, A.Name from travelled_on T, astronauts A where A.AstronautID=T.AstronautID group by A.AstronautID order by count(distinct(T.Mission_Name)) desc limit 1"
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if not results:
            print("Empty set")
        for x in results:
            print(x)
        con.commit()
        tmp = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def mps():
    print("mps")
    sys.stdout.flush()
    try:
        name = input("Enter Mission Name: ")
        purpose = input("Enter Mission Purpose: ")
        cb = input("Enter the Celestial Body: ")
        payload = input("Enter the Payload weight available: ")
        timeline = input("Enter status of the mission (Past / Ongoing / Future): ")
        status = input("Enter Status(Failure / Success / Scrapped) if Past Mission, NULL otherwise: ")
        astronauts = input("Type 1 if astronauts are required and 0 if they aren't: ")
        oc = input("Type 1 if open for collaboration and 0 if not: ")
        if (status != "NULL"):
            query = """INSERT INTO mission VALUES('%s', %s, '%s', '%s', %s, %s, '%s', '%s')""" % (name, payload, timeline, status, oc, astronauts, purpose, cb)
        else:
            query = """INSERT INTO mission VALUES('%s', %s, '%s', NULL, %s, %s, '%s', '%s')""" % (name, payload, timeline, oc, astronauts, purpose, cb)
        pprint(query)
        cur.execute(query)
        con.commit()
        tmp = input("Press Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def asr():
    print("asr")
    sys.stdout.flush()
    try:
        name = input("Enter the Agency Name: ")
        country = input("Enter the Associated Country: ")
        pp = input("Type 1 if the agency is public and 0 if it is private: ")
        empno = input("Enter the number of employees: ")
        query = """INSERT INTO space_agencies VALUES('%s', '%s', %s, %s)""" % (country, name, pp, empno)
        pprint(query)
        cur.execute(query)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>", e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def udp():
    print("udp")
    sys.stdout.flush()
    try:
        model_name = input("Enter the rocket name: ")
        mission_name = input("Enter mission name")
        experiment_name = input("Enter experiment name")
        query = "update payload set Rocket_Name='%s' where Mission_Name='%s' and Experiment_Name='%s'" % (model_name, mission_name, experiment_name)
        pprint(query)
        cur.execute(query)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>", e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return
    
def arf():
    print("arf")
    sys.stdout.flush()
    try:
        mission_name = input("Enter the mission name: ")
        resource_name = input("Enter resource name: ")
        quantity = input("Enter the quantity for this resource: ")
        requestingAgCountry = input("Enter the requesting agency country: ")
        requestingAgName = input("Enter the requesting agency name: ")
        requestedFromCountry = input("Enter the country requested from: ")
        query = "insert into resources values ('%s', '%s', %s, '%s', '%s', '%s')" % (mission_name, resource_name, quantity, requestingAgCountry, requestingAgName, requestedFromCountry)
        pprint(query)
        cur.execute(query)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>", e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)

    return

def uga():
    print("uga")
    sys.stdout.flush()
    try:
        country = input("Enter the Country of the ambassador to be changed: ")
        agency = input("Enter the National Space Agency of the ambassador to be changed: ")
        name = input("Enter the Name of the new ambassador: ")
        nationality = input("Enter the Nationality of the new ambassador: ")
        contact = input("Enter the Contact Number of the new ambassador: ")
        query = """UPDATE Ambassador SET Name = '%s', Nationality = '%s', Contact_Number = '%s' WHERE Agency_Country = '%s' AND Agency_Name = '%s' """ % (name, nationality, contact, country, agency)
        pprint(query)
        cur.execute(query)
        con.commit()
        print("Inserted successfully!")
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def dpm():
    print("dpm")
    sys.stdout.flush()
    try:
        query = "DELETE FROM Mission WHERE Timeline = 'Future' AND Status = 'Scrapped'"
        pprint(query)
        cur.execute(query)
        con.commit()
        print("Removed successfully!")
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def drc():
    print("drc")
    sys.stdout.flush()
    try:
        query = "DELETE FROM Rocket WHERE Status = 'Scrapped'"
        pprint(query)
        cur.execute(query)
        con.commit()
        print("Removed successfully!")
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def rmp():
    print("rmp")
    sys.stdout.flush()
    try:
        mn = input("Enter the Mission Name for which a report must be generated: ")
        # query = """SELECT Experiment_Name,Weight,Sender_Name,Sender_Country FROM Payload WHERE Mission_Name='%s'""" % mn
        query = """select p.Experiment_Name,p.Weight,p.Sender_Name,p.Sender_Country,r.Resource_Name,r.Quantity,r.Requesting_Agency_Name,r.Requesting_Agency_Name,r.Country_Requested_From from payload p inner join resources r on r.Mission_Name=p.Mission_Name where p.Mission_Name='%s'""" % mn
        pprint(query)
        cur.execute(query)
        con.commit()
        results = cur.fetchall()
        if(len(results)==0):
            print("Empty set")
        for i in results:
            pprint(i)
        con.commit()
        # query = "select Resource_Name,Quantity,Requesting_Agency_Name,Requesting_Agency_Name,Country_Requested_From FROM Resources where Mission_Name='%s'" % mn
        # pprint(query)
        # cur.execute(query)
        # con.commit()
        # results = cur.fetchall()
        # if(len(results)==0):
        #     print("Empty set")
        # for i in results:
        #     pprint(i)
        # con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def nrr():
    print("nrr")
    sys.stdout.flush()
    try:
        name = input("Enter agency name: ")
        country = input("Enter agency country: ")
        num = input("Enter the minimum number of missions to search for: ")
        # query = "SELECT count(*) FROM Rocket r1 WHERE (r1.Model_Name) in (select r2.Model_Name as models From Rocket r2, Mission_Rockets mr, Mission m Where r2.Agency_Name='%s' and r2.Agency_Country='%s' and r2.Status=1 and r2.Reusable=1 and mr.Rocket_Model=r2.Model_Name and mr.Rocket_Agency_Name=r2.Agency_Name and mr.Rocket_Agency_Country=r2.Agency_Country and mr.Mission_Name=m.Name and m.Status='Successful' Group by Models Having count(distinct(mr.Mission_Name)) >= %s )" % (name, country, num)
        # query = "select count(*) from rocket r1 where (r1.Model_Name) in (select r2.Model_Name as models from rocket r2 inner join mission_rockets mr on ( mr.Rocket_Model=r2.Model_Name and mr.Rocket_Agency_Name=r2.Agency_Name and mr.Rocket_Agency_Country=r2.Agency_Country) inner join Mission m on mr.Mission_Name=m.Name where r2.Agency_Name='%s' and r2.Agency_Country='%s' and r2.Status=1 and r2.Reusable=1 and m.Status='Successful' Group by models Having count(distinct(mr.Mission_Name)) >= %s )" % (name,country,num)
        query = "select * from mission_rockets mr inner join rocket r on mr.Rocket_Model=r.Model_Name and mr.Rocket_Agency_Country=r.Agency_Country and mr.Rocket_Agency_Name=r.Agency_Name where Agency_Country='%s' and Agency_Name='%s' and Reusable=1 and (select count(distinct Mission_Name) from mission_rockets where Rocket_Model=Model_Name and Rocket_Agency_Country=Agency_Country and Rocket_Agency_Name=Agency_Name group by Rocket_Model, Rocket_Agency_Country, Rocket_Agency_Name) >= %s" % (country, name, num)
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if(len(results)==0):
            print("Empty set")
        for i in results:
            pprint(i)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def tmt():
    print("tmt")
    sys.stdout.flush()
    try:
        name = input("Enter the agency for whom you need average fuel efficiency: ")
        country = input("Enter the country the agency is based in: ")
        query = "SELECT Agency_Name, Agency_Country, avg(Fuel_Efficiency) FROM Rocket WHERE Agency_Name = '%s' AND Agency_Country = '%s'" % (name,country)
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if(len(results)==0):
            print("Empty set")
        for i in results:
            pprint(i)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def spm():
    print("spm")
    sys.stdout.flush()
    try:
        purp = input("Enter the Purpose: ")
        query = "select * from Mission where Purpose like '%%%s%%'" % purp
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if(len(results)==0):
            print("Empty set")
        for i in results:
            pprint(i)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

def pee():
    print("pee")
    sys.stdout.flush()
    try:
        purp = input("Enter the Experiment: ")
        query = "select * from Payload where Experiment_Name like '%%%s%%'" % (purp)
        pprint(query)
        cur.execute(query)
        results = cur.fetchall()
        if(len(results)==0):
            print("Empty set")
        for i in results:
            pprint(i)
        con.commit()
        tmp1 = input("Enter to continue")
    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>",e)
        tmp2 = input("Enter to continue")
    tmp = sp.run("cls", shell=True)
    return

perms = dict()
perms["S"] = list()
perms["U"] = list()
perms["C"] = list()
perms["A"] = list()
perms["G"] = list()
perms["D"] = list()

functions = dict()
func_calls = dict()

#  GSA
functions["GSA"] = "Get all space agencies participating in a mission"
func_calls["GSA"] = gsa
perms["S"].append("GSA")
perms["U"].append("GSA")
perms["C"].append("GSA")
perms["A"].append("GSA")
perms["G"].append("GSA")
perms["D"].append("GSA")

# RSA
functions["RSA"] = "Get all rockets developed by space agency 1 that have taken space agency 2 payload to the moon"
func_calls["RSA"] = rsa
perms["S"].append("RSA")
perms["U"].append("RSA")
perms["A"].append("RSA")
perms["G"].append("RSA")

# GSM
functions["GSM"] = "Get space missions which can support payloads more than N kgs"
func_calls["GSM"] = gsm
perms["S"].append("GSM")
perms["U"].append("GSM")

# FMS
functions["FMS"] = "Find missions a space agency has sent to a celestial body"
func_calls["FMS"] = fms
perms["S"].append("FMS")
perms["U"].append("FMS")
perms["C"].append("FMS")
perms["A"].append("FMS")
perms["G"].append("FMS")
perms["D"].append("FMS")

# GAS
functions["GAS"] = "Get the average success ratio of a particular space agency"
func_calls["GAS"] = gas
perms["S"].append("GAS")
perms["U"].append("GAS")
perms["A"].append("GAS")
perms["C"].append("GAS")

# MSR
functions["MSR"] = "Get the space agency with the maximum success rate"
func_calls["MSR"] = msr
perms["S"].append("MSR")
perms["U"].append("MSR")
perms["A"].append("MSR")

# MFE
functions["MFE"] = "Get most fuel efficient rocket"
func_calls["MFE"] = mfe
perms["S"].append("MFE")
perms["U"].append("MFE")
perms["C"].append("MFE")
perms["A"].append("MFE")
perms["G"].append("MFE")
perms["D"].append("MFE")

# ACM
functions["ACM"] = "Get astronaut that has completed the most missions"
func_calls["ACM"] = acm
perms["S"].append("ACM")
perms["A"].append("ACM")
perms["C"].append("ACM")

# MPS
functions["MPS"] = "Insert a new mission along with payload specifications"
func_calls["MPS"] = mps
perms["S"].append("MPS")

# ASR
functions["ASR"] = "Add a space agency and their associated representative"
func_calls["ASR"] = asr
perms["D"].append("ASR")
perms["G"].append("ASR")

# UDP
functions["UDP"] = "Update Rocket of payload"
func_calls["UDP"] = udp
perms["S"].append("UDP")

# ARF
functions["ARF"] = "Add resources needed for a particular mission"
func_calls["ARF"] = arf
perms["S"].append("ARF")

# UGA
functions["UGA"] = "Update the government ambassador for a country"
func_calls["UGA"] = uga
perms["G"].append("UGA")

# DPM
functions["DPM"] = "Delete scrapped missions"
func_calls["DPM"] = dpm
perms["S"].append("DPM")

# DRC
functions["DRC"] = "Delete all scrapped rockets"
func_calls["DRC"] = drc
perms["S"].append("DRC")

# RMP
functions["RMP"] = "Get a report of all external materials and products acquired for a mission by a space agency"
func_calls["RMP"] = rmp
perms["G"].append("RMP")
perms["D"].append("RMP")

# NRR
functions["NRR"] = "Get number of rockets developed by a space agency that are reusable and have been used on at least n missions"
func_calls["NRR"] = nrr
perms["D"].append("NRR")
perms["S"].append("NRR")
perms["C"].append("NRR")

# TMT
functions["TMT"] = "Get Average Fuel Efficiency of a Space Agency"
func_calls["TMT"] = tmt
perms["D"].append("TMT")
perms["S"].append("TMT")
perms["C"].append("TMT")

# SPM
functions["SPM"] = "Partially search for the purpose of a mission (like mission related to humans being sent to space, or planetary exploration with probes, …etc)"
func_calls["SPM"] = spm
perms["C"].append("SPM")
perms["D"].append("SPM")
perms["G"].append("SPM")

# PEE
functions["PEE"] = "Partially search for a payload by experiment name (example: Search for zero gravity)"
func_calls["PEE"] = pee
perms["U"].append("PEE")

def prompt():
    print("""To continue, please enter the letter specified by your role:\n
Format: Role (Letter to Enter)
1. Space Agency (S)
2. University (U)
3. Scientist (U)
4. Lab (U)
5. Observatory (U)
6. Casual User (C)
7. Astronaut (A)
8. Government Agency (G)
9. UN Department (D)
10. Exit the application (E)""")
    user = input("Please enter your role: ")
    return user

def queries(user):
    tmp = sp.run("cls", shell=True)
    print("Available queries:\nFormat: Query details (code)")
    for i in range(len(perms[user])):
        print(i+1,". ",functions[perms[user][i]]," (",perms[user][i],")",sep="")
    print(len(perms[user]) + 1,". Logout of current user mode (L)", sep="")
    c = input("Enter the code of the query you need to run: ")
    if(c not in perms[user] and c!="L"):
        print("Invalid code")
        return 'inv'
    return c

print("\nWelcome to the official Application of the United Nations Space Exploration Division.")
# init_db()

def agency():
    print("\nHello Space Agency!\n")
    while(1):
        c = queries("S")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return

def client():
    print("\nHello Intellectual!\n")
    while(1):
        c = queries("U")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return

def casual():
    print("\nHello Layman!\n")
    while(1):
        c = queries("C")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return

def ast():
    print("\nHello Astronaut!\n")
    while(1):
        c = queries("A")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return

def govt():
    print("\nHello Government!\n")
    while(1):
        c = queries("G")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return

def un():
    print("\nHello United Nations!\n")
    while(1):
        c = queries("D")
        if(c=="inv"):
            continue
        elif(c=="L"):
            break
        else:
            func_calls[c]()
    return



username = input("Database username: ")
# password = input("Database Password: ")

try:
    con = pymysql.connect(host='127.0.0.1',
                            port=3307,
                            user=username,
                            passwd=getpass.getpass("Password: "),
                            db='UNSED',
                            cursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor()
    tmp = sp.call('cls', shell=True)
    if(con.open):
        print("Connected")
    else:
        print("Failed to connect")

    tmp = input("Enter any key to CONTINUE>")
except Exception as e:
    tmp = sp.call('cls', shell=True)
    print(e)
    print("Connection Refused: Either username or password is incorrect")
    exit()

while(1):
    tmp = sp.run("cls", shell=True)
    user = prompt()
    
    if(user=="E"):
        print("Goodbye.\n")
        break

    elif(user == 'S'):
        agency()
        continue

    elif(user == 'U'):
        client()
        continue
    
    elif(user == 'C'):
        casual()
        continue

    elif(user == 'A'):
        ast()
        continue

    elif(user == 'G'):
        govt()
        continue

    elif(user == 'D'):
        un()
        continue

    else:
        print("\nInvalid role. Please try again")
        continue

# for j in range(20):
#     x=input()
#     k = "func_calls[\""
#     for i in range(len(x)):
#         if(x[i]=="["):
#             k += x[i+2:i+5]
#             k += "\"] = "
#             k += x[i+2:i+5].lower()
#             break
#     print(x)
#     print(k)
"""
describe ambassador;
+----------------------+-------------+------+-----+---------+-------+
| Field                | Type        | Null | Key | Default | Extra |
+----------------------+-------------+------+-----+---------+-------+
| Agency_Country       | varchar(64) | NO   | PRI | NULL    |       |
| Agency_Name          | varchar(64) | NO   | PRI | NULL    |       |
| Name                 | varchar(64) | NO   | PRI | NULL    |       |
| Nationality          | varchar(64) | NO   |     | NULL    |       |
| Contact_Number       | varchar(32) | YES  |     | NULL    |       |
| Super_Agency_Country | varchar(64) | YES  | MUL | NULL    |       |
| Super_Agency_Name    | varchar(64) | YES  |     | NULL    |       |
| Super_Name           | varchar(64) | YES  |     | NULL    |       |
+----------------------+-------------+------+-----+---------+-------+
space_agencies
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| Country | varchar(64) | NO   | PRI | NULL    |       |
| Name    | varchar(64) | NO   | PRI | NULL    |       |
| Public  | tinyint(1)  | NO   |     | NULL    |       |
| EmpNo   | int         | YES  |     | 0       |       |
+---------+-------------+------+-----+---------+-------+
 describe astronauts;
+----------------+---------------------------+------+-----+---------+----------------+
| Field          | Type                      | Null | Key | Default | Extra          |
+----------------+---------------------------+------+-----+---------+----------------+
| AstronautID    | int(10) unsigned zerofill | NO   | PRI | NULL    | auto_increment |
| Name           | varchar(64)               | NO   |     | NULL    |                |
| Nationality    | varchar(64)               | YES  |     | NULL    |                |
| Mission_Status | varchar(64)               | NO   |     | NULL    |                |
+----------------+---------------------------+------+-----+---------+----------------+
describe collaboration;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| Mission_Name    | varchar(64) | NO   | PRI | NULL    |       |
| Agency1_Country | varchar(64) | NO   | PRI | NULL    |       |
| Agency1_Name    | varchar(64) | NO   | PRI | NULL    |       |
| Agency2_Country | varchar(64) | NO   | PRI | NULL    |       |
| Agency2_Name    | varchar(64) | NO   | PRI | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
 describe contract;
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| Mission_Name   | varchar(64)  | NO   | PRI | NULL    |       |
| AstronautID    | int unsigned | NO   | PRI | NULL    |       |
| Agency_Country | varchar(64)  | NO   | PRI | NULL    |       |
| Agency_Name    | varchar(64)  | NO   | PRI | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
describe employee;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| EmployeeID  | varchar(10) | NO   | PRI | NULL    |       |
| Name        | varchar(64) | NO   |     | NULL    |       |
| Nationality | varchar(64) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
 describe mission;
+------------------------+--------------+------+-----+---------+-------+
| Field                  | Type         | Null | Key | Default | Extra |
+------------------------+--------------+------+-----+---------+-------+
| Name                   | varchar(64)  | NO   | PRI | NULL    |       |
| Available_Payload      | int          | YES  |     | NULL    |       |
| Timeline               | varchar(64)  | NO   |     | NULL    |       |
| Status                 | varchar(64)  | YES  |     | NULL    |       |
| Open_for_Collaboration | tinyint(1)   | YES  |     | NULL    |       |
| Astronauts_Required    | tinyint(1)   | YES  |     | NULL    |       |
| Purpose                | varchar(256) | NO   |     | NULL    |       |
| Celestial_Body         | varchar(64)  | YES  |     | NULL    |       |
+------------------------+--------------+------+-----+---------+-------+
 describe mission_agencies;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| Name           | varchar(64) | NO   | PRI | NULL    |       |
| Agency_Country | varchar(64) | NO   | PRI | NULL    |       |
| Agency_Name    | varchar(64) | NO   | PRI | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
 describe mission_rockets;
+-----------------------+-------------+------+-----+---------+-------+
| Field                 | Type        | Null | Key | Default | Extra |
+-----------------------+-------------+------+-----+---------+-------+
| Mission_Name          | varchar(64) | NO   | PRI | NULL    |       |
| Rocket_Model          | varchar(64) | NO   | PRI | NULL    |       |
| Rocket_Agency_Country | varchar(64) | NO   | PRI | NULL    |       |
| Rocket_Agency_Name    | varchar(64) | NO   | PRI | NULL    |       |
+-----------------------+-------------+------+-----+---------+-------+
 describe payload;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| Mission_Name    | varchar(64) | NO   | PRI | NULL    |       |
| Experiment_Name | varchar(64) | NO   | PRI | NULL    |       |
| Weight          | int         | NO   |     | NULL    |       |
| Sender_Country  | varchar(64) | NO   | MUL | NULL    |       |
| Sender_Name     | varchar(64) | NO   |     | NULL    |       |
| Rocket_Name     | varchar(64) | NO   | MUL | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
 describe resources;
+---------------------------+-------------+------+-----+---------+-------+
| Field                     | Type        | Null | Key | Default | Extra |
+---------------------------+-------------+------+-----+---------+-------+
| Mission_Name              | varchar(64) | NO   | PRI | NULL    |       |
| Resource_Name             | varchar(64) | NO   | PRI | NULL    |       |
| Quantity                  | int         | YES  |     | NULL    |       |
| Requesting_Agency_Country | varchar(64) | NO   | MUL | NULL    |       |
| Requesting_Agency_Name    | varchar(64) | NO   |     | NULL    |       |
| Country_Requested_From    | varchar(64) | YES  |     | NULL    |       |
+---------------------------+-------------+------+-----+---------+-------+
describe resource_request;
+----------------------------+-------------+------+-----+---------+-------+
| Field                      | Type        | Null | Key | Default | Extra |
+----------------------------+-------------+------+-----+---------+-------+
| Mission_Name               | varchar(64) | NO   | PRI | NULL    |       |
| Resource_Name              | varchar(64) | NO   | PRI | NULL    |       |
| Ambassador1_Agency_Country | varchar(64) | NO   | MUL | NULL    |       |
| Ambassador1_Agency_Name    | varchar(64) | NO   | PRI | NULL    |       |
| Ambassador1_Name           | varchar(64) | NO   | PRI | NULL    |       |
| Ambassador2_Agency_Country | varchar(64) | NO   | PRI | NULL    |       |
| Ambassador2_Agency_Name    | varchar(64) | NO   | PRI | NULL    |       |
| Ambassador2_Name           | varchar(64) | NO   | PRI | NULL    |       |
| EmployeeID                 | varchar(10) | NO   | PRI | NULL    |       |
| Agency_Country             | varchar(64) | NO   | PRI | NULL    |       |
| Agency_Name                | varchar(64) | NO   | PRI | NULL    |       |
+----------------------------+-------------+------+-----+---------+-------+
describe rocket;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| Model_Name      | varchar(64)  | NO   | PRI | NULL    |       |
| Agency_Country  | varchar(64)  | NO   | PRI | NULL    |       |
| Agency_Name     | varchar(64)  | NO   | PRI | NULL    |       |
| Max_Payload     | int          | YES  |     | NULL    |       |
| Fuel_Type       | varchar(64)  | YES  |     | NULL    |       |
| Cost            | int          | YES  |     | NULL    |       |
| Year_First_Use  | date         | YES  |     | NULL    |       |
| Engines         | varchar(128) | YES  |     | NULL    |       |
| Status          | varchar(64)  | YES  |     | NULL    |       |
| Fuel_Efficiency | decimal(5,2) | YES  |     | NULL    |       |
| Reusable        | tinyint(1)   | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
 describe space_agency_locations;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| Country  | varchar(64)  | NO   | PRI | NULL    |       |
| Name     | varchar(64)  | NO   | PRI | NULL    |       |
| Location | varchar(128) | NO   | PRI | NULL    |       |
+----------+--------------+------+-----+---------+-------+
 describe travelled_on;
+-----------------------+--------------+------+-----+---------+-------+
| Field                 | Type         | Null | Key | Default | Extra |
+-----------------------+--------------+------+-----+---------+-------+
| Mission_Name          | varchar(64)  | NO   | PRI | NULL    |       |
| Rocket_Model          | varchar(64)  | NO   | PRI | NULL    |       |
| Rocket_Agency_Country | varchar(64)  | NO   | PRI | NULL    |       |
| Rocket_Agency_Name    | varchar(64)  | NO   | PRI | NULL    |       |
| AstronautID           | int unsigned | NO   | PRI | NULL    |       |
+-----------------------+--------------+------+-----+---------+-------+
"""