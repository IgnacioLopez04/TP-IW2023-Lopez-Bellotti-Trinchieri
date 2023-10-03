from django.shortcuts import render

contexts = [
    {
        'nombreViaje': 'Mendoza',
        'dias': 6,
        'descripcion': 'Mucho vino, nieve y aventuras por las montañas',
        'url':'https://img.itinari.com/pages/images/original/324b16ee-ab94-4faa-a773-b3cdf53a6d7e-8551e86d-12c9-4150-b0a3-d54d23292d5f-istock-693410412.jpg?ch=DPR&dpr=2.625&w=1200&h=800&s=6a08a72138ffcb00d99594a4b8ad3778',
        'alt': 'foto montaña',
        'calificacion': 5
    },
    {
        'nombreViaje': 'Salta',
        'dias': 4,
        'descripcion': 'Mucho locro y peñas',
        'url': 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/6ALKAZKZDZBDLCPDYNRYMZWTZY.jpg',
        'alt': 'foto salta',
        'calificacion': 3
    },
    {
        'nombreViaje': 'Córdoba',
        'dias': 3,
        'descripcion': 'Mucho fernet, sierras y rios de aguas cristalinas',
        'url':'https://images.musement.com/cover/0084/72/san-martin-square-cordoba-cathedral-argentina-jpg_header-8371496.jpeg',
        'alt': 'foto cordoba',
        'calificacion': 5
    },
    {
        'nombreViaje': 'La Pampa',
        'dias': 2,
        'descripcion': 'No se que hay en la Pampa',
        'url':'https://hablemosdeargentina.com/wp-content/uploads/2018/03/patagonia-la-pampa.jpg',
        'alt': 'foto la pampa',
        'calificacion': 1
    },
    {
        'nombreViaje': 'Rio Negro',
        'dias': 8,
        'descripcion': 'Mucho nieve',
        'url':'https://volemos.nyc3.cdn.digitaloceanspaces.com/blog/wp-content/uploads/2020/07/09121424/Imperdibles-de-Rio-Negro.jpg',
        'alt': 'foto rio negro',
        'calificacion': 4
    },
    ]

def inicio(request):
    contexto = {
        'contexts': contexts
    }
    return render(request, 'inicio.html', contexto)

def rebuild_index(request):
    from django.core.management import call_command
    from django.http import JsonResponse
    try:
        call_command("rebuild_index", noinput=False)
        result = "Index rebuilt"
    except Exception as err:
        result = f"Error: {err}"

    return JsonResponse({"result": result})