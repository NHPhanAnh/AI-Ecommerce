from django.http import HttpResponse

def gateway_home(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>API Gateway - E-Commerce</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="bg-light">
    <div class="container text-center mt-5">
        <h1 class="mb-4 text-primary">E-Commerce API Gateway</h1>
        <p class="lead">Entry Point Hệ thống Microservices</p>
        <div class="d-grid gap-3 col-6 mx-auto mt-4">
            <a href="http://localhost:8000/" class="btn btn-primary btn-lg shadow">🛍️ Truy cập Customer Portal (Port 8000)</a>
            <a href="http://localhost:8001/" class="btn btn-dark btn-lg shadow">⚙️ Truy cập Staff Admin (Port 8001)</a>
        </div>
        <div class="mt-5 text-start card p-4 shadow-sm border-0">
            <h5 class="text-secondary">Các API Endpoints Nội Bộ:</h5>
            <ul class="list-group list-group-flush mt-2">
                <li class="list-group-item"><strong>Product API (PostgreSQL):</strong> <a href="http://localhost:8002/products/">http://localhost:8002/products/</a></li>
                <li class="list-group-item"><strong>AI KnowledgeBase/Chat API:</strong> <a href="http://localhost:8005/docs">http://localhost:8005/docs</a></li>
            </ul>
        </div>
    </div>
    </body>
    </html>
    """
    return HttpResponse(html)
