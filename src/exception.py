import sys

def error_messgae_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename

    error_message="Error Occured in python script [{0}] error message [{2}]".format(file_name,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message=error_messgae_detail(error_message,error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message



