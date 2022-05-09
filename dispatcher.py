
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from test_dashboard import server as test
from landing_page import server as landing


app = DispatcherMiddleware(landing, {
    '/prawler/test': test,
})