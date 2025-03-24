import json
import jsonpickle
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from ..models import Brand
from ..services import brandService

bp = Blueprint('brands', __name__, url_prefix='/brands')

@bp.route('/', methods=['GET', 'POST'])
def all():
    if (request.method == 'POST'):
        print(request.form.get('name'))
        print(request.form.get('country'))
        
        name = request.form.get('name')
        country = request.form.get('country')
        
        newBrand = Brand(
            name,
            country,
        )
        result = brandService.addBrand(newBrand)

    brands = brandService.getBrands()
    
    for brand in brands:
        print(brand)

    if not brands:
        return 'Brands list page. Brands list is empty! '
    
    result = []
    for brand in brands:
        result.append(brand.toJson())
    # for brand in brands:
    #     result += json.dumps(brand) + ", "
    return result

@bp.route("/<int:id>", methods=['GET', 'POST'])
def one(id):
    brand = brandService.getBrand(id)
    
    if (brand is None):
        return 'Brand info page'
    return brand