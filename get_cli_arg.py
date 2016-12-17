import argparse
import sys

# type =  type to which the command-line argument should be converted
# help =  description of what the argument does.
# required = whether option is required
# nargs = for list of inputs
# default = value produced if the argument is absent from the command line.
# choices = list of the allowable values for the argument.


def get_cli_args(args=None):
    parser = argparse.ArgumentParser(description='<Desicription of Script Here>')
    parser.add_argument('-s', '--server',
                        type=str,
                        help='server ip',
                        required='True')
    parser.add_argument('-p', '--port',
                        type=str,
                        help='port of the web server',
                        required=True,
                        nargs='+')
    parser.add_argument('-u', '--user',
                        type=str,
                        help='user name',
                        choices={'admin', 'user'},
                        default='root')

    results = parser.parse_args(args)
    results.port = results.port[0].split(",")
    return (results.server,
            results.port,
            results.user)

if __name__ == '__main__':
    h, p, u = get_cli_args(sys.argv[1:])
    print 'h =', h
    print 'p =', p
    print 'u =', u
