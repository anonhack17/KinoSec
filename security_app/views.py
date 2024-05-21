from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import System, SecurityEvent, AccessLog
from .forms import SystemForm, SecurityEventForm

def security_events_list(request):
    events = SecurityEvent.objects.all()
    return render(request, 'security_app/security_events_list.html', {'events': events})

def delete_system(request, system_id):
    system = get_object_or_404(System, pk=system_id)
    # Логика для удаления системы
    system.delete()
    return redirect('systems_list')
def edit_system(request, system_id):
    system = get_object_or_404(System, pk=system_id)
    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            form.save()
            return redirect('systems_list')
    else:
        form = SystemForm(instance=system)
    return render(request, 'security_app/edit_system.html', {'form': form})
def systems_list(request):
    systems = System.objects.all()  # Получаем все системы из базы данных
    return render(request, 'security_app/systems_list.html', {'systems': systems})
@login_required
def dashboard(request):
    systems = System.objects.all()
    recent_events = SecurityEvent.objects.order_by('-occurred_at')[:10]
    return render(request, 'security_app/dashboard.html', {'systems': systems, 'recent_events': recent_events})

@login_required
def system_detail(request, pk):
    system = get_object_or_404(System, pk=pk)
    events = SecurityEvent.objects.filter(system=system).order_by('-occurred_at')
    return render(request, 'security_app/system_detail.html', {'system': system, 'events': events})

@login_required
def add_system(request):
    if request.method == "POST":
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SystemForm()
    return render(request, 'security_app/add_system.html', {'form': form})

@login_required
def add_security_event(request):
    if request.method == 'POST':
        form = SecurityEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('systems_list')  # Перенаправление на страницу списка систем или другую страницу
    else:
        form = SecurityEventForm()
    return render(request, 'security_app/add_security_event.html', {'form': form})