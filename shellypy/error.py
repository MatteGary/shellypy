
class ShellyError(Exception):
   """Base class for other exceptions"""
   pass

class DeviceNotReady(ShellyError):
    """Raised when the device is not ready"""
    pass
    
class NetworkError(ShellyError):
    """Raised when a network call fails"""
    pass