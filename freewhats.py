import requests, json, random, string, time
from bs4 import BeautifulSoup
logo = """
 ____    ____  ____   ___     ___   ___ ___         __  ____    ____    __  __  _    ___  ___       
|    \  /    ||    \ |   \   /   \ |   |   |       /  ]|    \  /    |  /  ]|  |/ ]  /  _]|   \      
|  D  )|  o  ||  _  ||    \ |     || _   _ |      /  / |  D  )|  o  | /  / |  ' /  /  [_ |    \     
|    / |     ||  |  ||  D  ||  O  ||  \_/  |     /  /  |    / |     |/  /  |    \ |    _]|  D  |    
|    \ |  _  ||  |  ||     ||     ||   |   |    /   \_ |    \ |  _  /   \_ |     \|   [_ |     |    
|  .  \|  |  ||  |  ||     ||     ||   |   |    \     ||  .  \|  |  \     ||  .  ||     ||     |    
|__|\_||__|__||__|__||_____| \___/ |___|___|     \____||__|\_||__|__|\____||__|\_||_____||_____|    
                                                                                                    
 ____   __ __      _____  ____   ____  __ __  ______    ___  ____   ___   _____                     
|    \ |  |  |    |     ||    | /    ||  |  ||      |  /  _]|    \ /   \ / ___/                     
|  o  )|  |  |    |   __| |  | |   __||  |  ||      | /  [_ |  D  )     (   \_                      
|     ||  ~  |    |  |_   |  | |  |  ||  _  ||_|  |_||    _]|    /|  O  |\__  |                     
|  O  ||___, |    |   _]  |  | |  |_ ||  |  |  |  |  |   [_ |    \|     |/  \ |                     
|     ||     |    |  |    |  | |     ||  |  |  |  |  |     ||  .  \     |\    |                     
|_____||____/     |__|   |____||___,_||__|__|  |__|  |_____||__|\_|\___/  \___|  fighteros121212@gmail.com                             
                                                                                    Ahmed M. Abd El-Ghany                        """
print(logo)
pssw = input(' [-] Enter Password: ').strip()
if pass=='fighteros00'
  with requests.Session() as (req):
      number =input('[-] Enter vodafone Number: ')
      pwd = input('[-] Enter ana vodafone password please: ').strip()
  def generationLink(stringLingth):
      latters = string.ascii_lowercase
      return ''.join((random.choice(latters) for i in range(stringLingth)))
  urlLoginPage = 'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={}&kc_locale=en'.format(generationLink(10))
  responsePageLogin = req.get(urlLoginPage)
  soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
  getUrlAction = soup.find('form').get('action')
  headerRequest = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'Accept-Encoding':'gzip, deflate, br',
   'Accept-Language':'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
   'Connection':'keep-alive',
   'Content-Type':'application/x-www-form-urlencoded',
   'Host':'web.vodafone.com.eg',
   'Origin':'https://web.vodafone.com.eg',
   'Referer':urlLoginPage,
   'Sec-Fetch-Dest':'document',
   'Sec-Fetch-Mode':'navigate',
   'Sec-Fetch-Site':'same-origin',
   'Sec-Fetch-User':'?1',
   'Upgrade-Insecure-Requests':'1',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
  formData = {'username':number,
   'password':pwd}
  sendUserData = req.post(getUrlAction, headers=headerRequest, data=formData)
  checkRegistry = sendUserData.url
  _checkRegistry = checkRegistry.find('KClogin')
  if _checkRegistry != -1:
      code = checkRegistry
      _code = code[code.index('code=') + 5:]
      headerAccessToken = {'Accept':'*/*',
       'Accept-Encoding':'gzip, deflate, br',
       'Accept-Language':'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
       'Connection':'keep-alive',
       'Content-type':'application/x-www-form-urlencoded',
       'Host':'web.vodafone.com.eg',
       'Origin':'https://web.vodafone.com.eg',
       'Referer':'https://web.vodafone.com.eg/ar/KClogin',
       'Sec-Fetch-Dest':'empty',
       'Sec-Fetch-Mode':'cors',
       'Sec-Fetch-Site':'same-origin',
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
      formDataAccessToken = {'code':_code,
       'grant_type':'authorization_code',
       'client_id':'website',
       'redirect_uri':'https://web.vodafone.com.eg/ar/KClogin'}
      sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token', headers=headerAccessToken, data=formDataAccessToken)
      access_token = sendDataAccessToken.json()['access_token']
      oneTime = "inf"#input(' [-] To renew at once 200 MB, press [one]. or to renew every minute, press [inf]: ')
      if oneTime == 'one':
          print(' ============================== ')
          header = {'Accept':'application/json, text/plain, */*',
           'api-host':'RatePlanHost',
           'Authorization':f"Bearer {access_token}",
           'Content-Type':'application/json',
           'msisdn':number,
           'Referer':'https://web.vodafone.com.eg/ar/flexmanagement',
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
          payload = {'msisdn':f"{number}",
           'packageId':'723',  'clientId':'WEBSITE',  'serviceId':'Prepaid_Mig',  'action':'i',  'migrationFees':0,  'ratePlanRank':'23',  'rateplancolor':'X',  'customerId':'194367544'}
          send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
          payload = {'msisdn':f"{number}",
           'packageId':'470',  'clientId':'WEBSITE',  'serviceId':'Flexat_Main',  'action':'i',  'customerId':'194367544'}
          send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
          payload = {'msisdn':f"{number}",
           'packageId':'470',  'clientId':'WEBSITE',  'serviceId':'Flexat_Main',  'action':'i',  'customerId':'194367544'}
          send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
          eDescription = send.json()['eDescription']
          if str(eDescription).find('Success and the transaction is already processed') != -1:
              print(' [-] 200 MB added successfully.')
          else:
              print(' [-] Error );')
      else:
          if oneTime == 'inf':
              print(' ============================== ')
              while True:
                  header = {'Accept':'application/json, text/plain, */*',  'api-host':'RatePlanHost',
                   'Authorization':f"Bearer {access_token}",
                   'Content-Type':'application/json',
                   'msisdn':number,
                   'Referer':'https://web.vodafone.com.eg/ar/flexmanagement',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
                  payload = {'msisdn':f"{number}",
                   'packageId':'723',  'clientId':'WEBSITE',  'serviceId':'Prepaid_Mig',  'action':'i',  'migrationFees':0,  'ratePlanRank':'23',  'rateplancolor':'X',  'customerId':'194367544'}
                  send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
                  payload = {'msisdn':f"{number}",
                   'packageId':'470',  'clientId':'WEBSITE',  'serviceId':'Flexat_Main',  'action':'i',  'customerId':'194367544'}
                  send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
                  payload = {'msisdn':f"{number}",
                   'packageId':'470',  'clientId':'WEBSITE',  'serviceId':'Flexat_Main',  'action':'i',  'customerId':'194367544'}
                  send = req.post('https://web.vodafone.com.eg/services/changePrepaidServiceClass', headers=header, data=(json.dumps(payload)))
                  eDescription = send.json()['eDescription']
                  if str(eDescription).find('Success and the transaction is already processed') != -1:
                      print(' [-] 200 MB added successfully.')
                      time.sleep(6)
                  else:
                      print(' [-] Error );')
                  time.sleep(65)
          else:
              pass

  else:
      print(' [False] Error username or password.')
else:
  print('==========================[incorrect password]===============================')
  print('you need to contact Ahmed M. Abd El-Ghany to get the password')
x = input(' exit...')
