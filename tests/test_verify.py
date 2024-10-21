import jwt, datetime as date
from Backend import token_service as ts

def generic_test_for_validation_of_token_by_token_service(token: str, service: ts.TokenService) -> bool:
    return service.verify(token)

def generic_test_for_right_encoding_matching_with_verification(username: str, service: ts.TokenService) -> bool:
    return service.verify(service.encode(username))


def test_of_validation_and_encoding_of_data_by_token_service():
    service = ts.TokenServiceImpl()
    username = "Andrew"
    token = service.encode(username)
    if not service.verify(token):
        print("test_of_validation failed. token is: " + token)
        return False
    
    return True

# test execution:
print("test_of_validation_and_encoding_of_data_by_token_service: " + str(test_of_validation_and_encoding_of_data_by_token_service()))
