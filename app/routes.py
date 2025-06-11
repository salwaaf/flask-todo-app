from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('todo_requests_total', 'Total requests to the index route')

start_http_server(8000)  # metrics available at localhost:8000

@main.route('/')
def index():
    REQUEST_COUNT.inc()
    return render_template('index.html')