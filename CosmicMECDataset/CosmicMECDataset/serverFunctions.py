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
    primaryHistology = request.POST.get('primaryHistology')
    histologySubtype = request.POST.get('histologySubtype')
    mutationDescription = request.POST.get('mutationDescription')
    FATHMMPrediction = request.POST.get('FATHMMPrediction')
    tumorOrigin = request.POST.get('tumorOrigin')
    out = run([sys.executable, "C:\\Users\\Bilal Günden\\PycharmProjects\\test.py", geneName,PrimarySite,primaryHistology,histologySubtype,mutationDescription,FATHMMPrediction,tumorOrigin], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'index.html', {'data1': out.stdout})
