from flask import Blueprint, render_template

import requests
import yaml
import random
import boto3

bumps = Blueprint('bumps', __name__)

def retrieve_bumps():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('halbrd-bumps')
    url = lambda file: 'https://halbrd-bumps.s3-ap-southeast-2.amazonaws.com/' + file

    bumps = [ {
        # the creator field used to be used but the repo I sourced went private on github
        'creator': None,
        'source': url(bump.key)
    } for bump in list(bucket.objects.all()) ]

    return bumps


@bumps.route('/bumps/')
def index():
    bumps = retrieve_bumps()
    random.shuffle(bumps)

    return render_template('bumps/index.html',
        bumps=bumps
    )
