from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .models import ActiveIng, Drug
from .serializers import ActiveIngSerializer, DrugSerializer

@api_view(['GET'])
def ApiOverView(request):
    api_urls = {
        'all_items': '/',
        'Search By Name': '/drugs/?name=drug_name',
        'Search By Active Ingredient': '/ings/?name=ing_name',
        'Add Drug': '/drugs/create',
        'Add Active Ingredient': '/ings/create',
        'Update Drug': '/drugs/update/pk',
        'Update Active Ingredient': '/ings/update/pk',
        'Delete Drug': '/drugs/pk/delete',
        'Delete Active Ingredient': '/ings/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_ing(request):
    ing = ActiveIngSerializer(data=request.data)

    if ActiveIng.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This Active Ingredient is already added.')

    if ing.is_valid():
        ing.save()
        return Response(ing.data)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_drug(request):
    drug = DrugSerializer(data=request.data)

    if Drug.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This drug already exists!')
    
    if drug.is_valid():
        drug.save()
        return Response(drug.data)
    
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_drugs(request):
    
    #Checking for parameters for search
    if request.query_params:
        drugs = Drug.objects.filter(**request.query_params.dict())
    else:
        drugs = Drug.objects.all()
    
    if drugs:
        drug_set = DrugSerializer(drugs, many=True)
        return Response(drug_set.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_ings(request):

    #Checking for parameters for search
    if request.query_params:
        ings = ActiveIng.objects.filter(**request.query_params.dict())
    else:
        ings = ActiveIng.objects.all()

    if ings:
        items = ActiveIngSerializer(ings, many=True)
        return Response(items.data)
    else:
        return Response(stauts=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_ing(request, pk):
    ing = ActiveIng.objects.get(pk=pk)
    item = ActiveIngSerializer(instance=ing, data=request.data)

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_drug(request, pk):
    drug = Drug.objects.get(pk=pk)
    item = DrugSerializer(instance=drug, data=request.data)

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def delete_ing(request, pk):
    ing = get_object_or_404(ActiveIng, pk=pk)
    ing.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def delete_drug(request, pk):
    drug = get_object_or_404(Drug, pk=pk)
    drug.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

