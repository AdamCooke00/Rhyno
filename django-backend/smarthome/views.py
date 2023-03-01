from .models import SmartHome
from .serializers import SmartHomeSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .camera import *
from .temperature import *
from .colors import colorDict
import os
import threading
from django.http import JsonResponse


# Need a global to keep track of the thread id to be able to kill it...
rtsp_hls_threadId = 0

class SmartHomeListCreate(generics.ListCreateAPIView):
    queryset = SmartHome.objects.all()
    serializer_class = SmartHomeSerializer

@api_view(['GET', 'POST'])
def smarthome_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print("GET")
        smarthome = SmartHome.objects.all()
        serializer = SmartHomeSerializer(smarthome, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("POST")
        serializer = SmartHomeSerializer(data=request.data)
        # print(request.data['plug'])
        
        key = list(request.data.keys())[0]
        print(key)

        if(key == "plug"):
            state = None
            if(request.data[key] == "get-data"):
                print("GOTTA CALL DATA CMD")
                
                
                return JsonResponse({"state":"OFF"})

            elif(request.data[key] == "OFF"):
                state = "OFF"
            elif(request.data[key] == "ON"):
                state = "ON"
            else:
                print("Invalid Command")
            
            cmdStr = "mosquitto_pub -t \'zigbee2mqtt/plug1/set\' -m \'{ \"state\": \"%s\"}\'" % state
            os.system(cmdStr)
            # print(cmdStr)
        # Returns the temperature and humdity data to the webpage
        elif(key == "temp"):
            print("GOT IT!")
            return JsonResponse(read_data_from_excel())

        elif(key == "light1"):
            state = "ON"
            key = list(request.data.keys())[0]
            brightness = request.data['brightness']
            print(brightness)

            if(request.data[key] == "get-data"):
                print("GOTTA CALL DATA CMD")

                return JsonResponse({"state":"ON","brightness":50})

            elif(request.data[key] == "OFF"):
                state = "OFF"
            elif(request.data[key] == "ON"):
                state = "ON"
            #
            # "mosquitto_pub -t \'zigbee2mqtt/light2/set\' -m \'{ \"state\": \"ON\",\"brightness\":254 }\'"
            cmdStr = "mosquitto_pub -t \'zigbee2mqtt/light1/set\' -m \'{ \"state\": \"%s\",\"brightness\":%s}\'" % (state,brightness)
            os.system(cmdStr)
            print(cmdStr)
        elif(key == "light2"):
            state = "ON"
            brightness = request.data['brightness']

            if(request.data[key] == "get-data"):
                print("GOTTA CALL DATA CMD")

                return JsonResponse({"state":"ON","brightness":50})
                
            elif(request.data[key] == "OFF"):
                state = "OFF"
            elif(request.data[key] == "ON"):
                state = "ON"
            
            cmdStr = "mosquitto_pub -t \'zigbee2mqtt/light2/set\' -m \'{ \"state\": \"%s\",\"brightness\":%s}\'" % (state,brightness)
            os.system(cmdStr)
            print(cmdStr)
        elif(key == "matter"):
            colorKey = list(request.data.keys())[1]
            stateKey = list(request.data.keys())[2]
            brightnessKey = list(request.data.keys())[3]

            rgb_color = request.data[colorKey]
            rgb_state = request.data[stateKey]
            rgb_brightness = request.data[brightnessKey]

            if(int(rgb_brightness) < 2):
                rgb_brightness = 2

            chip_tool_dir = "/home/jared/Desktop/esp-matter/esp-matter/connectedhomeip/connectedhomeip/out/host"
            os.chdir(chip_tool_dir)

            # First calling the state command
            state_cmd = "./chip-tool onoff {} 0x7283 0x1".format(rgb_state)
            os.system(state_cmd)
            print(rgb_color)

            rgb_color = colorDict[rgb_color['name']]
            print(rgb_color)
            color_cmd = "./chip-tool colorcontrol move-to-hue-and-saturation {} 100 0 0 0 0x7283 0x1".format(rgb_color)
            os.system(color_cmd)

            brightness_cmd =  "./chip-tool levelcontrol move-to-level {} 0 0 0 0x7283 0x1".format(rgb_brightness)
            os.system(brightness_cmd)
        


        elif(key == "camera"):

            cmd = list(request.data.keys())[1]
            if(cmd == "move"):
                if(request.data[cmd] == "start"):
                    cmd = "start"
                elif(request.data[cmd] == "stop"):
                    cmd = "stop"
                if(request.data[key] == "left"):
                    ctrlLeft(cmd)
                elif(request.data[key] == "right"):
                    ctrlRight(cmd)
                elif(request.data[key] == "up"):
                    ctrlUp(cmd)
                elif(request.data[key] == "down"):
                    ctrlDown(cmd)
            elif(cmd == "rtspUrl"):

                rtspCmd = list(request.data.keys())[2]
                rtspUrl = request.data[cmd]
                videoDirectory = "/home/rhyno/Desktop/svelte-frontend/public/video/"

                

                global rtsp_hls_threadId
                
                print(request.data[rtspCmd])

                if(request.data[rtspCmd] == "start"):
                    # print("Starting Video Stream?")
                    t = threading.Thread(target=startVideoStream, args=(videoDirectory,rtspUrl))
                    t.start()

                    
                elif(request.data[rtspCmd] == "stop"):
                    # print("Ending Video Stream and deleting files?")
                    
                    osCmd = "killall -9 ffmpeg"
                    os.system(osCmd)
                    
                    for filename in os.listdir(videoDirectory):
                        file_path = os.path.join(videoDirectory, filename)
                        try:
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                                print(f"Successfully deleted {file_path}")
                        except Exception as e:
                            print(f"Error deleting {file_path}: {e}")

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



def startVideoStream(videoDirectory, rtspUrl):
    # -hls_list_size 600 -hls_flags
    osCmd = "ffmpeg -i {} -c:v libx264 -preset veryfast -tune zerolatency -g 10 -c:a aac -f hls -hls_time 1 -hls_list_size 600 \
        -hls_flags delete_segments+append_list+omit_endlist -hls_segment_filename {}stream_{}.ts  {}stream.m3u8".format(rtspUrl,videoDirectory,r"%03d",videoDirectory)

    os.system(osCmd)

    