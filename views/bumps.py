from flask import Blueprint, render_template

import requests
import yaml
import random

bumps = Blueprint('bumps', __name__)

BUMPS_URL = 'https://raw.githubusercontent.com/treesnetwork/bumps/master/index.js'

def retrieve_bumps():
    bumps_payload = requests.get(BUMPS_URL).text.strip()

    # pre-parse checks
    prefix = 'module.exports = '
    suffix = ';'
    assert bumps_payload.startswith(prefix)
    assert bumps_payload.endswith(suffix)

    # trim affixes
    bumps_payload = bumps_payload[len(prefix) : len(suffix) * -1]

    # thanks @pseudoSudo
    bumps = yaml.safe_load(bumps_payload)

    def resolve_bump_source(bump):
        def sortable(quality):
            # convert XXXp quality string into number
            return int(quality.rstrip('p'))

        sources_by_quality = sorted(
            bump['source']['sources'],
            key=lambda source: sortable(source['quality']),
            reverse=True,
        )

        return sources_by_quality[0]['url']

    bumps = [ {
        'creator': bump.get('username'),  # not every bump has a username - store None instead of throwing KeyError
        'source': resolve_bump_source(bump)
    } for bump in bumps ]

    return bumps


@bumps.route('/bumps/')
def index():
    bumps = retrieve_bumps()
    random.shuffle(bumps)

    return render_template('bumps/index.html',
        bumps=bumps
    )
