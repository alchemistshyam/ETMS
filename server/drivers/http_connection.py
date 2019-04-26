import requests
class HTTP_Connection:

    def get_http_connection(url,token):
        token_string = {"token":token}
        response = requests.request("GET", url,params=token_string)
        return(response.text)