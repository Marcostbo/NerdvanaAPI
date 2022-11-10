from rest_framework.exceptions import ValidationError


def validate_code_input(code_object, user):
    if not code_object:
        raise ValidationError('Code does not exists')
    elif code_object.user != user:
        raise ValidationError('Invalid code for this user')
    elif not code_object.is_valid:
        raise ValidationError('Code not valid anymore')
