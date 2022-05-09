
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from test_dashboard import server as test
import landing_page


app = DispatcherMiddleware(landing_page, {
    '/prawler/test': test,
})