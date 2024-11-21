import requests
import json
import jsonschema

base_url = 'https://automationexercise.com/api/'

auth_token = ''

JSON_SCHEMA = {
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "responseCode": {
      "type": "number"
    },
    "products": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "price": {
            "type": "string"
          },
          "brand": {
            "type": "string"
          },
          "category": {
            "type": "object",
            "properties": {
              "usertype": {
                "type": "object",
                "properties": {
                  "usertype": {
                    "type": "string"
                  }
                },
                "required": [
                  "usertype"
                ]
              },
              "category": {
                "type": "string"
              }
            },
            "required": [
              "usertype",
              "category"
            ]
          }
        },
        "required": [
          "id",
          "name",
          "price",
          "brand",
          "category"
        ]
      }
    }
  },
  "required": [
    "responseCode",
    "products"
  ]
}

#GET request
def get_request():
    URL =  base_url + '/productsList'
    headers = {'Authorization' : auth_token}
    response = requests.get(URL, headers = headers)
    
    assert response.status_code == 200
    status_code = response.status_code

    json_data = response.json()
    json_pretty_str = json.dumps(json_data, indent=2 )
    print('json response: \n', json_pretty_str)
    
    #validate json schema...
    try:
        jsonschema.validate(instance=json_data,schema=JSON_SCHEMA)
        print("JSON is valid")
    except jsonschema.exceptions.ValidationError as e:
        print("JSON is invalid:", e)
    
    return status_code

#POST request

#PUT request

#DELETE request

def test_GET_ProductsList():
    assert get_request() == 200

def main():
    get_request()


if __name__ =="__main__":
     main()