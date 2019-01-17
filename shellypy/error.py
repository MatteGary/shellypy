
class ShellyError(Exception):
   """Base class for other exceptions"""
   pass

class DeviceNotReady(ShellyError):
    """Raised when the device is not ready"""
    pass
    
class NetworkError(ShellyError):
    """Raised when a network call fails"""
    pass

class RelayStatusError(ShellyError):
    """Raised when an error occurred while checking relay status"""
    pass
    
class RelayIsNotValid(ShellyError):
    """Raised when a relay returns is_valid as False"""
    pass
    
class SetRelayError(ShellyError):
    """Raised when something went wrong while setting Relays status"""
    pass