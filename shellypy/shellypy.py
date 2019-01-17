
import requests
import const
import error

class Shelly:
    """Represents a single Shelly Relay device"""
    
    def __init__(self, address, device):
        """Initialize Shelly Device class"""
        
        if ("http://" in address):
            self.device_address = address
        else:
            self.device_address = "http://" + address
            
        self.device_number = str(device)
        self.mode = const.MODE_RELAY
        
        self.check_status()
        
    def check_status(self):
        """Check the status of the device"""
        from requests.exceptions import RequestException
        try:
            r  = requests.get(self.device_address + "/status")
        except RequestException as err:
            raise error.NetworkError
        
        if (r.status_code == 200):
            return
        else:
            raise DeviceNotReady
        
    
    def get_relay_status(self):
        """Get the latest data from Shelly Device"""
        r = requests.get(self.device_address + "/relay/" + self.device_number)
        return r.json()
