import os
# setting the environment variables
os.environ['CLARIFAI_APP_ID']= 'k_4REO2PhmcZeTjorCpb7WKKE6X2mR_ns4jzSmPN'
os.environ['CLARIFAI_APP_SECRET'] ='YO4Yr7jJrRMHlcHPcwbeM2wm9exoyg_N4p9x4tMh'
from clarifai.client import ClarifaiApi
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
#asking for input argumnent
imageurl= raw_input('enter the url of image ')
output = clarifai_api.tag_image_urls(imageurl)
tags = output['results'][0]['result']['tag']['classes']
tags_prob = output['results'][0]['result']['tag']['probs']

for index in range(len(tags)):
	print str(tags[index]), " ", tags_prob[index] 

