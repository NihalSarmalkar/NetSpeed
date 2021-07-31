import speedtest

test_speed = speedtest.Speedtest()

print("Loading the best server ...")
test_speed.get_servers()
print(test_speed)
print("choosing best server ...")
bestServer=test_speed.get_best_server()
print(bestServer)
print(bestServer['host'],bestServer['country'])

print("Performing download test...")
download_result=test_speed.download()
print("Performing upload test...")
upload_result=test_speed.upload()
ping_result=test_speed.results.ping

print("Download speed is %s Mbit/s",download_result/1024/1024)
print("Download speed is %s Mbit/s",upload_result/1024/1024)
print("Ping is ",ping_result)




