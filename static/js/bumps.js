// TODO: make it loop

// this file is heavily based on this: https://stackoverflow.com/a/52554103/4809728


// `bumps` will already be defined as a list of direct links to bumps
var bumpIndex = 0;

var videoContainer = document.getElementsByTagName('figure')[0];
var textOutputs = document.getElementsByTagName('figcaption');
var video1 = document.getElementsByTagName('video')[0];
var video2 = document.getElementsByTagName('video')[1];


function initVideo(video) {
    video.playsinline = true;
    video.muted = false;
    video.preload = 'auto';

    video.onplaying = function (e) {
        bumpsIndex = ++bumpIndex % bumps.length;

        for (textOutput of textOutputs) {
            if (bumps[bumpIndex]['creator']) {
                textOutput.innerHTML = 'Created by @' + bumps[bumpIndex]['creator'];
            }
        }

        this.nextVideo.src = bumps[bumpIndex]['source'];
        this.nextVideo.pause();
    }

    video.onended = function (e) {
        this.style.display = 'none';
        this.nextVideo.style.display = 'revert';
        this.nextVideo.play();
    }
}


video1.nextVideo = video2;
video2.nextVideo = video1;

// set up video1 to play
video1.autoplay = true;
video1.src = bumps[bumpIndex]['source'];
initVideo(video1);

// set up video2 to warm up
video2.style.display = 'none';
initVideo(video2);
