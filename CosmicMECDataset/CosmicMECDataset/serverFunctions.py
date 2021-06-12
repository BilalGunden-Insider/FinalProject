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
    primaryHistology = request.POST.get('primaryHistology').lower()
    histologySubtype = request.POST.get('histologySubtype').lower()
    mutationDescription = request.POST.get('mutationDescription').lower()
    FATHMMPrediction = request.POST.get('FATHMMPrediction').lower()
    tumorOrigin = request.POST.get('tumorOrigin').lower()
    out = run([sys.executable, "C://Users//Bilal Günden//Desktop//MUT_EX_CENSUS//mutexcen_test.py", geneName,PrimarySite,primaryHistology,histologySubtype,mutationDescription,FATHMMPrediction,tumorOrigin], shell=False, stdout=PIPE)
    print(out)

    return render(request, 'index.html', {'data1':out.stdout.decode('UTF-8')})
