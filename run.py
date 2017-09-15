'''run'''
import eventlet, os, time, sys, getopt
from os import environ, system
from flask import current_app, g, session
from app import create_app
app = create_app('app')

#-------------------------------------------------------------------------------
@app.before_request
def do_setup():
    session.permanent = True
    g.db = current_app.db_client['simbot']
    g.group = 'sean'

#-------------------------------------------------------------------------------
@app.after_request
def do_teardown(response):
    return response

#-------------------------------------------------------------------------------
def main(argv):

    from detect import startup_msg
    from detect import set_environ
    import workers

    try:
        opts, args = getopt.getopt(argv,"cds", ['celerybeat', 'debug'])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in('-c', '--celerybeat'):
            environ['BRV_BEAT'] = 'True'
            beat = True
        elif opt in ('-d', '--debug'):
            app.config['DEBUG'] = True
            app.config['USE_DEBUGGER'] = True

    app.logger.debug('Starting server...')

    set_environ(app)
    workers.kill()
    time.sleep(1)
    workers.start(beat=bool(environ.get('BRV_BEAT')))
    time.sleep(1)
    startup_msg(app, show_celery=False)

    app.logger.info("Server ready @%s", app.config['LOCAL_URL'])

    app.run()

    """
    sio_server.run(app,
        port=app.config['LOCAL_PORT'],
        log_output=False,
        use_reloader=False)
    """

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
