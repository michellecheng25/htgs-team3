from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseServerError

from chemistry.compounds import search_compounds, get_molecule_info
from compound_search.models import Compound


@require_GET
def search(request: HttpRequest):
    try:
        smiles_query = request.GET.get("query", "")
        all_smiles = [compound.smiles for compound in Compound.objects.all()]
        smiles_matching_query = all_smiles
        if smiles_query != "":
            match_indices_list = search_compounds(smiles_query, all_smiles)
            smiles_matching_query = [
                all_smiles[i]
                for i, match_indices in enumerate(match_indices_list)
                if len(match_indices) > 0
            ]

        properties = []
        for match in smiles_matching_query:
            prop = get_molecule_info(match)
            properties.append(prop)

        mylist = zip(smiles_matching_query, properties)
        result_length = len(smiles_matching_query)

        return render(
            request,
            "compound_search/search.html",
            {
                "result_length": result_length,
                "smiles_list": mylist,
                "smiles_query": smiles_query,
                "properties_list": properties,
            },
        )
    except Exception as e:
        print(f"Error: {e}")
        return render(
            request,
            "compound_search/search.html",
            {
                "smiles_list": [],
                "smiles_query": "",
                "error_message": "An error occurred while processing your request. Please try again.",
            },
        )


@require_POST
def add_compounds(request: HttpRequest):
    smiles = request.POST.get("smiles_list", None)
    smiles_list = [s.strip() for s in smiles.splitlines() if s.strip() != ""]
    for smiles in smiles_list:
        Compound.objects.create(smiles=smiles).save()

    # Redirect back to the page you were on
    return HttpResponseRedirect(request.headers.get("Referer"))
