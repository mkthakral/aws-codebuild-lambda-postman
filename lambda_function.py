import yaml
import json

# import requests


def lambda_handler(event, context):
  
    #Read request body
    data = json.dumps(event)
    data = json.loads(data)
    
    #Convert input YAML to JSON
    yaml_object = yaml.safe_load(data['body']) 
    json_out = json.dumps(yaml_object)
    
    
    #Retun output JSON
    return {
     'statusCode': 200,
     'body': json_out
    }
