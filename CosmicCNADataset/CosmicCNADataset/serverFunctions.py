import sys
from subprocess import run, PIPE
from django.shortcuts import render


# buraya fonksiyonlarımızı yazıyoruz

# home.html'i yüklüyor
def showWebPage(request):
    return render(request, 'index.html')


def returnPredictValue(request):
    geneName = request.POST.get('geneName').lower()
    PrimarySite = request.POST.get('PrimarySite').lower()
    TotalCN = request.POST.get('TotalCN').lower()
    mutationType = request.POST.get('mutationType').lower()
    Chromosome = request.POST.get('Chromosome').lower()
    out = run([sys.executable, "C://Users//Bilal Günden//Desktop//CNA//cna_test.py",geneName,PrimarySite,TotalCN,mutationType,Chromosome], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'index.html', {'data1': out.stdout.decode('UTF-8')})
