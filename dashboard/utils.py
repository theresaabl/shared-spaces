def resident_request_type(purpose):
    """
    Helper function for edit_resident_request and delete_resident_request views
    Returns whether the resident request is of type request or message
    """
    return "Maintenance request" if purpose == 0 else "Message"


def convert_date(booking_date):
    """
    Convert date to 'YYYY-MM-DD' for proper display in date picker
    """
    return booking_date.strftime("%Y-%m-%d")
