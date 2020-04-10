import requests,urllib,os,json
from twilio.twiml.messaging_response import *
from flask import *
bot = Flask(__name__)
@bot.route('/', methods=['POST','GET'])
def simi():
	balas = MessagingResponse()
	chat = request.form.get('Body')
	res=requests.get('https://secureapp.simsimi.com/v1/simsimi/talkset?uid=287126054&av=6.8.9.4&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=pNfLbeQT%2B0cnFY8YHQb7CNHowpg%3D&message_sentence='+urllib.parse.quote(chat)+'&normalProb=8&isFilter=1&talkCnt=2&talkCntTotal=2&reqFilter=1&session=XZzaduTVCSqa6vMtuyFhGv9eCXiyWwKJVETZjpQjc2oLPGBN2XtpzcKRFhLukHd6EAYVWMiSGuPzQV5Vwcdmwz14&triggerKeywords=%5B%5D').text
	balas.message(json.loads(res)['simsimi_talk_set']['answers'][0]['sentence'])
	return str(balas)
if __name__=='__main__':
	bot.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)),debug=True)
    
