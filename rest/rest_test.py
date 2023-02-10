import requests, json

# Template class for REST API's
class RestAPI:

    #####
    #   __init__
    #       input: _host (str), _header (str)
    #####
    def __init__(self, _host, _header="json"):
        self.base_api_url = str(_host)
        self.headers = {"Content-Type":"application/" + str(_header)} 

    #####
    #   post_rest
    #       input: request (str), data(dict)
    #
    #       output: bool - success
    #####
    def post_rest(self, request, data):
        print("Testing API: ")
        req = request
        body = data
        
        # sending post request with some data, save response
        response = requests.post(url=self.base_api_url + req, data=json.dumps(body), headers=self.headers)

        # Response
        try:
            print(response.json())
            return True
        except:
            print("Not printable response")
            try:
                print(response)
            except:
                print("Err")
            return False

    #####
    #   get_rest
    #       input: data (list), args (dict)
    #       
    #       output: bool - success
    #####
    def get_rest(self, request, data=None, args=None):
        print("Testing API: ")
        req = request

        # this should cover /api/data1/data2 etc
        if(data):
            if(type(data) != list):
                print("Data type needs to be a list")
                return -1
            for i in data:
                req = req + "/" + str(i)

        # Work through the arguments, would normally be "/api?arg1=val1&arg2=val2"
        if(args):
            if(type(args) != dict):
                print("Args type needs to be a dict")
                return -1
            first = True
            for k in args:
                if(first):
                    req = req + "?"
                    first = False
                else:
                    req = req + "&"
                req = req + str(k) + "=" + str(args[k])
        
        # sending get request and saving the response as response object
        response = requests.get(url=self.base_api_url + req, headers=self.headers)

        try:
            print(response.json())
            return True
        except:
            print("Not printable response")
            try:
                print(response)
            except:
                print("Err")
            return False

# Example using regres.in API:
if __name__ == '__main__':

    ## Set up API:
    ta = RestAPI("https://reqres.in/api/", header="json")

    # Create payload
    payload ={
        "email": "fake_email@reqres.in",
        "password": "password"
    }
    # Do a post request
    ta.post_rest("register", payload)

    # Do a get request eg
    ta.get_rest("users", args={"delay": 3})