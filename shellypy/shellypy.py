
import requests
import const
import error

class Shelly:
    """Represents a Shelly device base class"""
    
    def __init__(self, address):
        """Initialize Shelly base class"""
        
        if ("http://" in address):
            self.device_address = address
        else:
            self.device_address = "http://" + address
            
            
    def check_status(self):
        """Check the status of the device"""
        from requests.exceptions import RequestException
        try:
            r  = requests.get(self.device_address + "/status")
        except RequestException as err:
            raise error.NetworkError
        
        if (r.status_code == 200):
            return const.STATUS_OK
        else:
            return const.STATUS_DEVICENOTREADY
            

class ShellyRelay(Shelly):
    """Represents a single Shelly Relay device"""
    
    def __init__(self, address, device):
        """Initialize Shelly Device class"""
        
        Shelly.__init__(self, address)
            
        self.device_number = str(device)
        self.mode = const.MODE_RELAY
        
        self.check_status()
    
    def get_status(self):
        """Get the latest data from Shelly Relay"""
        from requests.exceptions import RequestException
        try:
            r = requests.get(self.device_address + "/relay/" + self.device_number).json()
        except RequestException as err:
            raise error.RelayStatusError

        if (r["is_valid"] == True):
            return r["ison"]
        else:
            raise error.RelayIsNotValid
            
    def turn_on(self):
        """Turn on a Shelly Relay"""
        self.set_relay_status(const.ON)
        
    def turn_off(self):
        """Turn off a Shelly Relay"""
        self.set_relay_status(const.OFF)
            
    def set_status(self, is_on):
        """Set the status of a Shelly Relay"""        
        from requests.exceptions import RequestException
        try:
            r = requests.post(self.device_address + "/relay/" + self.device_number + "?turn=" + is_on)
        except RequestException as err:
            raise error.SetRelayError           
