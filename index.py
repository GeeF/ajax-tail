from pprint import pformat

def application(environ, start_response):
    output = ['']

    with open('/path/to/www/template.html', 'r') as f:
        for line in f:
            output.append(line)

    output.append('</body>')
    # send results
    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/html'),
                              ('Content-Length', str(output_len))])
    return output
