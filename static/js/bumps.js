// this file is heavily based on this: https://stackoverflow.com/a/52554103/4809728


// `bumps` will already be defined as a list of direct links to bumps
var bumpIndex = 0;

var videoContainer = document.getElementById('video-container');
var textOutput = document.getElementById('text-output');
var video1 = document.getElementById('video-1');
var video2 = document.getElementById('video-2');


function initVideo(video) {
    video.playsinline = true;
    video.muted = false;
    video.preload = 'auto';

    video.onplaying = function (e) {
        textOutput.innerHTML = bumpIndex;
        this.nextVideo.src = bumps[++bumpIndex % bumps.length];
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
video1.src = bumps[bumpIndex];
initVideo(video1);

// set up video2 to warm up
video2.style.display = 'none';
initVideo(video2);
