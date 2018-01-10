from django.shortcuts import render
from SmartHome import config

def dashboard(request):
    print(config.espModuleConfig.items())
    for (k, v) in config.espModuleConfig.items():
        print(v.name)
        for (i, j) in v.pin.items():
            print(j.pin_no + " --- " + j.description)
    return render(request, "ControlElectricAppliances/dashboard.html",{
        'espModelList': config.espModuleConfig
    })
