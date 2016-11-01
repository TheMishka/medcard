from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

from .models import Human, HumanDocument, PhoneNumber, PersonEmail, DiagnosisCategory, DiagnosisRelation
from .forms import NewPerson, DocumentEdit, Phone, Email


def index(request):
    return render(request, 'medcard/search.html', {})

def searchresult(request):
    query_name = ''
    query_patronymic = ''
    query_surname = ''
    query_bdate = ''
    found_card = None
    if request.GET:
        query_name = request.GET['search_name']
        query_patronymic = request.GET['search_patronymic']
        query_surname = request.GET['search_surname']
        query_bdate = request.GET['search_bdate']
        found_card = Human.objects.filter(
            name__icontains=query_name,
            surname__icontains=query_surname,
            patronymic__icontains=query_patronymic,
            birthday__icontains=query_bdate
        )
    return render(request, 'medcard/searchresult.html', {
        'query_name': query_name,
        'query_patronymic': query_patronymic,
        'query_surname': query_surname,
        'query_bdate': query_bdate,
        'found_card': found_card
    })

def new_person(request):
    if request.method == "POST":
        formPerson = NewPerson(request.POST)
        formPhone = Phone(request.POST)
        formEmail = Email(request.POST)
        if formPerson.is_valid() and formPhone.is_valid() and formEmail.is_valid():
            p_card = formPerson.save()
            p_phone = formPhone.save(commit=False)
            p_phone.human = p_card
            p_phone.save()
            p_email = formEmail.save(commit=False)
            p_email.human = p_card
            p_email.save()
            return redirect('medcard.views.personcard', person_id=p_card.id)
    else:
        formPerson = NewPerson()
        formPhone = Phone()
        formEmail = Email()
    return render(request, 'medcard/new_person.html', {'formPerson': formPerson, 'formPhone': formPhone, 'formEmail': formEmail})

def card_edit(request, person_id):
    p_card = get_object_or_404(Human, id=person_id)
    if request.method == "POST":
        formPerson = NewPerson(request.POST)
        formPhone = Phone(request.POST)
        formEmail = Email(request.POST)
        if formPerson.is_valid() and formPhone.is_valid() and formEmail.is_valid():
            p_card = formPerson.save()
            p_phone = formPhone.save(commit=False)
            p_phone.human = p_card
            p_phone.save()
            p_email = formEmail.save(commit=False)
            p_email.human = p_card
            p_email.save()
            return redirect('medcard.views.personcard', person_id=p_card.id)
    else:
        formPerson = NewPerson(instance=p_card)
        try:
            p_phone = PhoneNumber.objects.get(human=p_card)
            formPhone = Phone(instance=p_phone)
        except PhoneNumber.DoesNotExist:
            formPhone = Phone()
        try:
            p_email = PersonEmail.objects.get(human=p_card)
            formEmail = Email(instance=p_email)
        except PersonEmail.DoesNotExist:
            formEmail = Email()
    return render(request, 'medcard/new_person.html', {'formPerson': formPerson, 'formPhone': formPhone, 'formEmail': formEmail})

def about(request):
    return render(request, 'medcard/about.html', {})

def personcard(request, person_id):
    p_card = get_object_or_404(Human, id = person_id)
    try:
        p_phone = PhoneNumber.objects.get(human = p_card)
    except PhoneNumber.DoesNotExist:
        p_phone = ''
    try:
        p_email = PersonEmail.objects.get(human=p_card)
    except PersonEmail.DoesNotExist:
        p_email = ''
    return render(request, 'medcard/personcard.html', {'p_card': p_card, 'p_phone': p_phone, 'p_email': p_email})


@csrf_protect
def doc_edit(request, person_id, doc_id=''):
    p_card = get_object_or_404(Human, id=person_id)
    if doc_id != '':
        p_doc = get_object_or_404(HumanDocument, id=doc_id)
        if request.method == "POST" and request.is_ajax():
            p_doc = HumanDocument(
                id=request.POST.get("doc_id"),
                human=p_card,
                document_type=request.POST.get("doc_type"),
                document_number=request.POST.get("doc_number"),
                document_date=request.POST.get("doc_date")
            )
            p_doc.save()
            return JsonResponse({'person_id': person_id})
        else:
            form = DocumentEdit(instance=p_doc)
    else:
        p_doc = ''
        if request.method == "POST" and request.is_ajax():
            p_doc = HumanDocument(
                human=p_card,
                document_type=request.POST.get("doc_type"),
                document_number=request.POST.get("doc_number"),
                document_date=request.POST.get("doc_date")
            )
            p_doc.save()
            return JsonResponse({'person_id': person_id})
        else:
            form = DocumentEdit()
    return render(request, 'medcard/docmodal.html', {'form': form, 'p_card': p_card, 'p_doc': p_doc})


@csrf_protect
def doc_del(request):
    doc_id = request.POST.get("doc_id")
    p_doc = get_object_or_404(HumanDocument, id=doc_id)
    p_doc.delete()
    return HttpResponse("ok")


@csrf_protect
def diags_edit(request, person_id, relation_id=''):
    p_inst = get_object_or_404(Human, id=person_id)
    nodes = DiagnosisCategory.objects.all()
    if relation_id != '':
        rel_inst = get_object_or_404(DiagnosisRelation, id=relation_id)
        if request.method == "POST" and request.is_ajax():
            diags_id = request.POST.get("diags_id")
            d_inst = get_object_or_404(DiagnosisCategory, id=diags_id)
            rel_inst = DiagnosisRelation(
                id=relation_id,
                human=p_inst,
                diagnosis=d_inst,
                create_date=request.POST.get("diags_date")
            )
            rel_inst.save()
            return JsonResponse({'person_id': person_id})
    else:
        rel_inst = ''
        if request.method == "POST" and request.is_ajax():
            diags_id = request.POST.get("diags_id")
            d_inst = get_object_or_404(DiagnosisCategory, id=diags_id)
            rel_inst = DiagnosisRelation(
                human=p_inst,
                diagnosis=d_inst,
                create_date=request.POST.get("diags_date")
            )
            rel_inst.save()
            return JsonResponse({'person_id': person_id})
    return render(request, 'medcard/diagstree.html', {'nodes': nodes, 'p_inst': p_inst, 'rel_inst': rel_inst})


@csrf_protect
def diag_del(request):
    diag_id = request.POST.get("diag_id")
    rel_inst = get_object_or_404(DiagnosisRelation, id=diag_id)
    rel_inst.delete()
    return HttpResponse("ok")