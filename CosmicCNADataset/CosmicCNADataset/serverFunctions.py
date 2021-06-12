import sys
from subprocess import run, PIPE
from django.shortcuts import render


# buraya fonksiyonlarımızı yazıyoruz

# home.html'i yüklüyor
def showWebPage(request):
    return render(request, 'index.html')


def returnPredictValue(request):
    geneName = request.POST.get('geneName')
    PrimarySite = request.POST.get('PrimarySite')
    TotalCN = request.POST.get('TotalCN')
    mutationType = request.POST.get('mutationType')
    Chromosome = request.POST.get('Chromosome')
    out = run([sys.executable, "C:\\Users\\Bilal Günden\\PycharmProjects\\test.py", geneName,PrimarySite,TotalCN,mutationType,Chromosome], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'index.html', {'data1': out.stdout})
