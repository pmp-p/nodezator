import sys
from nodezator import __main__

NATIVE_FILE_EXTENSION = '.ndz'

print( __main__.main )

if __name__ == "__main__":

    ### parse arguments received, looking for a filepath
    ### (or using None instead, a filepath wasn't provided)

    ## import argument parser
    from argparse import ArgumentParser

    ## instantiate and configure it

    parser = ArgumentParser(
               description = " - Python Node Editor"
             )

    parser.add_argument(

             'filepath',

             type    = str,
             nargs   = '?',
             default = None,

             help    = (
               "path of "
               + NATIVE_FILE_EXTENSION
               + " file to be loaded."
             )
           )

    ## parse arguments
    args = parser.parse_args()


    ### finally call the main function, passing along
    ### the filepath argument received (which might be the
    ### default, None)
    __main__.main(args.filepath)
