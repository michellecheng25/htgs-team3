from django.http import HttpRequest, HttpResponse

from chemistry.compounds import get_highlighted_image, smiles_to_svg


def generate_image(request: HttpRequest, smiles: str):
    highlighted_substructure = request.GET.get("highlight", "")
    if highlighted_substructure == "":
        return HttpResponse(smiles_to_svg(smiles), content_type="image/svg+xml")
    else:
        return HttpResponse(
            get_highlighted_image(smiles, highlighted_substructure),
            content_type="image/svg+xml",
        )
