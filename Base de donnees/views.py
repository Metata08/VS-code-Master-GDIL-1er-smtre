from django.shortcuts import render, redirect
from .forms import PersonneForm

def ajouter_personne(request):
    if request.method == "POST":
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre la personne dans la base de données
            return redirect('liste_personnes')  # Redirige après la soumission du formulaire
    else:
        form = PersonneForm()

    return render(request, 'ajouter_personne.html', {'form': form})
