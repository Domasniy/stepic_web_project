def application(environ, start_response):
    test = environ['QUERY_STRING'].split('&')
    test = "\n".join(test)
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return [test]
