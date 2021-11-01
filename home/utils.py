from .imports import *
import json


def permission_check(user_type):
    def _method_wrapper(view_method):

        def _arguments_wrapper(request, *args, **kwargs):
            """
            Wrapper with arguments to invoke the method
            """
            # user = CustomUser.objects.get(username=request.api_user)
            # permission = user.is_superuser
            try:
                get_token = request.META['HTTP_AUTHORIZATION']
                token = get_token[6:].strip()
                print('token', token)

                resp = decode_auth_token(token)
                print('resp', resp)

                if "code" in resp.keys() and resp["code"] == 401:
                    data = {
                        "code": 401,
                        "message": "Token expired. Please log in again."
                    }
                    dump = json.dumps(data)

                    return HttpResponse(dump, content_type="application/json", status=401)

                elif "code" in resp.keys() and resp["code"] == 403:
                    data = {
                        "code": 401,
                        "message": "Invalid token. Please log in again."
                    }
                    dump = json.dumps(data)

                    return HttpResponse(dump, content_type="application/json", status=401)

                else:
                    request.api_user = resp["username"]
                    print(request.api_user)
                    # permission check if any
                    if user_type=='Admin':
                        if not User.objects.get(username=request.api_user).is_superadmin:
                            data = {
                                "code": 401,
                                "message": "You need admin access for this API."
                            }
                            dump = json.dumps(data)

                            return HttpResponse(dump, content_type="application/json", status=401)
                    return view_method(request, *args, **kwargs)


            except ValidationError:
                data = {
                    'status': 'Failed',
                    'message': "Permission Denied",
                    "code": 401,
                    "error": "Invalid Authorization details"
                }

                dump = json.dumps(data)
                return HttpResponse(dump, content_type="application/json", status=401)

            except KeyError:
                print('key error block')
                data = {
                    'status': 'Failed',
                    'message': "Unauthorized",
                    "code": 401,
                    "error": "Authorization Credentials were not provided"
                }

                dump = json.dumps(data)
                return HttpResponse(dump, content_type="application/json", status=401)

        return _arguments_wrapper

    return _method_wrapper
