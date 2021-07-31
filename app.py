from flask import Flask, render_template,request
from flask.wrappers import Request
import speedtest


app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    
    
    
    if request.method=='POST':
        test_speed = speedtest.Speedtest()
        
        test_speed.get_servers()
        
        
#         bestServer=test_speed.get_best_server()
        

#         hostaddress=" Location at "+bestServer['country']+","+bestServer['name']

        
#         download_result=test_speed.download()
        
#         upload_result=test_speed.upload()
#         ping_result=test_speed.results.ping

        str1="Download - "+str(round(test_speed.download()/1024/1024,2))+" Mbps"
        str2="Upload - "+str(round(test_speed.upload()/1024/1024,2))+" Mbps"

        str3="Ping is "+str(ping_result)
        return render_template('index.html',hostaddress=hostaddress,str1=str1,str2=str2,str3=str3)
    else:
        str4="Fail to Show the results"
        return render_template('index.html',str4=str4)
        


    


if __name__ == "__main__":
    app.run(debug=True)
