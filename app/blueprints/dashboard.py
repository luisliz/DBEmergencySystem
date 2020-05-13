from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route('/', methods=['GET'])
def index():
    return "Welcome to statistics"

@dashboard_bp.route('/statistics')
def statistics():
    pass


@dashboard_bp.route('/statistics/<string:region>', methods=['GET'])
def get_stats_by_region():
    #'west': {
    #            'aguada',
    #            'aguadilla',
    #            'añasco',
    #            'cabo rojo',
    #            'guanica',
    #            'hormigueros',
    #            'isabela',
    #            'lajas',
    #            'lares',
    #            'las marias',
    #            'maricao',
    #            'mayagüez',
    #            'moca',
    #            'mona',
    #            'quebradillas',
    #            'rincón',
    #            'sabana grande',
    #            'san german',
    #            'san sebastian',
    #            'yauco',
    #        },
    #'north': {
    #             'arecibo',
    #             'barceloneta',
    #             'camuy',
    #             'Dorado',
    #             'florida',
    #             'hatillo',
    #             'manati',
    #             'toa alta',
    #             'vega alta',
    #             'vega baja',

    #         },

    #'central': {
    #               'adjuntas',
    #               'aguas',
    #               'buenas',
    #               'aibonito',
    #               'barranquitas',
    #               'cayey',
    #               'ciales',
    #               'cidra',
    #               'comerio',
    #               'corozal',
    #               'jayuya',
    #               'morovis',
    #               'naranjito',
    #               'orocovis',
    #               'utuado',

    #           },

    #'south': {
    #             'arroyo',
    #             'caja de muertos',
    #             'coamo',
    #             'guayama',
    #             'guayanilla',
    #             'juana diaz',
    #             'patillas',
    #             'peñuelas',
    #             'ponce',
    #             'salinas',
    #             'santa isabel',
    #             'villalba',
    #         },
    #'metro': {
    #             'bayamon',
    #             'carolina',
    #             'cataño',
    #             'guaynabo',
    #             'san juan',
    #             'toa baja',
    #             'trujillo alto',
    #         },
    #'east': {,
    #        'caguas',
    #        'canovanas',
    #        'ceiba',
    #        'culebra',
    #        'fajardo',
    #        'gurabo',
    #        'humacao',
    #        'juncos',
    #        'las piedras',
    #        'loiza',
    #        'luquillo',
    #        'maunabo',
    #        'naguabo',
    #        'rio grande',
    #        'san lorenzo',
    #        'yabucoa',
    #        'vieques'
    #}

    pass


@dashboard_bp.route('/statistics/<string:city>', methods=['GET'])
def get_stats_by_city():
    pass

