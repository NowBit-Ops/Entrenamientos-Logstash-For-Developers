import random
from datetime import datetime, timedelta
import time
from faker import Faker
import uuid
import names
# from elasticsearch import Elasticsearch
import socket
import json
import json
from uuid import UUID


def uuid_convert(o):
    if isinstance(o, UUID):
        return o.hex


UDP_IP = '172.31.15.165'
UDP_PORT = 25000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

faker = Faker()

# es = Elasticsearch(

# 	    "elastic:LT3SWnO63cxAbssAL9M5LOTU@317e264e55a744fa857e3c0e68c5ab99.us-east-1.aws.found.io:9243",
#         verify_certs=False,
# 	    scheme="https",
# 	    request_timeout=30
# 	)
user = {}
now = datetime(2021, 1, 1)
UsusariosAnomalos=[]
total=0
while True:


    secondsSinceEpoch = time.time()
    name = random.choice(["William Boyd","Angie Ford","Carl Adkins","Rafael Seiberling","Johnny Stewart","Rosa Novak","Sammie Kutz","Hortencia Olvera","Rick Vermillion","Rosie Ward","Christopher Bullock","Brenda Snyder","Andrew Groth","Randy Campbell","Teresa Robbins","John Jones","David Story","John Zaring","Jared Brady","Etta Duvall","Zachery Martin","Vincent Caver","Elijah Kelly","Bridget Lapalme","Richard Haggard","Greg Guajardo","William Vanschaick","James Gover","Janice Pope","Mitsuko Smelley","Deborah Kim","Carol Rodriguez","Louis Bunch","Allen Malinsky","Willie Lopez","Rebecca Petersen","Fawn Reid","William Williams","Maxine Berlin","Wallace Blaney","Nicole Taylor","Josiah Gerrior","Carol Fuller","Velma Strother","Craig Cola","Sara Yaney","Angela Barber","Catherine Mendoza","Carl Humphrey","Kristen Cates","Heather Young","Allen Wood","Jeffrey Marquess","Joyce Villaman","Conrad Walsh","Alma Wright","Robert Richardson","Heather Salinas","Irwin Jones","Ann Hamby","Steven Kokoska","Emily Ray","Timothy Wright","Russell Housley","Gerald Ford","Marvin Amen","Crystal Randazzo","Todd Wilkes","Victoria Basinski","Diane Butler","Richard Girouard","Deborah Jones","Betty Bartberger","Jennifer Rose","Sherry Kestler","Roxann Steen","James Estep","Lee Pedley","Brenda Snow","Sylvia Edward","Mary Putman","Joseph Grassi","Lawerence Ellis","Craig Kirk","Carmen Namm","Heather Arroyo","Lucille Nieves","Penny Enright","Alissa Butler","Michael Nelson","Dennis Woods","Casey Wahl","Richard Odell","Charles Bentz","Martin Kistler","Nancy Watson","Kendrick Kha","Renee Tomsic","Thomas Senz","Samuel Sheikh","Ralph Mathies","Travis Mcbee","Margaret Singh","Shawn Santana","Margaret Delgiudice","Sherry Reyes","Henry Price","David Weber","Milton Utley","Norma Margulis","Gregory Bergmark","Minnie Reyes","Mark Odell","Rebecca Flory","Harriet Huber","James Neeley","Judith Floer","Robert Hinton","Ricardo Chambers","Paul Schlosser","Patrick Williams","Jolene Macfarlane","Magnolia Anthony","Katherine Weaver","Pat Funk","Debra Rena","Antonio Beale","Sylvia Glenn","Joshua Cooper","James Baumgardner","Thomas Kruse","Hazel Werth","Edward Forrester","Myrl Ammon","Tara Huitink","Jerome Morales","Marvin Rubio","Heather Hutchison","Ruth Marks","Stewart Williams","Mark Jones","Audrey Cedeno","Laurie Woodard","James Mickens","Jillian Tinsley","Sandra Bromley","Lawrence Battista","Joseph Devoy","Jeffrey Larrabee","Sally Leandro","Andrea Madsen","Johnathon Campbell","Kevin Valentine","Stephen Rao","Ray Hachey","Angel Wimberly","Vicente Khouri","Frances Franklin","Francisco Wood","Tracy Gardener","Steve Steele","Robert Wilson","Nancy Cronan","Larry Krokos","David Harper","Anthony Johnson","Evelyn Burton","Patrick Guedry","Harry Marks","Jason Force","Donna Chavira","Jeffery Loggins","Richard Merchant","Geoffrey Walker","Walter Stovall","Timothy Purcell","Brenda Taylor","Archie Johnson","Sandra Shea","Melvin Gellings","Nathan Baker","Mable Molina","Aaron Sifuentes","Victor Graves","Alfonso Martinez","Allan Jaeger","Stanley Cahill","Raymond White","John Robertson","Chi Quivers","David Lung","Helene Edwards","Daniel Kranz","Cynthia Escobedo","Kenny Todd","Robert Conkle","Roderick Wade","Julie Collins","Silvia White","Terry Kettner","Marvin Harvey","Dianne Pace","Christine Sanon","James Cavender","Chris Moyer","Angela Siple","Donald Cook","Evelyn Lamboy","Laura Shurtz","Paula Roberts","Mary Watkins","Arthur Cross","Mary Martell","Eddie Parrish","Grace Lavin","Ramona Harrell","David Abrams","Mary Goldfarb","Donna Kiser","Regina Zarella","William Anders","Robert Gaylor","Beulah Davila","Tyson Macpartland","Vincent Bergstresser","Max Foreman","Leonard Mathis","George Anderson","Mariah Cheatam","Joe Kunze","Carol Ackerman","David Stewart","Matthew Cass","Kathy Fowler","Mike Savage","Raymond Merideth","Arthur Pruitt","Sharyn Rodriquez","Kenneth Gomez","Rogelio Frick","Lamar Velez","Genaro Mcelreavy","Paul Cantrell","James Young","Leonard Stinson","James Goble","Rachel Joyner","Fred Tibbles","Adrianna Johnson","Cheryl Miller","Jeffrey Brown","Bruce Beamon","Kevin Cox","Sylvia Maroney","Ernest Titcomb","Mary Rector","Eric Young","Linda Bloomquist","Tonya Wortham","Dawn Garza","David Cain","Ruth Omara","Blanche Garnett","Suzette Vause","Annie Conorich","Lindsey Lopez","James Bishop","Andrew Almond","Floyd Murphy","Crystal Larson","Stacey Sealey","Jose Pea","Charlene Mettler","Roy Driskell","Emma Mock","Angela Bridwell","Elizabeth Howard","Patricia Fleming","Scott Dilorenzo","Enrique Hudson","Rick Oneil","Carol Arnold","Christopher Morris","Dwight Hopping","Jack Coverdale","Susan Betancourt","Ronald Aldridge","Angela Person","Carolina Steven","Holly Karter","Deborah Ortiz","Milton Ruderman","Tawnya Voegele","Roy Cervantes","Lynn Santos","Maria Walker","Eva Mitchell","Billy Price","Jewell Collins","Leann Walter","Henry Balius","Diane Newcomb","Mary Lehtonen","Ronald Mcconnell","Barbara Muir","Dorothy Cushman","Melissa Moore","Robert Alexander","Larissa Sweatt","Gloria Wall","Nola Brown","Cecil Weil","Margaret Lueth","Gabriel Tyrer","Ruth Gray","Ronald Taylor","Gayla Felton","John Sandigo","Tracey Goods","Roberta Tran","Robert Giacomini","Barbara Kline","Michael Furrer","Melissa Vargas","Matthew Metevier","Kathryn Phillis","Mary Eike","Corey Sanders","Gary Matheis","William Ross","Rachel Musick","John Bush","Leslie Smith","Benjamin Cable","Nicholas Lee","Mitchell Reff","Ryan Garrett","Duane Fiala","Daniel Paul","Prudence Parker","Tony Miller","Maria Ramirez","Lori Perry","Samuel Devenport","Tammy Maymon","Monica Sedlacek","Bessie Toulouse","Keith Wilson","Marie Gentry","Warren Harrod","Jason Maxson","Jeffrey Forte","Frances Oppegard","Raymond Creek","David Lewis","Jeanie Boutte","Corliss Boris","Matthew Etter","Maribel Bean","Spencer Henkel","Joyce Nelson","Novella Mercado","Blake Samuels","Sandra Hail","Garry Hunter","William Goodrich","Raymond Gerth","Howard Herriott","John Williams","Marcelle Weekley","Harriett Eastwood","Burl Davis","Cecil Townsend","Amy Lambert","Susan Rubin","Scott Belton","Lauren Lowry","Alana Evans","David Newton","Everett Kantor","Jeffrey Stills","Joan Watlington","Ernesto Gomez","Michael Jones","Laverne Romero","Robert Lyons","Gerald Brixey","Betty Schmidt","Shirley Davis","Anita Morris","Christine Honey","Erica Ketterman","Catherine Dufresne","Angela Quintero","Teddy Garner","Barbara Riddell","Muriel Grier","Pauline Nall","Monica Collins","Francisco Tobin","Laurence Mann","Ismael Aldridge","Elizabeth Niederberger","Janet Belcher","Deana Moher","Maurice Longshore","Casey Moore","Betty Williams","Martha Belcher","Danny Jimenez","George Spivey","Charles Spannaus","Carlos Monaco","Mary Dowdell","Christopher Bailey","Sheldon Wilson","Amy Roberts","Sheila Hayes","Richard Phelps","John Tenney","Lucille Hovermale","Virginia Gill","Eric Stebner","Lesley Morris","Florence Gulledge","Steve Donato","Elizabeth Williams","Latonya Blair","Christopher Conzemius","Steven Achee","Jo Rodriguez","Deanna Reighard","Jerry Bailey","Ryan Mcclain","Tonya Dondero","David Spritzer","Steven Rivera","Margaret Donahue","Marguerite Berlin","Florence Ellman","Marion Hale","Daniel Sparrow","Mattie Almonte","Robert Ayers","Elizabeth Skinner","Pauline Dumas","Charles Waller","Sophie Capps","Laura Thompson","Pedro Mushrush","Stephen Moody","Linda Moorer","James Starkey","Lucinda Roundtree","John Little","Pamela Salvador","Lon Zimmer","Horace Arguello","Maria Longley","Eduardo Kelly","Dorris Smith","Mallory Wheeler","William Sutton","Denise Kauffman","Elaine Anderson","Gilbert Hill","Shirley Nowak","Kevin Henderson","Rosie Pena","Andrew Heath","Edith Platt","Dennis Manuel","Grace Simpson","David Whitfield","Debra Leonard","Robin Niswander","Virginia Robinson","Rhonda Matusz","James Johnson","Rebecca Muraro","Jesse Jones","Randall Maurer","George Hall","Barbara Chiarini","Thomas Owczarzak","Lorenzo Simmons","Spencer Ramos","Sheila Webster","Rene Beard","Patricia Parsons","Mildred Washington","Lloyd Cochrane","Bradley Cook","Patricia Rohling","Ben Stevens","Todd Torbert","William Hester","Bonnie Paneto","Dale Haskins","William Perez","Judith Riley","Carolee Hamilton","Sheldon Leday","Lionel Bogar","Virginia Dougherty","Robert Munson","Barry Meiners","Kimberly Harrington","Traci Farris","Chris Willemsen","Millie Holquin","Jennifer Rabello","Paul Lemm","Brigette Jackson","Timothy Barton","Monica Barron","Ellen Sichler","James Mullins","Frank Martinson","Marty Ortiz","Bob Dahlman","Esperanza Yingst","Marvin Renick","Mark Spencer","Sarah Menendez","Walter Hall","Annette Kolling","Tara Tristan","Adele Renfro","James Longoria","Angela Fenton","Timothy Mahoney","Virgina Young","Kimberly Mitchell","Betty Dowell","Mildred Jacobs","Kimberly Bush","Monique Lindsey","Annie Simmons","Sabrina Hall","Douglas Cervantes","Stephen Johnston","Rudy Johnson","John Geesey","Jose Donley","Randall Henson","Virginia Lenton","Dan Laird","Philip Green","Kimberly Collins","George Burkholder","Earnest Lusk","Ann Lenz","Gabriela Weaver","Julie Randolph","Donald Clay","Paul Raper","Allie Burton","Milton Ward","Jared Lieberman","Jayne Mao","Antonio Huff","Karen Tibbits","Elenor Moreno","Lillian Price","Dorothy Mccabe","Denise Arneecher","Clifton Weaver","Elaine Adams","Jeffrey Reyes","David Cummings","Casey Williams","John Griffin","Elizabeth Collier","Harold Manning","Robert Vaillancourt","Janie Aldape","Ruben Fuller","John Rivers","Raymond Singletary","Samantha Beaushaw","James Bosley","Amy Molina","Mary Johnson","Kenneth Testa","Kevin Brainard","Darryl Zahler","Philip Anderson","Bill Gee","Tarsha Mcclure","Charles Leisure","Richard Roark","Michael Mayeux","Daniel Shaw","Arvilla Herrera","Andrea Fulbright","Betty Jacobs","Dominique Rowan","Craig Owens","Tom Doyel"])
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    regTime = now.strftime("%Y-%m-%dT%H:%M:%S%z")

    if name in user:
        if len(UsusariosAnomalos) < 30 or name in UsusariosAnomalos:
            if name in UsusariosAnomalos: 
                probanomalia = 10
            else:
                probanomalia = 2
            if (random.randint(0, 100) < probanomalia):
                if not name in UsusariosAnomalos: 
                    UsusariosAnomalos.append(name)
                if (random.randint(0, 100) < 30):
                    email = faker.email()
                else:
                    email = user[name]['user']['email']
                source = random.choice(["WEB", "APP"])
                ip_addr = faker.ipv4()

                if (source == "WEB"):
                    agent = random.choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "APP", "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0)",
                                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)", "Mozilla/5.0 (Windows NT 6.1; WOW64) "])
                else:
                    agent = random.choice(["Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv)", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X)",
                                        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X)", "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv)"])
                contentLength = random.randint(256, 1024)
                refer = random.choice(["https://dev-apps.datacredito.com.co/raw/user-account/login/web/index",
                                    "https://dev-apps.datacredito.com.co/raw/user-account/login/web/index?", "https://dev-apps.datacredito.com.co/raw/user-account/login/web/index?conCaptcha"])
                lenguage = random.choice(
                    ["es-ES,es;q=0.9,en;q=0.8", "en-US,en;q=0.5,en;q=0.8"])
                secondIp = ip_addr + ", " + faker.ipv4()
                myuuid = uuid.uuid4()
                company = (random.choice(["Montoya Industries", "Banco Centroaviario", "Comtast S.A.", "Kibana GMBH",
                                        "Elastic Enterprises", "Super almacenes la Guayaba", "Almacenes Logstash", "Beats Company", "NowBit SAS", "Guzmán Enterprises"]))
                regTime = now.strftime("%Y-%m-%dT%H:%M:%S%z")
                id_user = str(random.randint(79627749, 79628749))
                user[name] = {
                    "wasAnomaly": True,
                    "user": {
                        "id": id_user,
                        "email": email,
                        "full_name": name
                    },
                    "date_epoc": str(secondsSinceEpoch),
                    "source": source,
                    "@timestamp": regTime,
                    "client": {
                        "ip": ip_addr
                    },
                    "user-agent": {
                        "original": agent
                    },
                    "accept-encoding": "gzip, deflate, br",
                    "sec-fetch-dest": "empty",
                    "accept": "application/json, text/javascript, */*; q=0.01",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-requested-with": "XMLHttpRequest",
                    "content-length": contentLength,
                    "url": {
                        "original": refer,
                        "port": "443",
                        "scheme": "https",
                        "domain": "https://dev-apps.datacredito.com.co"
                    },
                    "incap-client-ip": ip_addr,
                    "incap-proxy-238": "OK",
                    "host": {
                        "hostname":
                        "dev-apps.datacredito.com.co"
                    },
                    "accept-language": lenguage,
                    "content-type": "multipart/form-data; charset=UTF-8",
                    "x-request-start": 1587515606051,
                    "cookie": "segment=conex; WEBSERVERSESSIONID=368873B84563723DBF94604BAD3FA2CF; JSESSIONID=8a3d0887-f799-4aba-82cf-fc7353015bee",
                    "x-forwarded-for": secondIp,
                    "via": "1.1 spaces-router (00a6e5b0e835)",
                    "event": {
                        "id": myuuid
                    },
                    "apphub-framework-001": """{"placeholders":{"environment":"dev-apps.datacredito.com.co","apphub":"//dev-apps.datacredito.com.co","apphub.port":"","apphub.tunnel":"/raw","browser.family":"CHROME","browser.version":"80.0.3987.163","browser.version.major":"80","browser.version.minor":"0"}}""",
                    "organization": {"name": company}
                }
            else:
                user[name]['date_epoc'] = str(secondsSinceEpoch)
                user[name]['date_epoc'] = dt_string,
                user[name]['@timestamp'] = regTime
        else:
            user[name]['date_epoc'] = str(secondsSinceEpoch)
            user[name]['date_epoc'] = dt_string,
            user[name]['@timestamp'] = regTime
    else:
        email = faker.email()
        source = random.choice(["WEB", "APP"])
        ip_addr = faker.ipv4()

        if (source == "WEB"):
            agent = random.choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "APP", "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0)",
                                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)", "Mozilla/5.0 (Windows NT 6.1; WOW64) "])
        else:
            agent = random.choice(["Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv)", "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X)",
                                   "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X)", "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv)"])
        contentLength = random.randint(256, 1024)
        refer = random.choice(["https://dev-apps.datacredito.com.co/raw/user-account/login/web/index",
                               "https://dev-apps.datacredito.com.co/raw/user-account/login/web/index?", "https://dev-apps.datacredito.com.co/raw/user-account/login/web/index?conCaptcha"])
        lenguage = random.choice(
            ["es-ES,es;q=0.9,en;q=0.8", "en-US,en;q=0.5,en;q=0.8"])
        secondIp = ip_addr + ", " + faker.ipv4()
        myuuid = uuid.uuid4()
        company = (random.choice(["Montoya Industries", "Banco Centroaviario", "Comtast S.A.", "Kibana GMBH",
                               "Elastic Enterprises", "Super almacenes la Guayaba", "Almacenes Logstash", "Beats Company", "NowBit SAS", "Guzmán Enterprises"]))
        regTime = now.strftime("%Y-%m-%dT%H:%M:%S%z")
        id_user = str(random.randint(79627749, 79628749))
        user[name] = {
            "wasAnomaly": False,
            "user": {
                "id": id_user,
                "email": email,
                "full_name": name
            },
            "date_epoc": str(secondsSinceEpoch),
            "source": source,
            "@timestamp": regTime,
            "client": {
                "ip": ip_addr,
            },
            "user-agent": {
                "original": agent
            },
            "accept-encoding": "gzip, deflate, br",
            "sec-fetch-dest": "empty",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "content-length": contentLength,
            "url": {
                "port": "443",
                "original": refer,
                "scheme": "https",
                "domain": "https://dev-apps.datacredito.com.co"
            },
            "incap-client-ip": ip_addr,
            "incap-proxy-238": "OK",
            "host": {
                "hostname": "dev-apps.datacredito.com.co"
            },
            "accept-language": lenguage,
            "content-type": "multipart/form-data; charset=UTF-8",
            "x-request-start": 1587515606051,
            "cookie": "segment=conex; WEBSERVERSESSIONID=368873B84563723DBF94604BAD3FA2CF; JSESSIONID=8a3d0887-f799-4aba-82cf-fc7353015bee",
            "x-forwarded-for": secondIp,
            "via": "1.1 spaces-router (00a6e5b0e835)",
            "event": {
                "id": myuuid
            },
            "apphub-framework-001": """{"placeholders":{"environment":"dev-apps.datacredito.com.co","apphub":"//dev-apps.datacredito.com.co","apphub.port":"","apphub.tunnel":"/raw","browser.family":"CHROME","browser.version":"80.0.3987.163","browser.version.major":"80","browser.version.minor":"0"}}""",
            "organization": {
                "name": company
            }
        }
    data = user[name]

    #print(data)
    message = json.dumps(data, default=uuid_convert).encode('utf-8')
    sock.sendto(message, (UDP_IP, UDP_PORT))
#    es.index(index='expirian', body=data)
    now = now + timedelta(seconds=(random.randint(0, 100)))
    total = total+1
    
    print(now,total)
    if(total % 3000 == 0):
        time.sleep(20)
