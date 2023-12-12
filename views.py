from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        numero1 = float(request.POST['numero1'])
        numero2 = float(request.POST['numero2'])
        operacao = request.POST['operacao']

        if operacao == 'somar':
            result = numero1 + numero2
        elif operacao == 'subtrair':
            result = numero1 - numero2
        elif operacao == 'multiplicar':
            result = numero1 * numero2
        elif operacao == 'dividir':
            result = numero1 / numero2

        return render(request, 'calculator/results.html', {'result': result})

    return render(request, 'calculator/home.html')
