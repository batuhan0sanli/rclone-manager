from rclone_manager.base.exceptions._base import RCloneManagerException


class RCloneValueError(RCloneManagerException):
    """Exception for when the value is not set"""
    pass


class RCloneProcessError(RCloneManagerException):
    """Exception for when the process fails"""
    pass


class RCloneProcessTimeout(RCloneManagerException):
    """Exception for when the process times out"""
    pass
