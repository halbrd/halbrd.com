from flask import Blueprint, render_template

bumps = Blueprint('bumps', __name__)

@bumps.route('/bumps/')
def index():
    return render_template('bumps/index.html',
        bumps=[
            "https://player.vimeo.com/external/249463053.hd.mp4?s=e21e00dd63ab878189d39905f9e81f4c389bec87&profile_id=174",
            "https://player.vimeo.com/external/249463124.hd.mp4?s=c3f5c12969c711bb945314cb1b6517993936a43e&profile_id=174",
            "https://player.vimeo.com/external/249463125.hd.mp4?s=da7b1365cf462a4afc1305a3235d675f046657fd&profile_id=174"
        ]
    )
